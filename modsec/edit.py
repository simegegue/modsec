import django
import sys, os
from django.template.defaultfilters import length
sys.path.append("/home/nomis/tfg-workspace/modsec")
os.environ['DJANGO_SETTINGS_MODULE'] = 'TFG.settings'

django.setup()
from modsec.models import Rule
import os.path
from os import listdir
from os.path import islink, isdir
import re

def edit(rule_id):
    p="/home/nomis/tfg-workspace/modsec/modsec/restartServer"
    rule=Rule.objects.get(pk=rule_id)
    for archivo in listdir(rule.path.text):
        if archivo==rule.name:
            if not isdir(archivo) and not islink(archivo):
                f=open(rule.path.text + rule.name, "w")
                f.write(rule.text.encode("utf-8"))
                f.close()
                os.system("sh "+ p)
def create(rule_id):
    p="/home/nomis/tfg-workspace/modsec/modsec/restartServer"
    rule=Rule.objects.get(pk=rule_id)
    f=open(rule.path.text + rule.name, "w")
    f.write(rule.text.encode("utf-8"))
    f.close()
    print("Creado archivo")
    os.system("sh "+ p)
       
