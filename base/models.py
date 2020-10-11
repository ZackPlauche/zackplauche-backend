from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator, MinValueValidator

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    messages = models.JSONField(default=list)

    def __str__(self):
        return self.user.email


        
