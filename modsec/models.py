# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Rule(models.Model):
    name= models.CharField(max_length=200)
    text= models.TextField()
    lastMod=models.DateTimeField(default=timezone.now)

    def __str__(self):          
            return self.name
        
    def updateDate(self):
        self.lastMod = timezone.now()
        self.save()
    
class Log(models.Model):
    date=models.CharField(max_length=200)
    atackType=models.CharField(max_length=200)
    text=models.TextField()
    
    def __str__(self):              
            return self.date
