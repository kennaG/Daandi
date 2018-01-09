# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class student(models.Model):
	# use will already have name, lastname, email, username, password
	#user = models.OneToOneField(User,on_delete=models.DO_NOTHING, default=None)
	Name=models.CharField(max_length=30, null=True, blank = True)
	studentCode = models.IntegerField(default=None)
	SID= models.IntegerField(default=None, null = True)
	#DOB= models.DateField(default=None)
	#Email=models.EmailField(null=True, blank = True)
	#UserName=models.CharField(max_length=30,null=True, blank = True)
	#password=models.IntegerField(default=None)
	#foreign key here to parents

	#This code will be given distributed to parents. They will use it to get UN and password they use to login. 

	def __unicode__(self):
		return self.Name or u''

#database for parents
class parent(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,default=None)
	ParentID = models.AutoField(primary_key=True, default=None)
	Name=models.CharField(max_length=30, default=None, null=True, blank = True)
	#Email=models.EmailField(default=None)
	UserName=models.CharField(max_length=30, default=None, null=True, blank = True)
	password=models.IntegerField(default=None,null=True, blank = True)
	#phone=models.IntegerField(default=None, blank=True)
	
	#This code will be distributed to parents. They will use it to get UN and password they use to login. 
	ParentCode = models.IntegerField(default=None, blank=True)

	def __unicode__(self):
		return self.Name
