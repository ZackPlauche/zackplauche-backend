from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Service(models.Model):
    call_to_action_choices = [
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
    short_description = models.TextField(
        max_length=500,
        null=True,
        help_text='Max characters: 500',
    )
    long_description = HTMLField(default="Lorem Ipsum")
    created_date = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0.00,
        blank=True,
    )
    call_to_action = models.CharField(
        max_length=30,
        choices=call_to_action_choices,
        default="Order Now"
    )
    display = models.BooleanField(default=True)

    @property
    def slug(self):
        # Service.objects.filter(title=self.title).exists()
        return slugify(self.title)

    def __str__(self):
        return self.title
