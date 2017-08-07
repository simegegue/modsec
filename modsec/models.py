# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class Rule(models.Model):
    name= models.CharField(max_length=200)
    text= models.TextField()
    lastMod=models.DateTimeField(default=timezone.now)

class Log(models.Model):
    date=models.DateTimeField(blank=False,null=False)
    atackType=models.CharField(max_length=200)
    text=models.TextField()