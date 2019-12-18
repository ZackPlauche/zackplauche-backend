from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    content = HTMLField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return slugify(self.title)

class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=200)

    def __str__(self):
        return self.title
