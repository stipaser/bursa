# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Country, Post, Category, Good
from django.http import HttpResponse, Http404


def posts(request):

    posts = Post.objects.all().order_by('data_publ')
    return render(request, 'post/post.html', {'posts': posts})


def post_detail(req, id):

    post = Post.objects.get(pk=id)
    p = Post.objects.first()
    return render(req, 'post/post_detail.html', {"post": post, 'p': p})





def index(request, id):
    #cat_id = request.GET['id']
    cats = Category.objects.all().order_by('name')

    if id == None:
        cat = Category.objects.first()
    else:
        try:
            cat = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            raise Http404


    goods = Good.objects.filter(category=cat).order_by('name')

    context = {"category": cat, "cats": cats, "goods": goods}
    return render(request, 'index.html', context)



def good(request, id):
    goods = Good.objects.all().order_by('-price')
    s = ""
    if id == None:
        good = Good.objects.first()
    else:
        try:
            good = Good.objects.get(pk=id)
        except Good.DoesNotExist:
            raise Http404


    return render(request, 'good.html', {'good': good})




