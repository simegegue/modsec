import django
import sys, os
from django.template.defaultfilters import length
sys.path.append("/home/nomis/tfg-workspace/TFG")
os.environ['DJANGO_SETTINGS_MODULE'] = 'TFG.settings'

django.setup()
from modsec.models import  Log
import os.path
from os import listdir
from os.path import islink, isdir


BASE = os.path.dirname(os.path.abspath(__file__))

def loadLogs():
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
        try:
            Log.objects.get(date=s[0].strip("[,]"))
        except:
            log_atack = ""
           
            for d in s:
                if "msg" in d:
                    
                    log_atack = d[7:-1]
            log_date = s[0].strip("[,]")
            aux=""
            
            for c in s:
                if "Matched Data" in c:
                    c=""
                if "pid" in c:
                    c=c[5:]
                    aux=aux+"PID:"+c + "\n"
                if "client" in c:
                    c=c[8:]
                    aux=aux+"Client:"+c +"\n"
                if "file" in c:
                    k=c.split("[")
                    c=k[1]
                    c=c[5:]
                    aux=aux+"File:"+c +"\n"
                    
                if "line" in c:
                    c=c[6:]
                    aux=aux+"Line:"+c +"\n"
                    
                
                if "msg" in c:
                    c=c[6:]
                    aux=aux+"Message:"+c+"\n"
                    
                    
                if "maturity" in c:
                    c=c[10:]
                    aux=aux+"Maturity:"+c+"\n"
                    
                    
                if "accuracy" in c:
                    c=c[10:]
                    aux=aux+"Accuracy:"+c+"\n"
                    
                
                if "tag" in c:
                    if "Tag" not in aux:
                        c=c[5:]
                        aux=aux+"Tag:"+c+"\n"
                   
                    
                if "uri " in c:
                    c=c[5:]
                    aux=aux+"URI:"+c+"\n"
                    print(aux)
            log_text = aux
            Log.objects.create(date=log_date,atackType=log_atack,text=log_text)
    print("Log cargado correctamente") 
    
'''def addchar(s):
    aux = []
    for l in s:
        l = l + "]"
        aux.append(l)
    
    return aux'''
    
if __name__ == '__main__':
   loadLogs()
   