# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Country, Post, Category, Good

def show_posts(requests):

    posts = Post.objects.all()




