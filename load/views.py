#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from load.models import *
import xlwt
from namePaginator import NamePaginator


def index(request,  page):
    page = page or 1
    page = int(page)
    pag_limit = 30

    # delete spread
    try:
        removeId = request.GET.get('remove')
        Spread.objects.get(id=int(removeId)).delete()
    except:
        status = 'Данная запись не существует'
    # remove professor
    try:
        clearId = request.GET.get('clear')
        spread = Spread.objects.get(id=int(clearId))
        spread.prof = None
        spread.save()
    except:
        status = 'Данная запись не существует'
    # push professors
    try:
        prof = Professors.objects.get(id=int(request.POST.get('prof')))
        spreads = request.POST.getlist('spread')
        for s in spreads:
            spread = Spread.objects.get(id=int(s))
            spread.prof = prof
            spread.save()
    except:
       status = 'OK'
    # split group
    try:
        group = int(request.POST.get('idGroup'))
        amount = int(request.POST.get('number'))
        Subgroup.objects.create(group=Group.objects.get(id=group), amount=amount)
    except:
       status = 'OK'
    # edit hours
    try:
        editId = request.GET.get('editId')
        hours = int(request.GET.get('hours'))
        loadUnit = Spread.objects.get(id=int(editId))
        loadUnit.hours = hours
        loadUnit.save()
    except:
        status = 'Данная запись не существует'

    # split spread
    try:
        split = request.POST.get('number')
        idSpread = int(request.POST.get('idSpread'))
        spread = Spread.objects.get(id=idSpread)
        for s in range(0, int(split)):
            amount = int(request.POST.get('hours'+str(s)))
            if amount != 0:
                if s != 0:
                    Spread.objects.create(loadUnit=spread.loadUnit, group=spread.group, hours=amount)
                else:
                    if spread.hours != amount:
                        spread.hours = amount
                        spread.save()
                    else:
                        break
    except:
        status = 'Данная запись не существует'

    spreads = Spread.objects.all().order_by('loadUnit__subject__name', '-loadUnit__typeLoad__sort', 'group')
    try:
        sort = request.GET.get('sort')
        if sort == 'prof':
            spreads = Spread.objects.all().order_by('prof__last_name', 'loadUnit__subject__name', '-loadUnit__typeLoad__sort', 'group')
    except:
        spreads = {}
    

    groups = Group.objects.all()
    subgroups = Subgroup.objects.all()
    listSubGrps = []
    for sub in subgroups:
        listSubGrps.append(sub.group)

    profs = Professors.objects.all().order_by('last_name')
    hours = []
    for prof in profs:
        listSpread = Spread.objects.filter(prof=prof)
        time = 0
        for spr in listSpread:
            t = int(spr.hours)
            if spr.loadUnit.typeLoad.typeTL == 'sub':
                t *= int(Subgroup.objects.get(group=spr.group).amount)
            time += t
        hours.append([prof.id, time])

    report_flag = False
    if request.GET.get('report', ''):
        style_bold = xlwt.easyxf('font: name Times New Roman, color-index black, bold on', num_format_str='#,##0')
        wb1 = xlwt.Workbook()
        ws1 = wb1.add_sheet('Load')

        ws1.col(0).width = 200*30
        ws1.col(1).width = 100*30
        ws1.col(2).width = 70*30
        ws1.col(3).width = 100*30
        ws1.col(4).width = 60*30
        ws1.col(5).width = 150*30

        DATA = [0, 1]

        ws1.write(0, 0, u'Предмет',style=style_bold)
        ws1.write(0, 1, u'Группа',style=style_bold)
        ws1.write(0, 2, u'Семестр',style=style_bold)
        ws1.write(0, 3, u'Вид нагрузки',style=style_bold)
        ws1.write(0, 4, u'Часы',style=style_bold)
        ws1.write(0, 5, u'Преподаватель',style=style_bold)

        y = 1
        for spread in spreads:
            #Запись данных в таблицу
            ws1.write(y, 0, spread.loadUnit.subject.name,style=style_bold)

            if spread.group:
                string = ' '
                if spread.group.grade == 'b':
                    string = string + u'\u0411'
                elif spread.group.grade == 'm':
                    string = string + u'\u041c'
                if spread.loadUnit.typeLoad.typeTL == 'sub':
                        if spread.group not in listSubGrps:
                            string = string + '(?)'
                        else:
                            for sub in subgroups:
                                if sub.group == spread.group:
                                    string = string + '(' + str(sub.amount) + ')'
                ws1.write(y, 1, spread.group.caf.name + '-' + str(spread.group.sem) + str(spread.group.number) + string,style=style_bold)
            else:
                grps = groups.filter( caf=spread.loadUnit.caf, sem = spread.loadUnit.sem)
                string = ''
                i = 0
                for gr in grps:
                    if i != 0:
                        string = string + '\n'
                    i = 1
                    string = string + gr.caf.name + '-' + str(gr.sem) + str(gr.number) + ' '
                    if gr.grade == 'b':
                        string = string + u'\u0411'
                    elif gr.grade == 'm':
                        string = string + u'\u041c'
                ws1.write(y, 1, string, style=style_bold)
            ws1.write(y, 2, spread.loadUnit.sem, style=style_bold)
            ws1.write(y, 3, spread.loadUnit.typeLoad.name, style=style_bold)
            if spread.loadUnit.typeLoad.typeTL != 'sub':
                ws1.write(y, 4, spread.hours,style=style_bold)
            else:
                if spread.group in listSubGrps:
                    for sub in subgroups:
                        if sub.group == spread.group:
                            ws1.write(y, 4, spread.hours * sub.amount ,style=style_bold)
                            break
            if spread.prof:
                ws1.write(y, 5, spread.prof.last_name,style=style_bold)
            y = y + 1

        wb1.save('static/report_subjects.xls')
        report_flag = True

    pag_data = {'pages': None, 'counter': {'page': page, 'start_val': 0}}
    if page:
        paginator = Paginator(spreads, pag_limit)
        spreads = paginator.page(int(page))

        pag_data['pages'] = paginator.page_range
        pag_data['counter'] = {'page': page, 'start_val': pag_limit * (page - 1)}


    context = {
        'spreads': spreads,
        'profs': profs,
        'status': status,
        'groups': groups,
        'subgroups': subgroups,
        'listSubGrps': listSubGrps,
        'hours': hours,
        'pages': pag_data['pages'],
        'counter': pag_data['counter'],
        'report_flag': report_flag
    }

    return render(request, 'index.html', context)


def prof(request, page):
    page = int(page)

    try:
        removeId = request.GET.get('remove')
        Professors.objects.get(id=int(removeId)).delete()
    except:
        pass

    try:
        lastName = request.POST.get('lastName')
        firstName = request.POST.get('firstName')
        middleName = request.POST.get('middleName')
        degree = Degrees.objects.get(name=request.POST.get('degree'))
        post = Posts.objects.get(name=request.POST.get('post'))
        Professors.objects.create(last_name=lastName, first_name=firstName,
                                  middle_name=middleName, post=post, degree=degree)
    except:
       pass

    pages = []
    counter = 0
    if page:
        paginator = NamePaginator(Professors.objects.all(), on='last_name', per_page=8)
        professors = paginator.page(page).get_object_list()

        for i in range(len(paginator.pages)):
            p = paginator.pages[i]
            if len(p.letters) == 1:
                pages.append(p.letters[0])
            else:
                pages.append('%s - %s' % (p.letters[0],  p.letters[-1],))
            if i + 1 < page:
                counter += len(paginator.page(i+1).get_object_list())
    else:
        professors = Professors.objects.order_by('last_name')

    degrees = Degrees.objects.all()
    posts = Posts.objects.all()

    hours = []
    for professor in professors:
        list_spread = Spread.objects.filter(prof=professor)
        time = 0
        for spr in list_spread:
            t = int(spr.hours)
            if spr.loadUnit.typeLoad.typeTL == 'sub':
                t *= int(Subgroup.objects.get(group=spr.group).amount)
            time += t
        hours.append([professor.id, time])

    context = {
        'professors': professors,
        'degrees': degrees,
        'posts': posts,
        'menu': 'prof',
        'sub_menu': 'prof',
        'hours': hours,
        'pages': pages,
        'counter': {'page': page, 'start_val': counter}
    }

    return render(request, 'prof.html', context)


def caf(request):

    try:
        removeId = request.GET.get('remove')
        Caf.objects.get(id=int(removeId)).delete()
    except:
        status = 'Данная запись не существует' 

    try:
        new_caf = request.POST.get('attr')
        p = Caf.objects.create(name=new_caf)
        status = 'Запись вставлена'
    except:
        status = 'Данная запись уже существует'
    cafs = Caf.objects.all()
    context = {
        'title': 'Кафедры',
        'items': cafs,
        'status': status,
        'url': 'caf',
        'add': 'кафедру',
        'menu': 'group',
        'sub_menu': 'caf'
    }

    return render(request, 'dict.html', context)


def subject(request, page):
    page = int(page)

    try:
        removeId = request.GET.get('remove')
        Subject.objects.get(id=int(removeId)).delete()
        status = 'OK'
    except:
        status = 'Данная запись не существует'

    try:
        new_subject = request.POST.get('attr')
        if new_subject:
            p = Subject.objects.create(name=new_subject)
            status = 'Запись вставлена'
    except:
        status = 'Данная запись уже существует'

    subjects = Subject.objects.all()

    pag_data = {'pages': [], 'counter': {'page': page, 'start_val': 0}}
    if page:
        paginator = NamePaginator(subjects, on='name', per_page=8)
        subjects = paginator.page(page).get_object_list()

        for i in range(len(paginator.pages)):
            p = paginator.pages[i]
            if len(p.letters) == 1:
                pag_data['pages'].append(p.letters[0])
            else:
                pag_data['pages'].append('%s - %s' % (p.letters[0],  p.letters[-1],))
            if i + 1 < page:
                pag_data['counter']['start_val'] += len(paginator.page(i+1).get_object_list())

    context = {
        'title': 'Предметы',
        'items': subjects,
        'status': status,
        'url': 'subject',
        'add': 'предмет',
        'menu': 'subject',
        'sub_menu': 'subject',
        'pages': pag_data['pages'],
        'counter': pag_data['counter']
    }
    return render(request, 'subject.html', context)


def post(request):

    try:
        removeId = request.GET.get('remove')
        Posts.objects.get(id=int(removeId)).delete()
    except:
        status = 'Данная запись не существует'

    try:
        new_post = request.POST.get('attr')
        post = Posts.objects.create(name=new_post)
        status = 'Запись вставлена'
    except:
        status = 'Данная запись уже существует'
    posts = Posts.objects.all()
    context = {
        'title': 'Должности преподавателя',
        'items': posts,
        'status': status,
        'url': 'post',
        'add': 'должность',
        'menu': 'prof',
        'sub_menu': 'post',
    }
    return render(request, 'dict.html', context)


def degree(request):

    try:
        removeId = request.GET.get('remove')
        Degrees.objects.get(id=int(removeId)).delete()
    except:
        status = 'Данная запись не существует'

    try:
        new_degree = request.POST.get('attr')
        degree = Degrees.objects.create(name=new_degree)
        status = 'Запись вставлена'
    except:
        status = 'Данная запись уже существует'
    degrees = Degrees.objects.all()
    context = {
        'title' : 'Степени преподавателя',
        'items' : degrees,
        'status' : status,
        'url' : 'degree',
        'add' : 'степень',
        'menu': 'prof',
        'sub_menu': 'degree',
    }
    return render(request, 'dict.html', context)


def formpass(request):
    try:
        removeId = request.GET.get('remove')
        FormPass.objects.get(id=int(removeId)).delete()
    except:
        status = 'Данная запись не существует' 


    try:
        new_formPass = request.POST.get('attr')
        formpass = FormPass.objects.create(name=new_formPass)
        status = 'Запись вставлена'
    except:
        status = 'Данная запись уже существует'
    formPasss = FormPass.objects.all()
    context = {
        'title': 'Формы сдачи предмета',
        'items': formPasss,
        'status': status,
        'url': 'formpass',
        'add': 'форму сдачи предмета',
        'menu': 'subject',
        'sub_menu': 'formpass',
    }
    return render(request, 'dict.html', context)


def typeload(request):
    try:
        removeId = request.GET.get('remove')
        TypeLoad.objects.get(id=int(removeId)).delete()
    except:
        status = 'Данная запись не существует' 

    try:
        new_typeLoad = request.POST.get('attr')
        typeTL = request.POST.get('type')
        typeload = TypeLoad.objects.create(name=new_typeLoad, typeTL=typeTL)
        status = 'Запись вставлена'
    except:
        status = 'Данная запись уже существует'
    typeLoads = TypeLoad.objects.all().order_by('-sort')
    context = {
        'title': 'Типы нагрузки',
        'items': typeLoads,
        'status': status,
        'url': 'typeload',
        'add': 'тип нагрузки',
        'menu': 'subject',
        'sub_menu': 'typeload',
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
                status = 'OK'
    except:
        status = '' 

    typeLoads = TypeLoad.objects.all().order_by('-sort')

    context = {
        'items': typeLoads,
        'menu': 'subject',
        'sub_menu': 'sortload',
        'status': status,
    }
    return render(request, 'sortload.html', context)


def group(request, page):
    page = int(page)
    pag_limit = 8

    try:
        removeId = request.GET.get('remove')
        Group.objects.get(id=int(removeId)).delete()
    except:
        status = 'Данная запись не существует'

    try:
        caf = Caf.objects.get(name=request.POST.get('caf'))
        sem = request.POST.get('sem')
        number = request.POST.get('number')
        grade = request.POST.get('grade')
        for g in range(0, int(number)):
            grNumber = request.POST.get('grNumber'+str(g))
            grAmount = request.POST.get('grAmount'+str(g))
            Group.objects.create(caf=caf, sem=sem, number=grNumber, amount=grAmount, grade=grade)
        status = 'Запись вставлена'
    except:
        status = 'Данная запись уже существует'

    groups = Group.objects.all()
    cafs = Caf.objects.all()
    pag_data = {'pages': None, 'counter': {'page': page, 'start_val': 0}}
    if page:
        paginator = Paginator(groups, pag_limit)
        groups = paginator.page(int(page))

        pag_data['pages'] = paginator.page_range
        pag_data['counter'] = {'page': page, 'start_val': pag_limit * (page - 1)}

    context = {
        'groups': groups,
        'status': status,
        'cafs': cafs,
        'menu': 'group',
        'sub_menu': 'group',
        'pages': pag_data['pages'],
        'counter': pag_data['counter']
    }
    return render(request, 'group.html', context)


def subgroup(request, page):
    page = int(page)
    pag_limit = 6

    try:
        ID = int(request.POST.get('idSubgroup'))
        status = ID
        amount = int(request.POST.get('number'))
        subgroup = Subgroup.objects.get(id=ID)
        subgroup.amount = amount
        subgroup.save()
    except:
       status = 'OK'

    subgroups = Subgroup.objects.all()
    pag_data = {'pages': None, 'counter': {'page': page, 'start_val': 0}}
    if page:
        paginator = Paginator(subgroups, pag_limit)
        subgroups = paginator.page(int(page))

        pag_data['pages'] = paginator.page_range
        pag_data['counter'] = {'page': page, 'start_val': pag_limit * (page - 1)}

    context = {
        'subgroups': subgroups,
        'status': status,
        'menu': 'group',
        'sub_menu': 'subgroup',
        'pages': pag_data['pages'],
        'counter': pag_data['counter']
    }
    return render(request, 'subgroup.html', context)


def loadUnit(request, page):
    page = int(page)
    pag_limit = 25

    try:
        removeId = request.GET.get('remove')
        LoadUnit.objects.get(id=int(removeId)).delete()
    except:
        status = 'Данная запись не существует'
    # add new loadunits and spreads
    try:
        subject = Subject.objects.get(name=request.POST.get('subject'))
        caf = Caf.objects.get(name=request.POST.get('caf'))
        formPass = FormPass.objects.get(name=request.POST.get('formPass'))
        sem = int(request.POST.get('sem').split('_', 1)[0])
        grade = request.POST.get('sem').split('_', 1)[1]
        method = request.POST.get('method')
        typeLoad = TypeLoad.objects.all()
        
        for t in range(typeLoad.order_by('id')[0].id, typeLoad.order_by('-id')[0].id+1):
            hours = int(request.POST.get('load'+str(t), 0))
            if hours != 0:
                if method == 'create':
                    TP = typeLoad.get(id=t)
                    loadUnit = LoadUnit.objects.create(subject=subject, caf=caf, formPass=formPass, sem=sem, typeLoad=TP, hours=hours, grade = grade)
                    if TP.typeTL != 'all':
                        groups = Group.objects.all().filter(caf=caf, sem=sem, grade = grade)
                        for gr in groups:
                            Spread.objects.create(loadUnit=loadUnit, group=gr, hours=hours)
                    else:
                        Spread.objects.create(loadUnit=loadUnit, hours=hours)
                elif method == 'edit':
                    loadUnit = LoadUnit.objects.get(id=int(request.POST.get('spreadId')))
                    loadUnit.subject = subject
                    loadUnit.hours = hours
                    loadUnit.formPass = formPass
                    loadUnit.caf = caf
                    loadUnit.sem = sem
                    loadUnit.grade = grade
                    loadUnit.save()
    except:
            status = 'error'

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
                        Spread.objects.create(loadUnit=loadUnit, group=gr, hours = amount)
                else:
                    load.hours = amount
                    load.save()
                    spreads = Spread.objects.all().filter(loadUnit=load)
                    for spread in spreads:
                        spread.hours = amount
                        spread.save()
    except:
        status = 'Данная запись не существует'


    loadUnits = LoadUnit.objects.all().order_by('subject__name')
    pag_data = {'pages': None, 'counter': {'page': page, 'start_val': 0}}
    if page:
        paginator = Paginator(loadUnits, pag_limit)
        loadUnits = paginator.page(int(page))

        pag_data['pages'] = paginator.page_range
        pag_data['counter'] = {'page': page, 'start_val': pag_limit * (page - 1)}

    cafs = Caf.objects.all()
    subjects = Subject.objects.all()
    groups = Group.objects.all()
    semesters = []
    sem_sem = groups.values('caf__name', 'sem', 'grade').distinct()
    for sem in sem_sem:
        count = groups.filter(caf__name=sem['caf__name'], sem=sem['sem'], grade=sem['grade']).count()
        semesters.append({'caf': sem['caf__name'], 'sem': sem['sem'], 'grade': sem['grade'], 'count': count})

    formPasss = FormPass.objects.all()
    typeLoads = TypeLoad.objects.all().order_by('-sort')
    context = {
        'loadUnits': loadUnits,
        'subjects': subjects,
        'cafs': cafs,
        'groups': groups,
        'semesters': semesters,
        'formPasss': formPasss,
        'typeLoads': typeLoads,
        'menu': 'subject',
        'status': status,
        'sub_menu': 'loadunit',
        'pages': pag_data['pages'],
        'counter': pag_data['counter']
    }
    return render(request, 'loadunit.html', context)


# def spread(request):
#
#     try:
#         loadUnit = LoadUnit.objects.get(name=request.POST.get('loadUnit'))
#         prof = Professors.objects.get(name=request.POST.get('prof'))
#         group = Group.objects.get(name=request.POST.get('group'))
#         Spread.objects.create(loadUnit=loadUnit, prof=prof, group=group)
#     except:
#        status = 'OK'
#
#     spread = Spread.objects.all()
#     profs = Professors.objects.all()
#     context = {
#         'spreads': spread,
#         'profs': profs,
#     }
#     return render(request, 'spread.html', context)


def report(request):
    DATA = []
    spreads = Spread.objects.filter(prof__id__gt=0).order_by('prof__last_name')
    groups = Group.objects.all()
    profs = spreads.values('prof').distinct()
    status = profs
    status = []
    for prof in profs:
        cur = {}      

        pr = Professors.objects.get(id=int(prof['prof']))
        cur['name'] = pr.last_name+' '+pr.first_name+' '+pr.middle_name+', '+pr.post.name+', '+pr.degree.name

        spr = spreads.filter(prof__id=int(prof['prof']))
        types = spr.values('loadUnit__typeLoad__name').order_by('-loadUnit__typeLoad__sort').distinct()
        cur['spread'] = []
        sum1=0
        sum2=0
        for tp in types:
            sub = spr.filter(loadUnit__typeLoad__name=tp['loadUnit__typeLoad__name'])
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
                    line['sub1'] = sub1[i].loadUnit.subject.name
                    factor=1
                    if sub1[i].loadUnit.typeLoad.typeTL == 'all':
                        gr1=groups.filter(caf=sub1[i].loadUnit.caf,sem=sub1[i].loadUnit.sem,grade=sub1[i].loadUnit.grade)
                    else:
                        gr1=groups.filter(id=sub1[i].group.id)
                        if sub1[i].loadUnit.typeLoad.typeTL == 'sub':
                            factor = Subgroup.objects.get(group_id=gr1[0].id).amount

                    line['gr1'] = []
                    for g in gr1:
                        postfix = ''
                        if g.grade == 'b':
                            postfix += u'\u0411' # 'Б'
                        elif g.grade == 'm':
                            postfix += u'\u041c' # 'M'
                        if factor > 1:
                            postfix += '('+str(factor)+')'
                        line['gr1'].append(g.caf.name+'-'+str(g.sem)+str(g.number)+postfix+' ['+str(g.amount)+'] ')
                    line['hour1'] = sub1[i].hours*factor
                    hourSum1 += line['hour1']

                if i < len(sub2):
                    line['sub2'] = sub2[i].loadUnit.subject.name
                    factor=1
                    if sub2[i].loadUnit.typeLoad.typeTL == 'all':
                        gr2=groups.filter(caf=sub2[i].loadUnit.caf,sem=sub2[i].loadUnit.sem,grade=sub2[i].loadUnit.grade)
                    else:
                        gr2=groups.filter(id=sub2[i].group.id)
                        if sub2[i].loadUnit.typeLoad.typeTL == 'sub':
                            factor = Subgroup.objects.get(group_id=gr2[0].id).amount

                    line['gr2'] = []
                    for g in gr2:
                        postfix = ''
                        if g.grade == 'b':
                            postfix += u'\u0411' # 'Б'
                        elif g.grade == 'm':
                            postfix += u'\u041c' # 'M'
                        if factor > 1:
                            postfix += '('+str(factor)+')'
                        line['gr2'].append(g.caf.name+'-'+str(g.sem)+str(g.number)+postfix
                            +' ['+str(g.amount)+'] ')
                    line['hour2'] = sub2[i].hours*factor
                    hourSum2 += line['hour2']

                lines.append(line)
            cur['spread'].append({'typeload':tp['loadUnit__typeLoad__name'],'subs':lines, 
                'hourSum1': hourSum1, 'hourSum2': hourSum2})
            sum1 += hourSum1
            sum2 += hourSum2
        cur['sum1'] = sum1
        cur['sum2'] = sum2
        DATA.append(cur)

    context = {
        'spreads' : spreads,
        'data' : DATA,
        'status' : status,
        'menu' : 'report'
    }

    # save into xls

    style_full  =  style_antibottom = style_antitop = style_top = style_bottom = style_left = style_right = style_topleft = style_topright = style_bottomleft = style_bottomright = style_clear = xlwt.easyxf('font: name Times New Roman, color-index black, bold off', num_format_str='#,##0')
    style_red = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0')
    style_bold = xlwt.easyxf('font: name Times New Roman, color-index black, bold on', num_format_str='#,##0')
    style_wrap = xlwt.easyxf('font: name Times New Roman, color-index black, bold off', num_format_str='#,##0')

    align = xlwt.Alignment()
    align.wrap = 1
    align.horz = xlwt.Alignment.HORZ_JUSTIFIED
    align.vert = xlwt.Alignment.VERT_JUSTIFIED
    style_wrap.alignment = align

    borders_full = xlwt.Borders()
    borders_full.bottom = borders_full.top = borders_full.left = borders_full.right = xlwt.Borders.THIN
    style_full.borders = style_red.borders = style_bold.borders = style_wrap.borders = borders_full

    borders_top = xlwt.Borders()
    borders_top.top = xlwt.Borders.THIN
    style_top.borders = borders_top

    borders_bottom = xlwt.Borders()
    borders_bottom.bottom = xlwt.Borders.THIN
    style_bottom.borders = borders_bottom
    
    borders_left = xlwt.Borders()
    borders_left.left = xlwt.Borders.THIN
    style_left.left = borders_left
    
    borders_right = xlwt.Borders()
    borders_right.top = xlwt.Borders.THIN
    style_right.borders = borders_right
    
    borders_topleft = xlwt.Borders()
    borders_topleft.top = borders_topleft.left = xlwt.Borders.THIN
    style_topleft.borders = borders_topleft

    borders_topright = xlwt.Borders()
    borders_topright.top = borders_topright.right = xlwt.Borders.THIN
    style_topright.borders = borders_topright

    borders_bottomleft = xlwt.Borders()
    borders_bottomleft.top = borders_bottomleft.left = xlwt.Borders.THIN
    style_bottomleft.borders = borders_bottomleft

    borders_bottomright = xlwt.Borders()
    borders_bottomright.top = borders_bottomright.right = xlwt.Borders.THIN
    style_bottomright.borders = borders_bottomright

    borders_antibottom = xlwt.Borders()
    borders_antibottom.top = borders_antibottom.left = borders_antibottom.right = xlwt.Borders.THIN
    style_antibottom.borders = borders_antibottom

    borders_antitop = xlwt.Borders()
    borders_antitop.bottom = borders_antitop.left = borders_antitop.right = xlwt.Borders.THIN
    style_antitop.borders = borders_antitop

    wb = xlwt.Workbook()
    ws = wb.add_sheet('Load')

    ws.col(0).width = 100*30
    ws.col(1).width = 120*30
    ws.col(2).width = 125*30
    ws.col(3).width = 60*30
    ws.col(4).width = 120*30
    ws.col(5).width = 125*30
    ws.col(6).width = 60*30
    ws.col(7).width = 60*30

    y = 0
    for obj in DATA:
        ws.write_merge(y, y, 0, 7, obj['name'], style=style_bold)
        ws.write_merge(y+1, y+2, 0, 0, u'Нагрузка',style=style_bold)
        ws.write_merge(y+1, y+1, 1, 3, u'Осенний семестр',style=style_bold)
        ws.write_merge(y+1, y+1, 4, 6, u'Весенний семестр',style=style_bold)
        ws.write_merge(y+1, y+2, 7, 7, u'Итого:',style=style_bold)
        ws.write(y+2, 1, u'Предмет',style=style_bold)
        ws.write(y+2, 2, u'Группы',style=style_bold)
        ws.write(y+2, 3, u'Часы',style=style_bold)
        ws.write(y+2, 4, u'Предмет',style=style_bold)
        ws.write(y+2, 5, u'Группы',style=style_bold)
        ws.write(y+2, 6, u'Часы',style=style_bold)
        y += 3

        for spr in obj['spread']:
            ws.write_merge(y, y+len(spr['subs']), 0, 0, spr['typeload'],style=style_full)
            ws.write_merge(y, y-1+len(spr['subs']), 7,7, '',style=style_full)
            for sub in spr['subs']:
                if 'sub1' in sub:
                    ws.write(y, 1, sub['sub1'] ,style=style_topleft)
                    ws.write(y, 2, sub['gr1'],style=style_wrap)
                    ws.write(y, 3, sub['hour1'],style=style_topright)
                else:
                    ws.write(y, 1, '',style=style_topleft)
                    ws.write(y, 2, '',style=style_top)
                    ws.write(y, 3, '',style=style_topright)
                if 'sub2' in sub:
                    ws.write(y, 4, sub['sub2'],style=style_topleft)
                    ws.write(y, 5, sub['gr2'],style=style_wrap)
                    ws.write(y, 6, sub['hour2'],style=style_topright)
                else:
                    ws.write(y, 4, '',style=style_topleft)
                    ws.write(y, 5, '',style=style_top)
                    ws.write(y, 6, '',style=style_topright)
                y += 1   
            ws.write_merge(y, y, 1, 2, u'Итого:',style=style_bold)
            ws.write(y, 3, spr['hourSum1'],style=style_bold)
            ws.write_merge(y, y, 4, 5, u'Итого:',style=style_bold)
            ws.write(y, 6, spr['hourSum2'],style=style_bold)
            ws.write(y, 7, spr['hourSum2'] + spr['hourSum1'],style=style_bold)
            y += 1
        ws.write(y, 0, '',style=style_topleft)
        ws.write_merge(y, y, 1, 2, u'Итого за осенний семестр:',style=style_bold)
        ws.write(y, 3, obj['sum1'],style=style_bold)
        ws.write_merge(y, y, 4, 5, u'Итого за весенний семестр:',style=style_bold)
        ws.write(y, 6, obj['sum2'],style=style_bold)
        ws.write(y, 7, obj['sum2']+obj['sum1'],style=style_red)
        y += 3

    wb.save('static/report.xls')
    return render(request, 'report.html', context)


def clear(request):
    Spread.objects.all().delete()
    LoadUnit.objects.all().delete()
    Group.objects.all().delete()
    return redirect('/')
