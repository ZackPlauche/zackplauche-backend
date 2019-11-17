from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Service(models.Model):
    icon = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100, unique=True)
    short_description = models.TextField(max_length=500, null=True, help_text='Max characters: 500')
    long_description = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, blank=True)

    @property
    def slug(self):
        # Service.objects.filter(title=self.title).exists()
        return slugify(self.title)


    def __str__(self):
        return self.title

# class Tier(models.Model):
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     tier_title = models.CharField(max_length=50)
#     deliverables = models.TextField()
#     price = models.FloatField()
#
# class Review(models.Model):
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     star_rating  = models.FloatField()
#     headline = models.CharField(max_length=200)
#     review_text = models.TextField()
#     client_first_name = models.CharField(max_length=20)
#     client_last_name = models.CharField(max_length=20)
#     client_full_name = f"{client_first_name} {client_last_name}"
#
#     def __str__(self):
#         return self.headline
