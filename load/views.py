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
        removeId = request.GET.get('remove')
        Professors.objects.get(id=int(removeId)).delete()
    except:
        status = "Данная запись не существует"

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

def caf(request):

    try:
        removeId = request.GET.get('remove')
        Caf.objects.get(id=int(removeId)).delete()
    except:
        status = "Данная запись не существует" 

    try:
        new_caf = request.POST.get('attr')
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
        removeId = request.GET.get('remove')
        Subject.objects.get(id=int(removeId)).delete()
    except:
        status = "Данная запись не существует"

    try:
        new_subject = request.POST.get('attr')
        p = Subject.objects.create(name=new_subject)
        status = "Запись вставлена"
    except:
        status = "Данная запись уже существует"
    subjects = Subject.objects.all()
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
        removeId = request.GET.get('remove')
        Posts.objects.get(id=int(removeId)).delete()
    except:
        status = "Данная запись не существует"

    try:
        new_post = request.POST.get('attr')
        post = Posts.objects.create(name=new_post)
        status = "Запись вставлена"
    except:
        status = "Данная запись уже существует"
    posts = Posts.objects.all()
    context = {
        "title" : "Должности преподавателя",
        "items" : posts,
        "status" : status,
        "url" : "post",
        "add" : "должность"
    }
    return render(request, 'dict.html', context)

def degree(request):

    try:
        removeId = request.GET.get('remove')
        Degrees.objects.get(id=int(removeId)).delete()
    except:
        status = "Данная запись не существует"

    try:
        new_degree = request.POST.get('attr')
        degree = Degrees.objects.create(name=new_degree)
        status = "Запись вставлена"
    except:
        status = "Данная запись уже существует"
    degrees = Degrees.objects.all()
    context = {
        "title" : "Степени преподавателя",
        "items" : degrees,
        "status" : status,
        "url" : "degree",
        "add" : "степень"
    }
    return render(request, 'dict.html', context)

def formpass(request):
    try:
        removeId = request.GET.get('remove')
        FormPass.objects.get(id=int(removeId)).delete()
    except:
        status = "Данная запись не существует" 


    try:
        new_formPass = request.POST.get('attr')
        formpass = FormPass.objects.create(name=new_formPass)
        status = "Запись вставлена"
    except:
        status = "Данная запись уже существует"
    formPasss = FormPass.objects.all()
    context = {
        "title" : "Формы сдачи предмета",
        "items" : formPasss,
        "status" : status,
        "url" : "formpass",
        "add" : "форму сдачи предмета"
    }
    return render(request, 'dict.html', context)

def typeload(request):
    try:
        removeId = request.GET.get('remove')
        TypeLoad.objects.get(id=int(removeId)).delete()
    except:
        status = "Данная запись не существует" 

    try:
        new_typeLoad = request.POST.get('attr')
        typeload = TypeLoad.objects.create(name=new_typeLoad)
        status = "Запись вставлена"
    except:
        status = "Данная запись уже существует"
    typeLoads = TypeLoad.objects.all()
    context = {
        "title" : "Типы нагрузки",
        "items" : typeLoads,
        "status" : status,
        "url" : "typeload",
        "add" : "тип нагрузки"
    }
    return render(request, 'dict.html', context)

def group(request):

    try:
        removeId = request.GET.get('remove')
        Group.objects.get(id=int(removeId)).delete()
    except:
        status = "Данная запись не существует"

    try:
        caf = Caf.objects.get(name=request.POST.get('caf'))
        sem = request.POST.get('sem')
        number = request.POST.get('number')
        group = Group.objects.create(caf=caf, sem=sem, number=number)
        status = "Запись вставлена"
    except:
        status = "Данная запись уже существует"

    groups = Group.objects.all()
    cafs = Caf.objects.all()
    context = {
        "groups" : groups,
        "status" : status,
        "cafs" : cafs
    }
    return render(request, 'group.html', context)

def loadUnit(request):

    try:
        removeId = request.GET.get('remove')
        LoadUnit.objects.get(id=int(removeId)).delete()
    except:
        status = "Данная запись не существует"

    try:
        subject = Subject.objects.get(name=request.POST.get('subject'))
        caf = Caf.objects.get(name=request.POST.get('caf'))
        formPass = FormPass.objects.get(name=request.POST.get('formPass'))
        sem = int(request.POST.get('sem'))
        typeLoad = TypeLoad.objects.get(name=request.POST.get('typeLoad'))
        hours = int(request.POST.get('hours'))
        loadUnit = LoadUnit.objects.create(subject=subject, caf=caf, formPass=formPass, sem=sem, typeLoad=typeLoad, hours=hours)
    except:
       status = "OK"
    loadUnits = LoadUnit.objects.all().order_by('subject')
    subjects = Subject.objects.all()
    cafs = Caf.objects.all()
    formPasss = FormPass.objects.all()
    typeLoads = TypeLoad.objects.all()
    context = {
        "loadUnits" : loadUnits,
        "subjects" : subjects,
        "cafs" : cafs,
        "formPasss" : formPasss,
        "typeLoads" : typeLoads,
    }
    return render(request, 'loadunit.html', context)

def spread(request):
    try:
        loadUnit = LoadUnit.objects.get(name=request.POST.get('loadUnit'))
        prof = Professors.objects.get(name=request.POST.get('prof'))
        group = Group.objects.get(name=request.POST.get('group'))
        spread = Spread.objects.create(loadUnit=loadUnit, prof=prof, group=group)
    except:
       status = "OK"
    spread = Spread.objects.all()
    loadUnit = LoadUnit.objects.all()
    prof = Professors.objects.all()
    caf = Caf.objects.all()
    context = {
        "loadUnit" : loadUnit,
        "subject" : subject,
        "caf" : caf,
        "formPasss" : formPass,
        "sem" : sem,
        "typeLoad" : typeLoad,
        "hours" : hours,
    }
    return render(request, 'spread.html', context)