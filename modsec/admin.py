# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modsec.models import Log,Rule
# Register your models here.
admin.site.register(Log)
admin.site.register(Rule)