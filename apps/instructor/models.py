from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Instructor(User):
    DOCTOR = "Dr."
    PROFESSOR = "Prof."
    MR = "Mr."
    MRS = "Mrs."
    TITLE_CHOICES = [
        (DOCTOR, _("Doctor")),
        (PROFESSOR, _("Professor")),
        (MR, _("Mr.")),
        (MRS, _("Mrs.")),
    ]
    title = models.CharField(choices=TITLE_CHOICES, max_length=16,
                             help_text=_("Instructor's Salutation"))

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"


class Course(models.Model):
    name = models.CharField(_("name"), max_length=120)
    instructor = models.ForeignKey(Instructor, verbose_name=_("instructor"),
                                   on_delete=models.CASCADE)
    description = models.TextField(_("description"))


class Video(models.Model):
    title = models.CharField(_("title"), max_length=120)
    description = models.TextField(_("description"))
    tags = ArrayField(models.CharField(max_length=200), blank=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE,
                                   verbose_name=_("instructor id"))
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE,
                                 verbose_name=_("course id"))
