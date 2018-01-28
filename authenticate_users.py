import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','schoolsite.settings')
import django
django.setup()
from django.conf import settings


from django.contrib.auth.models import User 
''' this part is for django's systems. '''
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


for user in User.objects.all():
	user.set_password(user.password)
	user.save()
