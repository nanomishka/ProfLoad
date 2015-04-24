#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from load.models import Posts, Degrees, Professors, Caf, Subject, FormPass, TypeLoad, LoadUnit, Group, Spread, Subgroup
import codecs


def index(request):
    # delete spread
    try:
        removeId = request.GET.get('remove')
        Spread.objects.get(id=int(removeId)).delete()
    except:
        status = "Данная запись не существует"
    # remove professor
    try:
        clearId = request.GET.get('clear')
        spread = Spread.objects.get(id=int(clearId))
        spread.prof = None
        spread.save()
    except:
        status = "Данная запись не существует"
    # push professors
    try:
        prof = Professors.objects.get(id=int(request.POST.get('prof')))
        spreads = request.POST.getlist('spread')
        for s in spreads:
            spread = Spread.objects.get(id=int(s))
            spread.prof = prof
            spread.save()
    except:
       status = "OK"
    # split group
    try:
        group = int(request.POST.get('idGroup'))
        amount = int(request.POST.get('number'))
        Subgroup.objects.create(group=Group.objects.get(id=group), amount=amount)
    except:
       status = "OK"

    spreads = Spread.objects.all().order_by('loadUnit','group')
    groups = Group.objects.all()
    subgroups = Subgroup.objects.all()
    listSubGrps = []
    for sub in subgroups:
        listSubGrps.append(sub.group)

    profs = Professors.objects.all()
    hours = []
    for prof in profs:
        listSpread = Spread.objects.filter(prof=prof)
        time = 0
        for spr in listSpread:
            t = int(spr.loadUnit.hours)
            if spr.loadUnit.typeLoad.typeTL == "sub":
                t *= int(Subgroup.objects.get(group=spr.group).amount)
            time += t
        hours.append([prof.id,time])
    context = {
        "spreads" : spreads,
        "profs" : profs,
        "status" : status,
        "groups" : groups,
        "subgroups" : subgroups,
        "listSubGrps" : listSubGrps,
        "hours" : hours,
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
        status = "OK"
    except:
        status = "Данная запись не существует"

    try:
        new_subject = request.POST.get('attr')
        if new_subject:
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
        typeTL = request.POST.get('type')
        typeload = TypeLoad.objects.create(name=new_typeLoad, typeTL=typeTL)
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
    return render(request, 'typeload.html', context)

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

def subgroup(request):

    try:
        ID = int(request.POST.get('idSubgroup'))
        status = ID
        amount = int(request.POST.get('number'))
        subgroup = Subgroup.objects.get(id=ID)
        subgroup.amount = amount
        subgroup.save()
    except:
       status = "OK"

    subgroups = Subgroup.objects.all()
    context = {
        "subgroups" : subgroups,
        "status" : status,
        "menu" : "group",
    }
    return render(request, 'subgroup.html', context)

def loadUnit(request):

    try:
        removeId = request.GET.get('remove')
        LoadUnit.objects.get(id=int(removeId)).delete()
    except:
        status = "Данная запись не существует"
    # add new loadunits and spreads
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
                TP = typeLoad.get(id=t)
                loadUnit = LoadUnit.objects.create(subject=subject, caf=caf, formPass=formPass, sem=sem, typeLoad=TP, hours=hours, grade = grade)
                if TP.typeTL != "all":
                    groups = Group.objects.all().filter(caf=caf, sem=sem, grade = grade)
                    for gr in groups:
                        Spread.objects.create(loadUnit=loadUnit, group=gr)
                else:
                    Spread.objects.create(loadUnit=loadUnit)
    except:
            status = "error"

    # split loadunit
    try:
        split = request.POST.get('number')
        status = request.POST.get('idLoad')
        idLoad = int(request.POST.get('idLoad'))
        load = LoadUnit.objects.get(id=idLoad)
        status = split
        for s in range(0, int(split)):
            amount = int(request.POST.get('hours'+str(s)))
            if amount != 0:
                if s != 0:
                    loadUnit = LoadUnit.objects.create(subject=load.subject, caf=load.caf, formPass=load.formPass, sem=load.sem, typeLoad=load.typeLoad, hours=amount, grade=load.grade)
                    groups = Group.objects.all().filter(caf=load.caf, sem=load.sem, grade=load.grade)
                    for gr in groups:
                        Spread.objects.create(loadUnit=loadUnit, group=gr)
                else:
                    load.hours = amount
                    load.save()
    except:
        status = "Данная запись не существует"


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
        "groups" : groups,
        "semesters" : semesters,
        "formPasss" : formPasss,
        "typeLoads" : typeLoads,
        "menu" : "subject",
        "status" : status,
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