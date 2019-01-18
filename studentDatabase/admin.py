from django.contrib import admin

from .models import Student, StudentFather, StudentMother
# Register your models here.

admin.site.register(Student)
admin.site.register(StudentFather)
admin.site.register(StudentMother)