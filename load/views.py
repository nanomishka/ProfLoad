#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from load.models import Posts, Degrees, Professors, Caf, Subject, FormPass, TypeLoad, LoadUnit, Group, Spread

def index(request):
    context = {
    }

    return render(request, 'index.html', context)

def prof(request):
    try:
        lastName = request.POST.get('lastName')
        firstName = request.POST.get('firstName')
        middleName = request.POST.get('middleName')
        degree = Degrees.objects.get(name=request.POST.get('degree'))
        post = Posts.objects.get(name=request.POST.get('post'))
        prof = Professors.objects.create(last_name=lastName, first_name=firstName, middle_name=middleName, post=post, degree=degree)
    except:
       status = "OK"
    professor = Professors.objects.all()
    degrees = Degrees.objects.all()
    posts = Posts.objects.all()
    context = {
        "professors" : professor,
        "degrees" : degrees,
        "posts" : posts,
    }
    return render(request, 'prof.html', context)

def degree(request):
    try:
        new_degree = request.POST.get('degree')
        d = Degrees.objects.create(name=new_degree)
        status = "Запись вставлена"
    except:
        status = "Данная запусь уже существует"
    degrees = Degrees.objects.all()
    context = {
        "degrees" : degrees,
        "status" : status
    }
    return render(request, 'degrees.html', context)

def post(request):
    try:
        new_degree = request.POST.get('post')
        p = Posts.objects.create(name=new_degree)
        status = "Запись вставлена"
    except:
        status = "Данная запись уже существует"
    posts = Posts.objects.all()
    context = {
        "posts" : posts,
        "status" : status
    }
    return render(request, 'posts.html', context)

def caf(request):
    try:
        new_caf = request.POST.get('caf')
        p = Caf.objects.create(name=new_caf)
        status = "Запись вставлена"
    except:
        status = "Данная запись уже существует"
    cafs = Caf.objects.all()
    context = {
        "title" : "Кафедры",
        "items" : cafs,
        "status" : status,
        "url" : "caf",
        "add" : "кафедру"
    }
    return render(request, 'dict.html', context)

def subject(request):
    try:
        new_subject = request.POST.get('subject')
        p = Subject.objects.create(name=new_subject)
        status = "Запись вставлена"
    except:
        status = "Данная запись уже существует"
    cafs = Caf.objects.all()
    context = {
        "title" : "Предметы",
        "items" : subjects,
        "status" : status,
        "url" : "subject",
        "add" : "предмет"
    }
    return render(request, 'dict.html', context)
    
def post(request):
    try:
        new_post = request.POST.get('post')
        p = Posts.objects.create(name=new_post)
        status = "Запись вставлена"
    except:
        status = "Данная запись уже существует"
    poss = Caf.objects.all()
    context = {
        "title" : "Предметы",
        "items" : subjects,
        "status" : status,
        "url" : "subject",
        "add" : "предмет"
    }
    return render(request, 'dict.html', context)

