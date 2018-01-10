from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^StudentLogin/', views.StudentLogin, name='login'),
    url(r'^TeacherLogin/', views.TeacherLogin, name='TeacherLogin'),
    url(r'^ParentLogin/', views.ParentLogin, name='ParentLogin'),
    url(r'^StudentRegistration/', views.StudentRegistration, name='StudentRegistration'),
    url(r'^TeacherRegistration/', views.TeacherRegistration, name='TeacherRegistration'),
    url(r'^ParentRegistration/', views.ParentRegistration, name='ParentRegistration'),
    url(r'^(?P<id>\d+)/$', views.student_detail, name='Details/(?P<id>\d+)/'),
    

    #url(r'^TeacherRegister/', views.register, name='register'),
    #url(r'^ParentRegister/', views.register, name='register'),
    #url(r'^StudentLogin/', views.register, name='register'),
    #url(r'^parentLogin/', views.register, name='register'),
    #url(r'^TeacherLogin/', views.register, name='register')
]