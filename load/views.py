#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from load.models import Posts, Degrees, Professors, Caf, Subject, FormPass, TypeLoad, LoadUnit, Group, Spread, Subgroup
import codecs
import xlwt


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
    typeLoads = TypeLoad.objects.all().order_by("-sort")
    context = {
        "title" : "Типы нагрузки",
        "items" : typeLoads,
        "status" : status,
        "url" : "typeload",
        "add" : "тип нагрузки",
        "menu" : "subject",
    }
    return render(request, 'typeload.html', context)

def sortload(request):
    try:
        listSort = request.POST.getlist('sort')
        status = listSort
        length = len(listSort)
        if length > 0 :
            for item in listSort:
                typeLoad = TypeLoad.objects.get(name=item);
                typeLoad.sort = length
                length -=1
                typeLoad.save()
                status = "OK"
    except:
        status = "" 

    typeLoads = TypeLoad.objects.all().order_by("-sort")
    context = {
        "items" : typeLoads,
        "menu" : "subject",
        "status" : status,
    }
    return render(request, 'sortload.html', context)

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

def report(request):
    DATA = []
    spreads = Spread.objects.filter(prof__id__gt=0).order_by("prof__last_name")
    groups = Group.objects.all()
    profs = spreads.values('prof').distinct()
    status = profs
    status = []
    for prof in profs:
        cur = {}      

        pr = Professors.objects.get(id=int(prof["prof"]))
        cur["name"] = pr.last_name+" "+pr.first_name+" "+pr.middle_name+", "+pr.post.name+", "+pr.degree.name

        spr = spreads.filter(prof__id=int(prof["prof"]))
        types = spr.values('loadUnit__typeLoad__name').order_by("-loadUnit__typeLoad__sort").distinct()
        cur["spread"] = []
        sum1=0
        sum2=0
        for tp in types:
            sub = spr.filter(loadUnit__typeLoad__name=tp["loadUnit__typeLoad__name"])
            sub1 = []
            sub2 = []
            for spliter in sub:
                if spliter.loadUnit.sem % 2 == 0:
                    sub2.append(spliter)
                else:
                    sub1.append(spliter)
            size = max(len(sub1),len(sub2))
            lines = []
            hourSum1 = 0
            hourSum2 = 0
            for i in range(0, size):
                line = {}
                if i < len(sub1):
                    line["sub1"] = sub1[i].loadUnit.subject.name
                    factor=1
                    if sub1[i].loadUnit.typeLoad.typeTL == "all":
                        gr1=groups.filter(caf=sub1[i].loadUnit.caf,sem=sub1[i].loadUnit.sem,grade=sub1[i].loadUnit.grade)
                    else:
                        gr1=groups.filter(id=sub1[i].group.id)
                        if sub1[i].loadUnit.typeLoad.typeTL == "sub":
                            factor = Subgroup.objects.get(group_id=gr1[0].id).amount

                    line["gr1"] = []
                    for g in gr1:
                        postfix = ""
                        if g.grade == "b":
                            postfix += u'\u0411' # "Б"
                        elif g.grade == "m":
                            postfix += u'\u041c' # "M"
                        if factor > 1:
                            postfix += " ("+str(factor)+")"
                        line["gr1"].append(g.caf.name+"-"+str(g.sem)+str(g.number)+postfix)
                    line["hour1"] = sub1[i].loadUnit.hours*factor
                    hourSum1 += line["hour1"]

                if i < len(sub2):
                    line["sub2"] = sub2[i].loadUnit.subject.name
                    factor=1
                    if sub2[i].loadUnit.typeLoad.typeTL == "all":
                        gr2=groups.filter(caf=sub2[i].loadUnit.caf,sem=sub2[i].loadUnit.sem,grade=sub2[i].loadUnit.grade)
                    else:
                        gr2=groups.filter(id=sub2[i].group.id)
                        if sub2[i].loadUnit.typeLoad.typeTL == "sub":
                            factor = Subgroup.objects.get(group_id=gr2[0].id).amount

                    line["gr2"] = []
                    for g in gr2:
                        postfix = ""
                        if g.grade == "b":
                            postfix += u'\u0411' # "Б"
                        elif g.grade == "m":
                            postfix += u'\u041c' # "M"
                        if factor > 1:
                            postfix += " ("+str(factor)+")"
                        line["gr2"].append(g.caf.name+"-"+str(g.sem)+str(g.number)+postfix)
                    line["hour2"] = sub2[i].loadUnit.hours*factor
                    hourSum2 += line["hour2"]

                lines.append(line)
            cur["spread"].append({"typeload":tp["loadUnit__typeLoad__name"],'subs':lines, 
                "hourSum1": hourSum1, "hourSum2": hourSum2})
            sum1 += hourSum1
            sum2 += hourSum2
        cur["sum1"] = sum1
        cur["sum2"] = sum2
        DATA.append(cur)

    context = {
        "spreads" : spreads,
        "data" : DATA,
        "status" : status,
        "menu" : "report"
    }

    # save into xls

    style_full = style_antibottom = style_antitop = style_top = style_bottom = style_left = style_right = style_topleft = style_topright = style_bottomleft = style_bottomright = style_clear = xlwt.easyxf('font: name Times New Roman, color-index black, bold on', num_format_str='#,##0.00')
    style_red = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')

    borders_full = xlwt.Borders()
    borders_full.bottom = borders_full.top = borders_full.left = borders_full.right = xlwt.Borders.MEDIUM
    style_full.borders = style_red = borders_full

    borders_top = xlwt.Borders()
    borders_top.top = xlwt.Borders.MEDIUM
    style_top.borders = borders_top

    borders_bottom = xlwt.Borders()
    borders_bottom.bottom = xlwt.Borders.MEDIUM
    style_bottom.borders = borders_bottom
    
    borders_left = xlwt.Borders()
    borders_left.left = xlwt.Borders.MEDIUM
    style_left.left = borders_left
    
    borders_right = xlwt.Borders()
    borders_right.top = xlwt.Borders.MEDIUM
    style_right.borders = borders_right
    
    borders_topleft = xlwt.Borders()
    borders_topleft.top = borders_topleft.left = xlwt.Borders.MEDIUM
    style_topleft.borders = borders_topleft

    borders_topright = xlwt.Borders()
    borders_topright.top = borders_topright.right = xlwt.Borders.MEDIUM
    style_topright.borders = borders_topright

    borders_bottomleft = xlwt.Borders()
    borders_bottomleft.top = borders_bottomleft.left = xlwt.Borders.MEDIUM
    style_bottomleft.borders = borders_bottomleft

    borders_bottomright = xlwt.Borders()
    borders_bottomright.top = borders_bottomright.right = xlwt.Borders.MEDIUM
    style_bottomright.borders = borders_bottomright

    borders_antibottom = xlwt.Borders()
    borders_antibottom.top = borders_antibottom.left = borders_antibottom.right = xlwt.Borders.MEDIUM
    style_antibottom.borders = borders_antibottom

    borders_antitop = xlwt.Borders()
    borders_antitop.bottom = borders_antitop.left = borders_antitop.right = xlwt.Borders.MEDIUM
    style_antitop.borders = borders_antitop

    wb = xlwt.Workbook()
    ws = wb.add_sheet('Load')

    ws.col(0).width = 100*30
    ws.col(1).width = 120*30
    ws.col(2).width = 80*30
    ws.col(3).width = 60*30
    ws.col(4).width = 120*30
    ws.col(5).width = 80*30
    ws.col(6).width = 60*30
    ws.col(7).width = 60*30

    y = 0
    for obj in DATA:
        ws.write_merge(y, y, 0, 7, obj["name"], style=style_full)
        ws.write_merge(y+1, y+2, 0, 0, u"Нагрузка",style=style_full)
        ws.write_merge(y+1, y+1, 1, 3, u"Осенний семестр",style=style_antibottom)
        ws.write_merge(y+1, y+1, 4, 6, u"Весенний семестр",style=style_antibottom)
        ws.write_merge(y+1, y+2, 7, 7, u"Итого:",style=style_full)
        ws.write(y+2, 1, u"Предмет",style=style_bottomleft)
        ws.write(y+2, 2, u"Группы",style=style_bottom)
        ws.write(y+2, 3, u"Часы",style=style_bottomright)
        ws.write(y+2, 4, u"Предмет",style=style_bottomleft)
        ws.write(y+2, 5, u"Группы",style=style_bottom)
        ws.write(y+2, 6, u"Часы",style=style_bottomright)
        y += 3

        for spr in obj["spread"]:
            ws.write_merge(y, y+len(spr["subs"]), 0, 0, spr["typeload"],style=style_full)
            ws.write_merge(y, y-1+len(spr["subs"]), 7,7, "",style=style_full)
            for sub in spr["subs"]:
                if "sub1" in sub:
                    ws.write(y, 1, sub["sub1"] ,style=style_topleft)
                    ws.write(y, 2, sub["gr1"],style=style_top)
                    ws.write(y, 3, sub["hour1"],style=style_topright)
                else:
                    ws.write(y, 1, "",style=style_topleft)
                    ws.write(y, 2, "",style=style_top)
                    ws.write(y, 3, "",style=style_topright)
                if "sub2" in sub:
                    ws.write(y, 4, sub["sub2"],style=style_topleft)
                    ws.write(y, 5, sub["gr2"],style=style_top)
                    ws.write(y, 6, sub["hour2"],style=style_topright)
                else:
                    ws.write(y, 4, "",style=style_topleft)
                    ws.write(y, 5, "",style=style_top)
                    ws.write(y, 6, "",style=style_topright)
                y += 1   
            ws.write_merge(y, y, 1, 2, u"Итого",style=style_topleft)
            ws.write(y, 3, spr["hourSum1"],style=style_topright)
            ws.write_merge(y, y, 4, 5, u"Итого",style=style_topleft)
            ws.write(y, 6, spr["hourSum2"],style=style_topright)
            ws.write(y, 7, spr["hourSum2"] + spr["hourSum1"],style=style_topright)
            y += 1
        ws.write(y, 0, "",style=style_topleft)
        ws.write_merge(y, y, 1, 2, u"Итого за осенний семестр",style=style_topleft)
        ws.write(y, 3, obj["sum1"],style=style_topright)
        ws.write_merge(y, y, 4, 5, u"Итого за весенний семестр",style=style_topleft)
        ws.write(y, 6, obj["sum2"],style=style_topright)
        ws.write(y, 7, obj["sum2"]+obj["sum1"],style=style_topright)
        y += 3

    wb.save('static/report.xls')
    return render(request, 'report.html', context)