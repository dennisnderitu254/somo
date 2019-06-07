from django.db import models
from django.utils.translation import gettext as _

class Instructor(models.Model):
	DOCTOR = "Dr."
	PROFESSOR = "Prof."
	MR = "Mr."
	MRS = "Mrs."
	TITLE_CHOICES  = [
		(DOCTOR, _("Doctor")),
		(PROFESSOR,_("Professor")),
		(MR, _("Mr.")),
		(MRS, _("Mrs.")),
	]
	firstname = models.CharField("instructor first name",max_length=50)
	lastname = models.CharField("instructor last name",max_length=50)
	email = models.EmailField("instructor email",max_length=200)
	title = models.CharField("instructor email",choices=TITLE_CHOICES, help_text= _("This shows the salutation an instructor possesses"))
	date_registered = models.DateField()

class Course(models.Model):
	coursetitle = models.CharField("course title",max_length=50)
	courseid = models.IntegerField("course id", primary_key=True)


class Video(models.Model):
	title = models.CharField("video title",max_length=50)
	description = models.CharField("video description",max_length=150)
	tags = models.CharField("video tags",max_length=50)
	instructorid = models.ForeignKey("instructor id",Instructor, on_delete=models.CASCADE)
	courseid = models.ForeignKey("course id",Course, on_delete=models.CASCADE)



