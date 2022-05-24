from django.db import models


class Partner(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'partner')


class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'service')
