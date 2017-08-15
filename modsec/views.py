# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from modsec.models import Log,Rule
from django.http import Http404
# Create your views here.
def index(request):
    ultimos_logs = Log.objects.order_by('-date')[:5]
    
    reglas_recientes= Rule.objects.order_by('-lastMod')[:5]
    aux ={'reglas_recientes': reglas_recientes,'ultimos_logs':ultimos_logs }
    
    return render(request, 'modsec/index.html', aux)

def rules(request):
    reglas=Rule.objects.all()
    paginator = Paginator(reglas, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        reglas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        reglas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        reglas = paginator.page(paginator.num_pages)

    context={'reglas': reglas}
    return render(request, 'modsec/rules.html',context)

def logs(request):
    registros=Log.objects.all()
    paginator = Paginator(registros, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        registros = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        registros = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        registros = paginator.page(paginator.num_pages)

    context={'registros': registros}
    return render(request, 'modsec/logs.html',context)

def showRule(request,rule_id):
    try:
        rule = Rule.objects.get(pk=rule_id)
    except Rule.DoesNotExist:
        raise Http404("Rule does not exist")
    return render(request, 'modsec/displayRule.html', {'rule': rule})

def showLog(request,log_id):
    try:
        log = Log.objects.get(pk=log_id)
    except Log.DoesNotExist:
        raise Http404("Log does not exist")
    return render(request, 'modsec/displayLog.html', {'log': log})

