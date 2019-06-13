from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Instructor(User):
	DOCTOR = "Dr."
	PROFESSOR = "Prof."
	MR = "Mr."
	MRS = "Mrs."
	TITLE_CHOICES  = [
		(DOCTOR, _("Doctor")),
		(PROFESSOR, _("Professor")),
		(MR, _("Mr.")),
		(MRS, _("Mrs.")),
	]
	title = models.CharField(choices=TITLE_CHOICES, help_text= _("Instructor's salutation"))
	
	
class Course(models.Model):
	name = models.CharField(_("name"), max_length=120)
	instructor = models.ForeignKey(Instructor, verbose_name=_("instructor"), on_delete=models.CASCADE)
	description = models.TextField(_("description"))

class Video(models.Model):
	title = models.CharField("video title",max_length=50)
	description = models.CharField("video description",max_length=150)
	tags = models.CharField("video tags",max_length=50)
	instructorid = models.ForeignKey("instructor id",Instructor, on_delete=models.CASCADE)
	courseid = models.ForeignKey("course id",Course, on_delete=models.CASCADE)



