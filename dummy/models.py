from __future__ import unicode_literals

from django.db import models


class DummyModel(models.Model):

    char_field = models.CharField(max_length=100)
    csv_integers = models.CommaSeparatedIntegerField(max_length=200)
    logo = models.ImageField(upload_to='upload/logos/')
    text_field = models.TextField()

    def __unicode__(self):
        return self.char_field


class CharFieldModel(models.Model):
    char_field = models.CharField(max_length=100)
    dummy = models.ForeignKey(DummyModel, related_name='csv_chars')

    def __unicode__(self):
        return self.char_field


class ImageFieldModel(models.Model):
    img_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='upload/related/')
    dummies = models.ManyToManyField(DummyModel, related_name='images')

    def __unicode__(self):
        return self.img_name