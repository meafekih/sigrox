from django.db import models

class user(models.Model):
    firstName = models.CharField(max_length=50)
    lastName  = models.CharField(max_length=50)
    phone     = models.IntegerField(null=True)
    create_at = models.DateField(null=True)

# Create your models here.

us = user(lastName='ab', firstName='cd', phone=332, create_at='2023-02-23')
us.save()