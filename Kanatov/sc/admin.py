from django.contrib import admin
from .models import *
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]
    prepopulated_fields = {'slug': ('name',)}


class LecturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'patronymic']
    list_display_links = ['name']



class SubjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subject._meta.fields]


class GroupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Group._meta.fields]



class StudentScoresAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudentScores._meta.fields]


class FacultetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Facultet._meta.fields]

admin.site.register(Student, StudentAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(StudentScores, StudentScoresAdmin)
admin.site.register(Facultet, FacultetAdmin)
# Register your models here.
