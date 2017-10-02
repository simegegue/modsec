import django
import sys, os
from django.template.defaultfilters import length
sys.path.append("/home/nomis/tfg-workspace/modsec")
os.environ['DJANGO_SETTINGS_MODULE'] = 'TFG.settings'

django.setup()
from modsec.models import Rule, Log,Path
import os.path
from os import listdir
from os.path import islink, isdir
import re

BASE = os.path.dirname(os.path.abspath(__file__))

def loadInfo():
    directorio=Path.objects.all()
    lf = []
    
    for dir1 in directorio:
        for archivo in listdir(dir1.text):
            if not isdir(archivo) and not islink(archivo):
                f = open(dir1.text + archivo)
                datos = f.read()
                f.close()
                '''print "** %s **" % archivo'''
                try:
                    Rule.objects.get(name=archivo)
                except:
                    lf.append(archivo)
                    rule_name = archivo
                    rule_text = datos
                    
                    Rule.objects.create(name=rule_name, text=rule_text,path=dir1)
                
    print("Reglas cargadas correctamente")  
    

    
if __name__ == '__main__':
   loadInfo()
   
