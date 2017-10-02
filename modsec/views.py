# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404,redirect
from modsec.models import Log,Rule,Path
from django.http import Http404
from modsec.forms import selectRule, selectLog, ruleForm, pathForm,createRuleForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from modsec.edit import edit,create


# Create your views here.
'''---------------Vista principal-----------------------'''
@login_required(login_url='/modsec/login')
def index(request):
    ultimos_logs = Log.objects.order_by('-date')[:5]
    
    reglas_recientes= Rule.objects.order_by('-lastMod')[:5]
    aux ={'reglas_recientes': reglas_recientes,'ultimos_logs':ultimos_logs }
    
    return render(request, 'modsec/index.html', aux)

'''---------------Login----------------------------------'''
def access(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('notuser')
    else:
        form=AuthenticationForm()
        context={'form':form}
    return render(request, 'modsec/login.html',context )

'''---------------LoginError----------------------------------'''
def notuser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('notuser')
    else:
        form=AuthenticationForm()
        context={'form':form}
    return render(request, 'modsec/notuser.html',context )

'''---------------Logout----------------------------------'''
@login_required(login_url='/modsec/login')
def cerrar(request):
    logout(request)
    return redirect('/modsec/login')

'''---------------Lista de reglas--------------------------'''
@login_required(login_url='/modsec/login')
def rules(request):
    rule=""
    
    if request.method == 'POST':
        form = selectRule(request.POST)
        if form.is_valid():
            rule=form.cleaned_data['ruleSel']
            rules=Rule.objects.all()
            reglas=[]
            for r in rules:
                if str(rule)==str(r):
                    reglas.append(r)
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
            context={'form':form,'reglas':reglas,'rule': rule}
            return render(request, 'modsec/rules.html',context)
            
    
    else:
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

        form = selectRule()
        context={'form':form,'reglas':reglas,'rule': rule}
    return render(request, 'modsec/rules.html',context)
   
'''---------------Lista de registros----------------------------------'''
@login_required(login_url='/modsec/login')
def logs(request):
    
    log=""
    
    if request.method == 'POST':
        form = selectLog(request.POST)
        if form.is_valid():
            log=form.cleaned_data['logSel']
            logs=Log.objects.all()
            registros=[]
            for l in logs:
                if str(log)==str(l):
                    registros.append(l)
            paginator = Paginator(registros, 10) # Show 10 contacts per page
    
            page = request.GET.get('page')
            try:
                registros = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                registros = paginator.page(1)
            except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
                registros = paginator.page(paginator.num_pages)
            context={'form':form,'registros':registros,'log': log}
            return render(request, 'modsec/logs.html',context)
    else:
        registros=Log.objects.all()
        paginator = Paginator(registros, 10) # Show 10 contacts per page
    
        page = request.GET.get('page')
        try:
            registros = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            registros = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            registros = paginator.page(paginator.num_pages)

    

        form = selectLog()
        context={'form':form,'registros':registros,'log': log}
    return render(request, 'modsec/logs.html',context)

'''---------------Mostrar regla----------------------------------'''
@login_required(login_url='/modsec/login')
def showRule(request,rule_id):
    try:
        rule = Rule.objects.get(pk=rule_id)
    except Rule.DoesNotExist:
        raise Http404("Rule does not exist")
    return render(request, 'modsec/displayRule.html', {'rule': rule})
'''---------------Mostrar registro----------------------------------'''
@login_required(login_url='/modsec/login')
def showLog(request,log_id):
    try:
        log = Log.objects.get(pk=log_id)
    except Log.DoesNotExist:
        raise Http404("Log does not exist")
    return render(request, 'modsec/displayLog.html', {'log': log})
'''---------------Editar regla----------------------------------'''
@login_required(login_url='/modsec/login')
def editRule(request, rule_id): 
    rule = get_object_or_404(Rule, pk=rule_id)
    form = ruleForm(request.POST or None, instance=rule)
    if form.is_valid():
        form.save()
        rule.updateDate()
        edit(rule_id)
        return redirect('showRule', rule_id)
        
    return render(request, 'modsec/editRule.html', {'form': form})
'''---------------Crear regla----------------------------------'''
@login_required(login_url='/modsec/login')
def createRule(request):
    if request.method=='POST':
        form=createRuleForm(request.POST)
        if form.is_valid():
            rule=form.save()
            create(rule.id)
            return redirect('showRule', rule.id)
    else:
        form=createRuleForm()
    return render(request,'modsec/createRule.html',{'form':form})   
'''---------------Mostrar directorios--------------------------------''' 
@login_required(login_url='/modsec/login')
def paths(request):
    directorios=Path.objects.all()
    paginator = Paginator(directorios, 10)

    page = request.GET.get('page')
    try:
        directorios = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        directorios = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        directorios = paginator.page(paginator.num_pages)

    
    context={'directorios':directorios}
    return render(request, 'modsec/conf.html',context)
'''---------------Añadir directorio----------------------------------'''   
@login_required(login_url='/modsec/login')
def addPath(request):
    if request.method=='POST':
        form=pathForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paths')
    else:
        form=pathForm()
    return render(request,'modsec/editPath.html',{'form':form})
'''---------------Editar directorio----------------------------------''' 
@login_required(login_url='/modsec/login')
def editPath(request,path_id):
    path = get_object_or_404(Path, pk=path_id)
    form = pathForm(request.POST or None, instance=path)
    if form.is_valid():
        form.save()
        return redirect('paths')
        
    return render(request, 'modsec/editPath.html', {'form': form})

    
