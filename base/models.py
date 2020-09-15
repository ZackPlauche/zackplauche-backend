from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator, MinValueValidator

# Define your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def full_name(self): 
        return f'{self.first_name} {self.last_name}'

        
class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    messages = models.JSONField(default=list)

    def __str__(self):
        return self.user.__str__()

class Skill(models.Model):
    class Color(models.TextChoices):
        BLUE = 'blue'
        GREEN = 'green'
        GREY = 'grey'
        RED = 'red'
        WHITE = 'white'
        YELLOW = 'yellow'

    title = models.CharField(max_length=100)
    progress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    color = models.CharField(max_length=10, choices=Color.choices, default='White')

    def __str__(self):
        return self.title


