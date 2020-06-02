from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
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

    icon = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100, unique=True)
    short_description = models.TextField(max_length=500, null=True, help_text='Max characters: 500')
    long_description = HTMLField(blank=True, null=True, help_text="Optional long description for service page.")
    created_date = models.DateTimeField(default=timezone.now)
    deliverables = models.ManyToManyField(Deliverable)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, blank=True)
    call_to_action = models.CharField(max_length=30, choices=CALL_TO_ACTION_CHOICES, default="Order Now")
    display = models.BooleanField(default=True)

    @property
    def slug(self):
        # Service.objects.filter(title=self.title).exists()
        return slugify(self.title)

    def __str__(self):
        return self.title


class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    email = models.EmailField(unique=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_date = models.DateTimeField(auto_now=True)

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
