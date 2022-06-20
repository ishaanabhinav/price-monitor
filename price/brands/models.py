from django.db import models
from datetime import datetime

from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    country_origin = CountryField()
    countries = CountryField(multiple=True)

    def __str__(self):
        return u"%s - %s" % (self.id, self.name)

    class Meta:
        ordering = ['id']

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=1000, blank=True, null=True)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, blank=False, null=False
    )
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"%s - %s - %s" % (self.id, self.name, self.type)

    class Meta:
        ordering = ['id']