from django.db import models

class Instructor(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	email = models.EmailField(max_length=200)
	instructorid = models.IntegerField(primary_key=True)
	date_registered = models.DateField()

class Course(models.Model):
	coursetitle = models.CharField(max_length=50)
	courseid = models.IntegerField(primary_key=True)
	# description = models.CharField(max_length=250) 



class Video(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=150)
	tags = models.CharField(max_length=50)
	instructorid = models.ForeignKey(Instructor, on_delete=models.CASCADE)
	courseid = models.ForeignKey(Course, on_delete=models.CASCADE)



