# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class subject(models.Model):
	subject_id = models.AutoField(primary_key=True,default=True)
	subjectName = models.CharField(max_length = 30, null=True, blank = True)
	
	def __unicode__(self):
		return self.subjectName

class teacher(models.Model):
	user = models.OneToOneField(User,on_delete=models.DO_NOTHING,default=None)
	first_name = models.CharField(max_length = 30, null=True, blank = True)
	last_name = models.CharField(max_length = 30, null=True, blank = True)
	email = models.CharField(max_length = 30, null=True, blank = True)
	phone = models.CharField(max_length = 30, null=True, blank = True)
	TeacherId = models.AutoField(primary_key=True,default=True) 
	Subject = models.ForeignKey(subject, on_delete=models.DO_NOTHING, default=None) 

	def __unicode__(self):
		return self.first_name	

class assignment(models.Model):
	#students = models.OneToOneField(student,on_delete=models.DO_NOTHING,default=None)
	Aname = models.CharField(max_length = 30, null=True, blank = True)
	assigned_date = models.DateField()
	due_date = models.DateField()
	total_points_possible = models.CharField(max_length=100, default=None, blank=True, null = True)
	FK_to_subject = models.ForeignKey(subject, on_delete=models.DO_NOTHING, default=None)
	score = models.IntegerField(default=None, null=True, blank=True)

	def __unicode__(self):
		return self.Aname

class clas(models.Model):
	level = models.CharField(max_length = 6, null=True, blank = True)
	sections = models.CharField(max_length = 6, null=True, blank = True)
	subjectsFK = models.ManyToManyField(subject)

	def __unicode__(self):
		return self.level




class student(models.Model):
	# user will already have name, lastname, email, username, password
	# this is both foreign key and also makes sure sure the relation is one-to-one.
	user = models.OneToOneField(User,on_delete=models.DO_NOTHING, default=None)
	student_id = models.AutoField(primary_key = True, default = None)
	Name = models.CharField(max_length=30, null=True, blank = True)
	studentCode = models.IntegerField(default=None)
	SID= models.IntegerField(default=None, null = True)
	DOB= models.DateField(default=None)
	GradeLevelFK = models.ForeignKey(clas,on_delete=models.DO_NOTHING,default=None)


	def __unicode__(self):
		return self.Name or u''

#table for parents
class parent(models.Model):
	user = models.OneToOneField(User,on_delete=models.DO_NOTHING,default=None)
	parent = models.ForeignKey(student, on_delete=models.CASCADE, default=None) #creates a contraint on parents so they only exist if they have student at the school.
	ParentID = models.AutoField(primary_key=True, default=None)
	phone= models.IntegerField(default=None, blank=True, null = True)
	fName = models.CharField(max_length=30, null=True, blank = True)
	lName = models.CharField(max_length=30, null=True, blank = True)
	
	#This code will be distributed to parents. They will use it to get UN and password they use to login. 
	#ParentCode = models.IntegerField(default=None, blank=True) # just using emails to activate account for now.


	def __unicode__(self):
		return self.fName



