from django.db import models
from datetime import datetime

from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
from brands.models import Brand,Product

class Store(models.Model):
    RETAIL = 0
    WHOLE_SALE = 1
    STORE_TYPE_CHOICE = [
        (RETAIL, 'RETAIL'),
        (WHOLE_SALE, 'WHOLE_SALE'),
    ]

    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    store_type = models.PositiveIntegerField(choices=STORE_TYPE_CHOICE, null=False)
    country = CountryField()
    location = models.CharField(max_length=1000, blank=False, null=False)

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=False, null=False
    )
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, blank=False, null=False
    )
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField(null=False, default=0)

class Promotion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=False, null=False
    )
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, blank=False, null=False
    )

    start_date = models.DateTimeField(null=False,blank=False)
    end_date = models.DateTimeField(null=False,blank=False)

    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Alert(models.Model):
    OPEN = 0
    RESOLVED = 1
    ALERT_STATUS_CHOICE = [
        (OPEN, 'OPEN'),
        (RESOLVED, 'RESOLVED'),
    ]

    PRICE_INCREASE = 0
    PRICE_DECREASE = 1
    ALERT_TYPE_CHOICE = [
        (PRICE_INCREASE, 'PRICE_INCREASE'),
        (PRICE_DECREASE, 'PRICE_DECREASE'),
    ]

    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=False, null=False
    )
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, blank=False, null=False
    )
    alert_status = models.PositiveIntegerField(choices=ALERT_STATUS_CHOICE, null=False)
    alert_type = models.PositiveIntegerField(choices=ALERT_STATUS_CHOICE, null=False)

    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    