from django.db import models
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator, MinValueValidator

# Define your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email

class Skill(models.Model):
    title = models.CharField(max_length=100)
    progress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    COLOR_CHOICES = [
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Grey', 'Grey'),
        ('Red', 'Red'),
        ('White', 'White'),
        ('Yellow', 'Yellow'),
    ]
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='White')

    def __str__(self):
        return self.title

class Value(models.Model):
    icon = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100, null=True)
    description = HTMLField(blank=True, null=True)

    def __str__(self):
        return self.name
