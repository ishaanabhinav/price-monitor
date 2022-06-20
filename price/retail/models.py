
from django.db import models
from datetime import datetime

from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
import brands.models as brand_models
from django.db.models.signals import post_save, post_init


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

    def __str__(self):
        return u"%s - %s - %s" % (self.id, self.name, self.location)

    class Meta:
        ordering = ['id']

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    product = models.ForeignKey(
        brand_models.Product, on_delete=models.CASCADE, blank=False, null=False
    )
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, blank=False, null=False
    )
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField(null=False, default=0)
    
    previous_price = None
    
    class Meta:
        ordering = ['id']

    @staticmethod
    def post_save(sender, instance, created, **kwargs):
        print("State")
        print(instance.price)
        print(instance.previous_price)
        if instance.previous_price.amount > instance.price.amount:
            alert = Alert()
            alert.product = instance.product
            alert.store = instance.store
            alert.alert_status = Alert.OPEN
            alert.alert_type = Alert.PRICE_DECREASE
            alert.old_price = instance.previous_price
            alert.new_price = instance.price
            alert.save()

    @staticmethod
    def remember_state(sender, instance, **kwargs):
        instance.previous_price = instance.price

post_save.connect(Inventory.post_save, sender=Inventory)
post_init.connect(Inventory.remember_state, sender=Inventory)

class Promotion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    product = models.ForeignKey(
        brand_models.Product, on_delete=models.CASCADE, blank=False, null=False
    )
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, blank=False, null=False
    )

    promo_code = models.CharField(max_length=1000, blank=False, null=True)

    start_date = models.DateTimeField(null=False,blank=False)
    end_date = models.DateTimeField(null=False,blank=False)

    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

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
        brand_models.Product, on_delete=models.CASCADE, blank=False, null=False
    )
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, blank=False, null=False
    )
    old_price = MoneyField(max_digits=14, decimal_places=2, default_currency='INR',default=0.0)
    new_price = MoneyField(max_digits=14, decimal_places=2, default_currency='INR',default=0.0)
    alert_status = models.PositiveIntegerField(choices=ALERT_STATUS_CHOICE, null=False)
    alert_type = models.PositiveIntegerField(choices=ALERT_STATUS_CHOICE, null=False)

    added_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(null=True)

    class Meta:
        ordering = ['id']
    