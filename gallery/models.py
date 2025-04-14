from django.db import models

class Promo(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    link = models.CharField(blank=True, max_length=1000)

    def __str__(self):
        return f"Promo for {self.title}"

class Advertize(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/advertize')
    link = models.CharField(blank=True, max_length=1000)

    def __str__(self):
        return f"Advertize for {self.title}"

class Annonsment(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    link = models.CharField(blank=True, max_length=1000)

    def __str__(self):
        return f"Annonsment for {self.title}"

class Photo(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title

class Contact(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    link = models.CharField(blank=True, max_length=1000)

    def __str__(self):
        return f"Contact for {self.title}"
