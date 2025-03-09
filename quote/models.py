from django.db import models
from django.utils.timezone import now

class QuoteRequest(models.Model):
    contact_name = models.CharField(max_length=255, default="Unknown Name")
    company_name = models.CharField(max_length=255, default="Unknown Company")
    address = models.TextField(default="No address provided")
    website = models.URLField(blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50, default="No phone provided")
    quote_number = models.CharField(max_length=50, unique=True, default="No quote# provided")
    date = models.DateField(default=now)
    description = models.TextField(default="No description provided")

    def __str__(self):
            return f"{self.contact_name} ({self.company_name})"

class Application(models.Model):
    contact_name = models.CharField(max_length=255, default="Unknown Name")
    company_name = models.CharField(max_length=255, default="Unknown Company")
    address = models.TextField(default="No address provided")
    website = models.URLField(blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50, default="No phone provided")
    quote_number = models.CharField(max_length=50, unique=True, default="No quote# provided")
    date = models.DateField(default=now)
    description = models.TextField(default="No description provided")

    def __str__(self):
            return f"{self.contact_name} ({self.company_name})"