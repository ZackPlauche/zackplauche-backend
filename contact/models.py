from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email
