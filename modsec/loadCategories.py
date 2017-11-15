import django
import sys, os

from django.template.defaultfilters import length
sys.path.append("/home/nomis/tfg-workspace/modsec")
os.environ['DJANGO_SETTINGS_MODULE'] = 'TFG.settings'

django.setup()
from modsec.models import Category,Path,Log
import os.path
from os import listdir
from os.path import islink, isdir


BASE = os.path.dirname(os.path.abspath(__file__))

def loadCategory():
    directorio=Path.objects.all()
    lf = []
    
    for dir1 in directorio:
        for archivo in listdir(dir1.text):
            if not isdir(archivo) and not islink(archivo):
                f = open(dir1.text + archivo)
                datos = f.read()
                f.close()
               
                try:
                    if "REQUEST" in archivo:
                        cat=archivo[12:-5]
                        cat=cat.replace("-"," ")
                    if "RESPONSE" in archivo:
                        cat=archivo[13:-5]
                        cat=cat.replace("-"," ")
                    s=datos.split("\n")
                    c=Category.objects.get(name=cat)
                    aux2=[]
                    
                    for i in s:
                        if "msg:" in i:
                            
                            f=i[:-2]
                            aux2.append(f)
                            
                    if aux2!=c.text and len(aux2)>0:
                        Category.objects.get(name=c.name).delete()
                        Category.objects.create(name=c.name, text=aux2,cont=0)
                        
                        
                except:
                    cat=""
                    if "REQUEST" in archivo:
                        cat=archivo[12:-5]
                        cat=cat.replace("-"," ")
                    if "RESPONSE" in archivo:
                        cat=archivo[13:-5]
                        cat=cat.replace("-"," ")
                    s=datos.split("\n")
                    aux=[]
                    for i in s:
                        if "msg:" in i:
                            
                            f=i[:-2]
                            aux.append(f)
                    if len(aux)>0:
                        Category.objects.create(name=cat, text=aux,cont=0)
    print("Categorias cargadas correctamente")  
    

def prueba():
    logs=Log.objects.all()
    cats=Category.objects.all()
    for ca in cats:
        ca.reset()
    for l in logs:
        for c in cats:
            if len(l.atackType)>1 and l.atackType in c.text:
                print("Atack:"+l.atackType)
                print(c.text)
                c.count()
                
                
    act=Category.objects.all()
    for i in act:
        print(i.name)
        print(i.text)
        print(i.cont)
    list=Category.objects.all()
    aux=[]
    res="["
    for p in list:
        res=res+"{"+"label:\""+p.name+"\",value:\""+str(p.cont)+"\"},"
    
    res=res[:-1]
    res=res+"];"
    print(res)
if __name__ == '__main__':
    prueba()   
