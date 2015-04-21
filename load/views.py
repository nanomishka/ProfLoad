#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from load.models import Posts, Degrees, Professors, Caf, Subject, FormPass, TypeLoad, LoadUnit, Group, Spread
import codecs


def index(request):
    try:
        removeId = request.GET.get('remove')
        Spread.objects.get(id=int(removeId)).delete()
    except:
        status = "Данная запись не существует"

    try:
        clearId = request.GET.get('clear')
        spread = Spread.objects.get(id=int(clearId))
        spread.prof = None
        spread.save()
    except:
        status = "Данная запись не существует"

    try:
        prof = Professors.objects.get(id=int(request.POST.get('prof')))
        status = []
        spreads = request.POST.getlist('spread')
        for s in spreads:
            status.append(s)
            spread = Spread.objects.get(id=int(s))
            spread.prof = prof
            spread.save()
    except:
       status = "OK"
    spreads = Spread.objects.all()
    profs = Professors.objects.all() 
    context = {
        "spreads" : spreads,
        "profs" : profs,
        "status" : status,
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
        "menu" : "prof",   
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
        "add" : "кафедру",
        "menu" : "group",
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
        "add" : "предмет",
        "menu" : "subject",
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
        "add" : "должность",
        "menu" : "prof",
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
        "add" : "степень",
        "menu" : "prof",
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
        "add" : "форму сдачи предмета",
        "menu" : "subject"
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
        "add" : "тип нагрузки",
        "menu" : "subject",
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
        grade = request.POST.get('grade')
        for g in range(0, int(number)):
            grNumber = request.POST.get('grNumber'+str(g))
            grAmount = request.POST.get('grAmount'+str(g))
            group = Group.objects.create(caf=caf, sem=sem, number=grNumber, amount=grAmount, grade=grade)
        status = "Запись вставлена"
    except:
        status = "Данная запись уже существует"

    groups = Group.objects.all()
    cafs = Caf.objects.all()
    context = {
        "groups" : groups,
        "status" : status,
        "cafs" : cafs,
        "menu" : "group",
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
        sem = int(request.POST.get('sem').split("_", 1)[0])
        grade = request.POST.get('sem').split("_", 1)[1]
        typeLoad = TypeLoad.objects.all()
        for t in range(typeLoad.order_by("id")[0].id, typeLoad.order_by("-id")[0].id+1):
            hours = int(request.POST.get('load'+str(t), 0))
            if hours != 0:
                loadUnit = LoadUnit.objects.create(subject=subject, caf=caf, formPass=formPass, sem=sem, typeLoad=typeLoad.get(id=t), hours=hours)
                groups = Group.objects.all().filter(caf=caf, sem=sem, grade = grade)
                for gr in groups:
                    Spread.objects.create(loadUnit=loadUnit, group=gr)
    except:
            status = "error"

    loadUnits = LoadUnit.objects.all().order_by('subject')
    subjects = Subject.objects.all()
    cafs = Caf.objects.all()

    groups = Group.objects.all()
    sem_caf = groups.order_by("caf").values("caf__name").distinct()
    semesters = []
    sem_sem = groups.values("caf__name","sem","grade").distinct()
    for sem in sem_sem:
        count = groups.filter(caf__name=sem['caf__name'],sem=sem['sem'],grade=sem['grade']).count()
        semesters.append({'caf':sem['caf__name'],'sem':sem['sem'], 'grade':sem["grade"], 'count': count })

    formPasss = FormPass.objects.all()
    typeLoads = TypeLoad.objects.all()
    context = {
        "loadUnits" : loadUnits,
        "subjects" : subjects,
        "cafs" : cafs,
        "semesters" : semesters,
        "formPasss" : formPasss,
        "typeLoads" : typeLoads,
        "menu" : "subject",
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
    profs = Professors.objects.all() 
    context = {
        "spreads" : spreads,
        "profs" : profs,
    }
    return render(request, 'spread.html', context)