from django.db import models

from .choices import ProjectStatus, ProjectRole


class Project(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True)
    long_description = models.TextField(blank=True)
    site_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=ProjectStatus.choices, blank=True)

    thumbnail = models.ForeignKey('portfolio.Image', on_delete=models.SET_NULL, blank=True, null=True)
    technologies = models.ManyToManyField('portfolio.Technology', help_text='Technologies used for this project.', blank=True, related_name='projects')

    def __str__(self):
        return self.title


class Contributor(models.Model):
    name = models.CharField(max_length=255)
    
    image = models.ForeignKey('portfolio.Image', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Contribution(models.Model):
    role = models.CharField(max_length=50, choices=ProjectRole.choices, default=ProjectRole.COLLABORATOR)
    description = models.TextField(null=True, blank=True)

    contributor = models.ForeignKey('portfolio.Contributor', on_delete=models.CASCADE, related_name='contributions')
    project = models.ForeignKey('portfolio.Project', on_delete=models.CASCADE, related_name='contributions')

    def __str__(self):
        return f'{self.contributor.name}\'s Contribution'


class Image(models.Model):
    alt = models.CharField('alt / title', max_length=255)
    file = models.ImageField(upload_to='images/', blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.alt


class Icon(models.Model):
    alt = models.CharField('alt / title', max_length=255)
    file = models.ImageField(upload_to='icons/', blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.alt


class Download(models.Model):
    title = models.CharField('title', max_length=255)
    file = models.FileField(upload_to='downloads/', blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Technology(models.Model):
    title = models.CharField(max_length=255)

    icon = models.ForeignKey('portfolio.Icon', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'technologies'

    def __str__(self):
        return self.title


class Review(models.Model):
    body = models.TextField()
    author_name = models.CharField(max_length=255, blank=True)
    author_image = models.ImageField()
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.author_name}\'s Review'

