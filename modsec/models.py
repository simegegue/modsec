# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Log(models.Model):
    date=models.CharField(max_length=200)
    atackType=models.CharField(max_length=200)
    text=models.TextField()
    
    def __str__(self):              
            return self.date

class Path(models.Model):
    text=models.CharField(max_length=250)
    
    def __str__(self):
            return self.text
        
class Rule(models.Model):
    name= models.CharField(max_length=200)
    text= RichTextField(config_name='default',extra_plugins=['codesnippet'],)
    lastMod=models.DateTimeField(default=timezone.now)
    path=models.ForeignKey(Path,on_delete=models.CASCADE)

    def __str__(self):          
            return self.name
        
    def updateDate(self):
        self.lastMod = timezone.now()
        self.save()
    