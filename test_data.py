import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','schoolsite.settings')
import django
django.setup()
from django.conf import settings

import random # need this for subjects.

from faker import Faker # this is for generating random users for a given model.

from django.contrib.auth.models import User 
''' this part is for django's systems. '''
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


import json, codecs # enables me to use json.

subjects = ["eng", "chem", "physics","Bio", "eng"] # not sure if I still need this.

''' This will create users. '''
def form_user(model="auth.User"): # for student (model="home_page_app.student")
	faker = Faker()
	last_user_id = 4 #because at this point, there were 4 data already in the user model.
	last_teacher_id = 1
	subjects = [
		{"model":"home_page_app.subject","pk":1,"fields":{"subjectName":"eng"}},
		{"model":"home_page_app.subject","pk":2,"fields":{"subjectName":"chem"}},
		{"model":"home_page_app.subject","pk":3,"fields":{"subjectName":"physics"}},
		{"model":"home_page_app.subject","pk":4,"fields":{"subjectName":"Bio"}}
	]
	entities = {"subjects":subjects,"users":[],"teachers":[]}

	for i in range(100):
		user = {"model":model,"pk":last_user_id,"fields":{}}
		user["fields"]["username"] = "%s_%d" % (faker.user_name(),last_user_id) # creates fake username."%s_%d" % is basically ensuring no duplicate usernames.
		user["fields"]["email"] = faker.safe_email() #safe_email - one that does not break your system and is not a real email.
		user["fields"]["password"] = "password"
		entities["users"].append(user)

		teacher_model = "home_page_app.teacher"
		teacher = {"model":teacher_model,"pk":last_teacher_id,"fields":{}}
		teacher["fields"]["user"] = last_user_id
		teacher["fields"]["first_name"] = faker.name() 
		teacher["fields"]["last_name"] = faker.name()
		teacher["fields"]["Subject"] = random.randint(1,4)
		entities["teachers"].append(teacher)
		last_user_id += 1
		last_teacher_id += 1
	return entities

# user_models = form_user()
# with codecs.open("user_data.json","w","utf8") as json_file: # the data generated is being loaded into user_data.json.
# 	json_file.write(json.dumps(user_models["users"],sort_keys=True,ensure_ascii=False))

# can use the following by ,making the last_teacher_id a global variable.
'''
def form_teacher(model="home_page_app.teacher"): # for student (model="home_page_app.student")
	faker = Faker()
	last_user_id = 3 #because at this point, there were 4 data already in the user model.
	entities = {"teachers":[]}
	for i in range(100):
		user = {"model":model,"pk":last_user_id,"fields":{}}
		user["fields"]["user"] = last 
		user["fields"]["first_name"] = faker.name() 
		user["fields"]["last_name"] = faker.name()
		user["fields"]["subject"] = subjects[random.randint(0,3)] # will pick one of the subject and assign.
		entities["teacher"].append(user)
		last_user_id += 1
	return entities
'''
teacher_models = form_user()
with codecs.open("teacher_data.json","w","utf8") as json_file: # the data generated is being loaded into user_data.json.
	json_file.write(json.dumps(teacher_models["subjects"] + teacher_models["users"] + teacher_models["teachers"],sort_keys=True,ensure_ascii=False))





'''  this part is for laoding a json file into an already existing user model. '''
# with open(sys.argv[1],"r") as json_file:
# 	storedata = json.load(json_file)

# for index, user in enumerate(User.objects.all()):
# 	user.email = storedata[index % len(storedata)]["email"]
# 	user.password = storedata[index % len(storedata)]["password"]
# 	user.set_password(user.password)
# 	user.save()
