# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from modsec.models import Log,Rule
# Create your views here.
def index(request):
    ultimos_logs = Log.objects.order_by('-date')[:5]
    
    reglas_recientes= Rule.objects.order_by('-lastMod')[:5]
    aux ={'reglas_recientes': reglas_recientes,'ultimos_logs':ultimos_logs }
    
    return render(request, 'modsec/index.html', aux)