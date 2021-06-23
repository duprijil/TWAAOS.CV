from django.contrib import admin

# Register your models here.
from .models import CVData, CVExperience, CVSkills

admin.site.register(CVData)
admin.site.register(CVExperience)
admin.site.register(CVSkills)