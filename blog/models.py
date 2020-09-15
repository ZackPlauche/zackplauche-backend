from django.db import models
from django.utils.text import slugify
from base.models import User
from tinymce.models import HTMLField
from django.urls import reverse
from django.utils import timezone


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def delete(self, *args, **kwargs):
        self.user.delete()
        super().delete()

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, default="https://i2.wp.com/quidtree.com/wp-content/uploads/2020/01/placeholder.png?fit=1200%2C800&ssl=1")
    title = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(null=True)
    body = HTMLField(default='')
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_date']

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.published and not self.published_date:
            self.published_date = timezone.now()
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}\'s comment {date_created.date}'
