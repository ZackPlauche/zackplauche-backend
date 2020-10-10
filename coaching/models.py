from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from decimal import Decimal

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.name
    
class Session(models.Model):
    student = models.ForeignKey('coaching.Student', on_delete=models.DO_NOTHING)
    duration = models.DurationField()
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('70.00'))
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()
