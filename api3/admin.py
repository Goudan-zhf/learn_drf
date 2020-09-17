from django.contrib import admin

# Register your models here.
from api3 import models
admin.site.register(models.Course)
admin.site.register(models.Teacher)
admin.site.register(models.TeacherDetail)
admin.site.register(models.School)