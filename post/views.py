# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Country, Post, Category, Good
from django.http import HttpResponse


def posts(request):

    posts = Post.objects.all().order_by('data_publ')
    s=''
    for p in posts:
        s = s + str(p.id) +  p.__str__() + "<br>"

    return HttpResponse(s)




def index(request, id):
    #cat_id = request.GET['id']

    if id == None:
        cat = Category.objects.first()
    else:
        try:
            cat = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            cat = cat = Category.objects.first()


    goods = Good.objects.filter(category=cat).order_by('name')

    s = "Category: " + cat.name + "<br><br>"
    for good in goods:
        s = s + "(" + str(good.pk) + ")" + good.name + "<br>"
    return HttpResponse(s)



def good(request, id):
    goods = Good.objects.all().order_by('-price')
    s = ""
    if id == None:
        for good in goods:
            s = s + "(" + str(good.pk) + ")" + good.name + " - " + str(good.price) + " cat:  " + good.category.name + "<br>"
    else:
        good = Good.objects.get(pk=id)
        s = "(" + str(good.pk) + ")" + good.name + " - " +str(good.price) + "<br>"

    return HttpResponse(s)




