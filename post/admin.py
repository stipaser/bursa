# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Country, Post, Good, Category

# Register your models here.

admin.site.register(Post)
admin.site.register(Country)
admin.site.register(Good)
admin.site.register(Category)
