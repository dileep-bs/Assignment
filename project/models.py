# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=150,unique=True)
    profile = models.TextField()

    def __str__(self):
        return self.name