import django
import sys, os
from django.template.defaultfilters import length
sys.path.append("/home/nomis/tfg-workspace/TFG")
os.environ['DJANGO_SETTINGS_MODULE'] = 'TFG.settings'

django.setup()
from modsec.models import Rule, Log
import os.path
from os import listdir
from os.path import islink, isdir
import re

BASE = os.path.dirname(os.path.abspath(__file__))

def loadInfo():
    dir1 = "/usr/share/modsecurity-crs/rules/"
    lf = []
    for archivo in listdir(dir1):
        if not isdir(archivo) and not islink(archivo):
            f = open(dir1 + archivo)
            datos = f.read()
            f.close()
            """print "** %s **" % archivo"""
            lf.append(archivo)
            rule_name = archivo
            rule_text = datos
           
            Rule.objects.create(name=rule_name, text=rule_text)
    print("Reglas cargadas correctamente")  
    
    
    dir2 = "/var/log/apache2/"
    arch = "camundaError.log"
    ls = []
    s = []
    for archivo in listdir(dir2):
        if not isdir(archivo) and not islink(archivo) and archivo == arch:
            f = open(dir2 + archivo)
            datos = f.read()
            f.close()
         
            ls = datos.split("\n")
            ls.pop()
           
    for i in ls:
        s = i.split("]")
        s = addchar(s) 
        aux1 = []
        log_atack = ""
        for d in s:
            if "msg" in d:
                print(d[7:-2])
                log_atack = d[7:-2]
        log_date = s[0].strip("[,]")
       
        log_text = i
        Log.objects.create(date=log_date,atackType=log_atack,text=log_text)
    print("Log cargado correctamente") 
    
def addchar(s):
    aux = []
    for l in s:
        l = l + "]"
        aux.append(l)
    
    return aux
    
if __name__ == '__main__':
    loadInfo()
