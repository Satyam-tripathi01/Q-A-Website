from django.db import models

# Create your models here.

class user_login(models.Model):
	fname = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=50)
	
class question_box(models.Model):
	question = models.CharField(max_length=200)
	user = models.CharField(max_length=100)
	
class answers(models.Model):
	question = models.CharField(max_length=100000)
	answer = models.CharField(max_length=500)
	user = models.CharField(max_length=50)
	
class hello(models.Model):
	a = models.CharField(max_length=10)
	b = models.CharField(max_length=500)
	c = models.CharField(max_length=50)
	
