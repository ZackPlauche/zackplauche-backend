from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Author(models.Model):
    profile_picture = models.ImageField(upload_to='images/', blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=60, unique=True)
    body = HTMLField(null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True, help_text="You can only choose 1 tag per post.")
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()
    display = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_date']

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
