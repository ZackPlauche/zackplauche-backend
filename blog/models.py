from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.urls import reverse
from django.utils import timezone


class Author(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def delete(self, *args, **kwargs):
        self.user.delete()
        super().delete()


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, related_name='articles', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, default="https://via.placeholder.com/1800x1200")
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(editable=False, max_length=255, unique=True)
    body = HTMLField(default='')
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    related_service = models.ForeignKey('services.Service', on_delete=models.SET_NULL, null=True, blank=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.published and not self.published_date:
            self.published_date = timezone.now()
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={'slug': self.slug})


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}\'s comment {self.date_created.date}'
