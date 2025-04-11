from django.db import models

class Ad1(models.Model):
    pass

class Photo(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title
