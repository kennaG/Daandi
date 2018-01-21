# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class student(models.Model):
	# user will already have name, lastname, email, username, password
	# this is both foreign key and also makes sure sure the relation is one-to-one.
	user = models.OneToOneField(User,on_delete=models.DO_NOTHING, default=None)
	student_id = models.AutoField(primary_key = True, default = None)
	Name = models.CharField(max_length=30, null=True, blank = True)
	studentCode = models.IntegerField(default=None)
	SID= models.IntegerField(default=None, null = True)
	DOB= models.DateField(default=None)
	GradeLevel = models.CharField(max_length=2,null=True,blank=True)

	def __unicode__(self):
		return self.Name or u''

#database for parents
class parent(models.Model):
	user = models.OneToOneField(User,on_delete=models.DO_NOTHING,default=None)
	parent = models.OneToOneField(student, on_delete=models.CASCADE, default=None) #new
	ParentID = models.AutoField(primary_key=True, default=None)
	phone=models.IntegerField(default=None, blank=True, null = True)
	#This code will be distributed to parents. They will use it to get UN and password they use to login. 
	#ParentCode = models.IntegerField(default=None, blank=True) # just using emails to activate account for now.


	def __unicode__(self):
		return self.Name

'''
class assignments(models.Model):
	students = models.OneToOneField(student,on_delete=models.DO_NOTHING,default=None)
	Aname = models.CharField()
	assigned_date = models.DateField()
	due_date = models.DateField()
	total_points_possible = CharField(default=None, blank=True, null = True)

'''