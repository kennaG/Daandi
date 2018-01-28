# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import student
from .models import parent,assignment,teacher,subject,clas
# Register your models here.
admin.site.register(student)
admin.site.register(parent)
admin.site.register(assignment)
admin.site.register(teacher)
admin.site.register(subject)
admin.site.register(clas)