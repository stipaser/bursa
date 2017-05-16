# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

PARTS_OF_WORLD = (
    (1, "US"),
    (2, "EU"),
    (3, "CSI"),
    (4, "REST")
)

class Country(models.Model):

    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=3, unique=True)
    part = models.IntegerField(choices=PARTS_OF_WORLD, default=None, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Post(models.Model):

    plecat_din = models.ForeignKey(Country, related_name="plecat", null=True, blank=True)
    sosit_in = models.ForeignKey(Country, related_name="sosit", null=True, blank=True)
    data_publ = models.DateTimeField(auto_now=True, verbose_name='data postarii')
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.plecat_din, self.sosit_in)

    class Meta:
        ordering = ['-data_publ']
        verbose_name = "Postari transport"

################################################## dupa carte
class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Good(models.Model):

    name = models.CharField(max_length=50, unique=True, verbose_name='Denumire')
    category = models.ForeignKey(Category, null=True, blank=True)
    price = models.FloatField(verbose_name='Price')
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='Stoc')

    def get_is_stock(self):
        if self.in_stock:
            return "+"
        else:
            return "-"

    def __str__(self):
        return '%s (%s)' % (self.name, self.get_is_stock())

    class Meta:
        ordering = ['name', '-price']

    # comments
