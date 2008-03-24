from django.db import models
from money.contrib.django.models.fields import *
from money.contrib.django.models.managers import *
from money import Money


class Entity(models.Model):
    name = models.CharField(max_length=100)
    price = MoneyField(max_digits=12, decimal_places=3)
    
    objects = MoneyManager()
    
    def __unicode__(self):
        return self.name + " " + str(self.price)


class Entity_0_USD(models.Model):
    name = models.CharField(max_length=100)
    price = MoneyField(max_digits=12, decimal_places=3, default=Money(0, "USD"))
    
    objects = MoneyManager()
    
    def __unicode__(self):
        return self.name + " " + str(self.price)


class Entity_USD(models.Model):
    name = models.CharField(max_length=100)
    price = MoneyField(max_digits=12, decimal_places=3, default_currency="USD")
    
    objects = MoneyManager()
    
    def __unicode__(self):
        return self.name + " " + str(self.price)
