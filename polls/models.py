
# Create your models here.
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

import datetime

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

class CVData(models.Model):
    name = models.CharField(max_length=256)
    surrname = models.CharField(max_length=256)
    profession = models.CharField(max_length=256)
    email = models.EmailField(max_length = 256, default="example@examp.ex")
    phone_number = PhoneNumberField(default="+4012345678")

    def __str__(self):
        return self.name

class CVExperience(models.Model):
    company_name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    start_year = models.IntegerField(choices=year_choices())
    end_year = models.IntegerField(choices=year_choices())

class CVSkills(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
