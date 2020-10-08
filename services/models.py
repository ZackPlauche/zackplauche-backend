import uuid
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from tinymce.models import HTMLField
from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

from .managers import ServiceManager, OrderManager

class Client(models.Model): 
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user}'

    @property
    def total_orders(self):
        return self.orders.count()

class Company(models.Model):
    class LegalStructure(models.TextChoices):
        SP = 'sole proprietor'
        PS = 'partnership'
        LLC = 'limited liability company'
        CORP = 'corporation'
        S_CORP = 's corporation'
    
    clients = models.ManyToManyField('client', related_name='companies')
    parent_company = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/', blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    legal_stucture = models.CharField(choices=LegalStructure.choices, max_length=255)
    is_sponsor = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Deliverable(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Service(models.Model):

    class ServiceType(models.TextChoices):
        PRIMRARY = 'primary'
        STANDARD = 'standard'
        MICROSERVICE = 'microservice'


    class PaymentType(models.TextChoices):
        IN_FULL = 'in full'
        SPLIT_PAYMENTS = 'split payments'
        HOURLY = 'hourly'


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

    icon = models.ImageField(upload_to='images/', blank=True)
    service_type = models.CharField('type', max_length=50, choices= ServiceType.choices, default=ServiceType.STANDARD)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(editable=False, max_length=255, unique=True)
    short_description = models.TextField(max_length=500, default='', help_text='Max characters: 500')
    long_description = HTMLField(default='', help_text='Long description (optional)')
    created_date = models.DateTimeField(auto_now_add=True)
    deliverables = models.ManyToManyField(Deliverable, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.00'), validators=[MinValueValidator(Decimal('0.00'))])
    payment_type = models.CharField(max_length=50, choices=PaymentType.choices, default=PaymentType.IN_FULL)
    call_to_action = models.CharField(max_length=30, choices=CALL_TO_ACTION_CHOICES, default='Order Now')
    order = models.PositiveSmallIntegerField(blank=False, null=False, default=0)
    display = models.BooleanField(default=True)

    objects = ServiceManager()

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    @property
    def price_display(self):
        if self.payment_type == self.PaymentType.IN_FULL:
            return f'${self.price}'
        elif self.payment_type == self.PaymentType.HOURLY:
            return f'${self.price} /hr'
    
    def get_absolute_url(self):
        return reverse("services:service_detail", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.title


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending'
        APPROVED = 'approved'
        IN_PROGRESS = 'in_progress'
        FULFILLED = 'fulfilled'
        
    client = models.ForeignKey(Client, related_name='orders', on_delete=models.SET_NULL, null=True)
    services = models.ManyToManyField(Service, related_name='orders')
    status = models.CharField(max_length=50, choices=Status.choices, default='')
    id = models.UUIDField('order id', primary_key=True, default=uuid.uuid4, editable=False)
    price_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    objects = OrderManager()

    def __str__(self):
        return str(self.id)


class Testimonial(models.Model):
    client = models.ForeignKey(Client, blank=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    headline = models.CharField('title', max_length=255, default='')
    body = models.TextField(default='')
    order = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-date']
    def __str__(self):
        return self.headline