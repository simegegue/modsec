# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=500)
    text=models.TextField()
    cont=models.IntegerField(default=0)
   
    def __str__(self):              
            return self.name
    def count(self):
        self.cont = self.cont+1
        self.save()
        
    def reset(self):
        self.cont = 0
        self.save()
        
class Log(models.Model):
    date=models.CharField(max_length=200)
    atackType=models.CharField(max_length=200)
    text=models.TextField()
    dCreation=models.DateTimeField(default=timezone.now)
    def __str__(self):              
            return self.date

class Path(models.Model):
    text=models.CharField(max_length=250)
    
    def __str__(self):
            return self.text
        
class Rule(models.Model):
    name= models.CharField(max_length=200)
    text= models.TextField()
    lastMod=models.DateTimeField(default=timezone.now)
    path=models.ForeignKey(Path,on_delete=models.CASCADE)

    def __str__(self):          
            return self.name
        
    def updateDate(self):
        self.lastMod = timezone.now()
        self.save()
    
