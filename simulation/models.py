from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator

from django_countries.fields import CountryField


class Customer(models.Model):
    logo = models.ImageField(upload_to='upload/logos/')
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class SalesforceCloud(models.Model):
    icon = models.ImageField(upload_to='upload/salesforce/')
    name = models.CharField(max_length=100)
    descriptor = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class NoName(models.Model):
    use_cases = models.TextField()
    industry = models.CharField(max_length=100)
    vertical = models.CharField(max_length=100)
    country = CountryField()

    customer = models.ForeignKey(Customer, related_name='no_names')
    clouds = models.ManyToManyField(SalesforceCloud, related_name='no_names')

    def __unicode__(self):
        return str(self.customer)

class Asset(models.Model):
    name = models.CharField(max_length=100)
    link = models.TextField(validators=[URLValidator()])

    no_name = models.ForeignKey(NoName, related_name='assets')

    def __unicode__(self):
        return self.name