from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return slugify(self.title)
