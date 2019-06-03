from django.db import models

class Instructor(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	email = models.CharField(max_length=40)
	instructorid = models.CharField(max_length=40)

class Course(models.Model):
	coursetitle = models.CharField(max_length=50)
	courseid = models.CharField(max_length=50)


class Video(models.Model):
	title = models.CharField(max_length=40)
	description = models.CharField(max_length=50)
	tags = models.CharField(max_length=40)
	instructorid = models.CharField(max_length=50)
	courseid = models.CharField(max_length=50)



