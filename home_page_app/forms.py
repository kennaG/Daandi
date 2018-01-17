
from django.forms import ModelForm # this is for creating a form for our model.
from django import forms
from django.contrib.auth import authenticate, get_user_model,login,logout
from .models import student
from .models import parent #I m ight need this later
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


user=get_user_model()

#this is for the 'studentLogin' although it says userlogin.
class UserLoginForm(forms.Form): #this has to be forms.Form. why ? the others are ModelForm. maybe because they refer to other forms fields.
	username=forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		user = authenticate(username=username, password=password)

		if not user:
			raise forms.ValidationError("This user does not exist")
		if not user.check_password(password):
			raise forms.ValidationError("Incorrect Password")
		if not user.is_active:
			raise forms.ValidationError("This User is no longer active")

		return super(UserLoginForm,self).clean(*args, **kwargs)


class StudentRegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = user
		fields = [
		'email', 'username', 'password'
		]
'''
	def search_student_code(self):
		studentCode = self.cleaned_data.get('studentCode')
		sc = user.objects.filter(studentCode = studentCode)
		if sc.exists() == True:
			raise forms.ValidationError("You can't register")

		return super(StudentRegistrationForm,self).search_student_code(*args, **kwargs)
'''


#this is a demo form for new parent registration. Not going to use this according to the specification.
class NameForm(forms.ModelForm):
	
	class Meta:
		model = parent
		fields = ['ParentID']
	
'''
why doesn't this work ???
class ParentRegsitrationForm(forms.ModelForm):
	class Meta:
		model = user
		fields = ['ParentCode', 'password','username']

'''




#This is pretty ,much a registration form for a parent. Once they enter the following fields they will be given UserName and password
# from the model above and they can use that to login and see info about their kids.
'''
class ParentSignUpForm(ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	ParentCode = forms.IntegerField() # I put this here because I think it has to be here or else the user will not be required to fill the area.
	class Meta:
		model=student
		fields = ['SID']
'''
