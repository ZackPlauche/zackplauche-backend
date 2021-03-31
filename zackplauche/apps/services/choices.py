from django.db.models import TextChoices


class LegalStructure(TextChoices):
    SP = 'sole proprietor'
    PS = 'partnership'
    LLC = 'limited liability company'
    CORP = 'corporation'
    S_CORP = 's corporation'


class ServiceType(TextChoices):
    PRIMRARY = 'primary'
    STANDARD = 'standard'
    MICROSERVICE = 'microservice'


class PaymentType(TextChoices):
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


class OrderStatus(TextChoices):
    PENDING = 'pending'
    APPROVED = 'approved'
    IN_PROGRESS = 'in_progress'
    FULFILLED = 'fulfilled'
