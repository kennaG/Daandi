# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
#from .models import student #bucky's method
from django.contrib.auth import (authenticate, get_user_model,logout)
from django.contrib.auth import login as auth_login
from django.shortcuts import render, get_object_or_404
from .forms import UserLoginForm, StudentRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.contrib import messages
#from .forms import ParentSignUpForm
from django.http import HttpResponseRedirect, HttpResponse

user = get_user_model()
#from .forms import NameForm
#from .models import student

from django.forms import modelformset_factory
#from .forms import UserRegistrationForm # the other source
#from django.views.generic.edit import CreateView, UpdateView, DeleteView #also buckys method

from .forms import StudentRegistrationForm #ParentRegsitrationForm #could be used when I find our onetoone thing

# Create your views here.
def index(request):
	return render(request,'htmlFiles/Home.html')

def StudentLogin(request): #the name register here is misleading.
	print(request.user.is_authenticated())
	
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")

		#redirect goes here -- what will the user see once they login. In this is case it is pretty much profiles.
	return render(request,'htmlFiles/StudentLoginForm.html', {"form":form})

def ParentLogin(request):
	return render(request, 'htmlFiles/ParentLoginForm.html')

def TeacherLogin(request):
	return render(request, 'htmlFiles/TeacherLoginForm.html')

def StudentRegistration(request):
	title = "Student Register"
	form = StudentRegistrationForm(request.POST or None)
	
	if form.is_valid():
		
		
		user = form.save(commit=False)
		password = form.cleaned_data.get('password') #have to build the function for model student - User model has built in.
		user.set_password(password)
		user.save()
		new_user =authenticate(username = user.username, password = password)
		login(request, new_user)
		
	context = {
		"form" : form,
		"title" : title
	}
	return render(request, 'htmlFiles/StudentRegistrationForm.html', context)

def TeacherRegistration(request):
	return render(request, 'htmlFiles/TeacherRegistrationForm.html')


def ParentRegistration(request):
	title = "Student Register"
	form = ParentRegistrationForm(request.POST or None)
	
	if form.is_valid():
		
		
		user = form.save(commit=False)
		password = form.cleaned_data.get('password') #have to build the function for model student - User model has built in.
		user.set_password(password)
		user.save()
		new_user =authenticate(username = user.username, password = password)
		login(request, new_user)
		
	context = {
		"form" : form,
		"title" : title
	}
	return render(request, 'htmlFiles/ParentRegistrationForm.html', context)

'''    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            Name = request.POST.get('Name', '')
            Email = request.POST.get('Email','')
            SID = request.POST.get('SID', '')
            Name_object = student(Name=Name, Email = Email, SID = SID)
            # process the data in form.cleaned_data as required
            Name_object.save()
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/htmlFiles/ParentRegistrationForm/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
'''
	

'''
	if 'ParentCode' in request.GET and request.GET['ParentCode']:
		code = request.GET['ParentCode']
		user = None
		parent = None
		student_set = parent.objects.all().filter(parentID = code)
		if len(student_set) == 1:
			parent = student_set[0].parent
			
		return render(request,"htmlFiles/ParentRegistrationForm.html",{'user': user, 'ParentCode':code})
	else:
		return HttpResponse("Please Enter a valid Parent Code")
'''
		
def log_out(request):
	logout(request)
	return render(request, 'htmlFiles/Home') # not sure if there is home in my template but can be created.


def student_detail(request, id=None):
	#queryset = student.objects.all()
	instance = get_object_or_404(student, id=id)

	context = {
		
		"title":"Student Detail",
		"instance":instance
	}
	return render(request,'htmlFiles/student_details.html',context)

# for later use. This maybe a link teacher interfaceinterface. This one only displays name of list of students.
def student_list(request):
	queryset = student.objects.all()

	context = {
		"object_list":queryset,
		"title":instance
	}
	return render(request,'htmlFiles/student_list.html',context)




def login(request):
    if request.user.is_authenticated():
        return redirect('admin_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
			auth_login(request, user)
			return redirect('admin_page')
            #login(request)

            

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return render(request,'registration/logout.html')


def admin_page(request):
    if not request.user.is_authenticated():
        return redirect('blog_login')

    return render(request, 'registration/admin_page.html')