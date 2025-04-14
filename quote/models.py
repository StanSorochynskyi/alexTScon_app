from django.db import models
from django.utils.timezone import now
from django.db import IntegrityError
import itertools

class QuoteRequest(models.Model):
    processed = models.BooleanField(default=False)
    contact_name = models.CharField(max_length=255, default=" ")
    address = models.CharField(max_length=255, default=" ")
    email = models.EmailField()
    phone_number = models.CharField(max_length=50, default=" ")
    date = models.DateField(default=now)
    description = models.TextField(default=" ")

    def __str__(self):
        return f"{self.contact_name} ({self.date})"
