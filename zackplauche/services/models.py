import uuid
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from tinymce.models import HTMLField
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

from .choices import (
    OrderStatus,
    LegalStructure,
    ServiceType,
    PaymentType,
    CALL_TO_ACTION_CHOICES
)

class Client(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

    @property
    def total_orders(self):
        return self.orders.count()


class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/', blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    legal_stucture = models.CharField(choices=LegalStructure.choices, max_length=255)
    is_sponsor = models.BooleanField(default=False)
    worked_with = models.BooleanField(default=False)

    clients = models.ManyToManyField('client', related_name='companies', blank=True)
    parent_company = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class Deliverable(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Service(models.Model):
    icon = models.ImageField(upload_to='images/', blank=True)
    service_type = models.CharField('type', max_length=50, choices=ServiceType.choices, default=ServiceType.STANDARD)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(editable=False, max_length=255, unique=True)
    short_description = models.TextField(max_length=500, default='', help_text='Max characters: 500')
    long_description = HTMLField(default='', help_text='Long description (optional)')
    created_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.00'), validators=[MinValueValidator(Decimal('0.00'))])
    payment_type = models.CharField(max_length=50, choices=PaymentType.choices, default=PaymentType.IN_FULL)
    call_to_action = models.CharField(max_length=30, choices=CALL_TO_ACTION_CHOICES, default='Order Now')
    order = models.PositiveSmallIntegerField(blank=False, null=False, default=0)
    display = models.BooleanField(default=True)

    deliverables = models.ManyToManyField(Deliverable, blank=True)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    @property
    def price_display(self):
        if self.payment_type == PaymentType.IN_FULL:
            return f'${self.price}'
        elif self.payment_type == PaymentType.HOURLY:
            return f'${self.price} /hr'

    def get_absolute_url(self):
        return reverse("services:service_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Order(models.Model):
    status = models.CharField(max_length=50, choices=OrderStatus.choices, default='')
    id = models.UUIDField('order id', primary_key=True, default=uuid.uuid4, editable=False)
    price_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    client = models.ForeignKey(Client, related_name='orders', on_delete=models.SET_NULL, null=True)
    services = models.ManyToManyField(Service, related_name='orders')

    def __str__(self):
        return str(self.id)


class Testimonial(models.Model):
    title = models.CharField(max_length=255, null=True)
    body = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    client = models.ForeignKey(Client, blank=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        ordering = ['order', '-date']

    def __str__(self):
        return self.headline
