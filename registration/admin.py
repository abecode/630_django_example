from django.contrib import admin
from .models import Student, Professor, Course, Enrollment
# Register your models here.
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Enrollment)
    
