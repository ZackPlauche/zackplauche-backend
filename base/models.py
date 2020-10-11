from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.mail import send_mail
from django.conf import settings

from .managers import UserManager

# Define your models here.
class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    username = None
    email = models.EmailField('email address', unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='https://via.placeholder.com/400')
    is_client = models.BooleanField('client status', default=False)
    is_author = models.BooleanField('author status', default=False)
    is_contact = models.BooleanField('contact status', default=False)

    objects = UserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.is_contact = hasattr(self, 'contact')
        self.is_client = hasattr(self, 'client')
        self.is_author = hasattr(self, 'author')
        return super().save(*args, **kwargs)

    @property
    def full_name(self): 
        return f'{self.first_name} {self.last_name}'

        
class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    messages = models.JSONField(default=list)

    def __str__(self):
        return self.user.email

    def delete(self):
        self.user.delete()
        super().delete()

    def message_received_confirmation(self, message):
        send_mail(
            f'We\'ve recieved your message! (ZackPlauché.com)',
            f'Hi {self.user.first_name}!\n\n'
            'We\'ve recieved your message and will get back to you as soon as we can.\n\n'
            f'Your message:\n\n{message}',
            settings.DEFAULT_FROM_EMAIL,
            [self.user.email]
        )

    def new_message_notification(self, message):
        send_mail(
            f'Contact {self.user.full_name} ({self.user.email}) sent a message.',
            f'Contact {self.user.full_name} ({self.user.email}) sent a message.\n\nMessage:\n\n{message}',
            settings.DEFAULT_FROM_EMAIL,
            settings.CUSTOMER_SUPPORT_EMAILS,
        )

    def new_contact_notification(self):
        send_mail(
            f'New Contact {self.user.full_name} ({self.user.email}) added.',
            f'A new contact {self.user.full_name} was added to the database.',
            settings.DEFAULT_FROM_EMAIL,
            settings.CUSTOMER_SUPPORT_EMAILS,
        )

    def newsletter_signup_confirmation(self):
        send_mail(
            f'You\'ve successfully signed up for the Zack Plauché newsletter!',
            (
                'Hey there!\n\n'
                'This is a confirmation email confirming that you\'ve successfully joined the Zack Plauché newsletter :)'
            ),
            settings.DEFAULT_FROM_EMAIL,
            [self.user.email],
        )
    
    def newsletter_signup_notification(self):
        send_mail(
            f'A new user ({self.user.email}) has signed up for the newsletter! (zackplauche.com)',
            f'The user {self.user.email} has signed up through the newsletter form.',
            settings.DEFAULT_FROM_EMAIL,
            settings.CUSTOMER_SUPPORT_EMAILS,
        )
        

        
