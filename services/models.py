from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from base.models import User
from tinymce.models import HTMLField
from base.models import Contact
import uuid


class Deliverable(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Service(models.Model):

    CALL_TO_ACTION_CHOICES = [
        ('Sell', (
            ('Order Now', 'Order Now'),
            ('Hire Zack', 'Hire Zack'),
            ('Hire My Team', 'Hire My Team'),
            ('Book a Call', 'Book a Call'),
            ('Get Training', 'Get Training'),
        )
        ),
        ('Contact', (
            ('Contact Us', 'Contact Us'),
            ('Get Help Now', 'Get Help Now'),
            ('Get in Touch', 'Get in Touch'),
        )
        )
    ]

    icon = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(max_length=500, default='', help_text='Max characters: 500')
    long_description = HTMLField(blank=True, default='', help_text='Optional long description for service page.')
    created_date = models.DateTimeField(auto_now_add=True)
    deliverables = models.ManyToManyField(Deliverable)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    call_to_action = models.CharField(max_length=30, choices=CALL_TO_ACTION_CHOICES, default='Order Now')
    display = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    @property
    def price_display(self):
        return f'${self.price} USD'

    def __str__(self):
        return self.title


class Order(models.Model):
    service = models.ForeignKey(Service, related_name='orders', on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')
    email = models.EmailField('email address', unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name

    @property
    def order_total(self):
        price = f'${str(self.service.price)} USD'
        return price

    def __str__(self):
        return self.email

class Testimonial(models.Model):
        
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    headline = models.CharField('title', max_length=255, default='')
    body = models.TextField(default='')
    order = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.headline

    

    class Meta:
        ordering = ['order']