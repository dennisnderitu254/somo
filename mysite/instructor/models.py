from django.db import models
from django.utils.translation import gettext as _

class Instructor(models.Model):
	DOCTOR = "Dr."
	PROFESSOR = "Prof."
	MR = "Mr."
	MRS = "Mrs."
	TITLE_CHOICES  = _([
		(DOCTOR, "Doctor"),
		(PROFESSOR, "Professor"),
		(MR, "Mr."),
		(MRS, "Mrs.")
	])
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	email = models.EmailField(max_length=200)
	title = _(models.CharField(choices=TITLE_CHOICES, description="This shows the salutation an instructor possesses"))
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



