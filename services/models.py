import uuid
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from tinymce.models import HTMLField
from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator

from base.models import User


class Client(models.Model): 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150, blank=True, default='')
    company_website = models.URLField(default='', blank=True)
    company_logo = models.ImageField(upload_to='company_logos', blank=True)
    address_one = models.CharField('address 1', max_length=255, blank=True, default='')
    address_two = models.CharField('address 2', max_length=255, blank=True, default='')

    def __str__(self):
        return f'{self.user}'


    @property
    def total_orders(self):
        return self.orders.count()


class Deliverable(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class ServiceManager(models.Manager):

    def services(self):
        return self.get_queryset().filter(
            service_type=self.model.ServiceType.SERVICE)
    
    def microservices(self):
        return self.get_queryset().filter(
            service_type=self.model.ServiceType.MICROSERVICE)


class Service(models.Model):


    class ServiceType(models.TextChoices):
        SERVICE = 'service'
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
    service_type = models.CharField('type', max_length=50, choices= ServiceType.choices, default=ServiceType.SERVICE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
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


class OrderManager(models.Manager):

    def pending(self):
        return self.get_queryset().filter(status=self.model.Status.PENDING)

    def approved(self):
        return self.get_queryset().filter(status=self.model.Status.APPROVED)

    def in_progress(self):
        return self.get_queryset().filter(status=self.model.Status.IN_PROGRESS)

    def fulfilled(self):
        return self.get_queryset().filter(status=self.model.Status.FULFILLED)
    

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
    date = models.DateTimeField(auto_now_add=True)

    objects = OrderManager()

    def __str__(self):
        return str(self.id)


    @property
    def total(self):
        if self.services.exists():
            total = round(self.services.aggregate(total_price=models.Sum('price'))['total_price'], 2)
        else:
            total = Decimal('0.00')
        return f'${total}'


class Testimonial(models.Model):
    client = models.ForeignKey(Client, blank=True, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=50, default='')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField('client name', max_length=150)
    headline = models.CharField('title', max_length=255, default='')
    body = models.TextField(default='')
    order = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-date']
    def __str__(self):
        return self.headline