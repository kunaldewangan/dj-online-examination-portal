from django.contrib import admin
from . import models
from django.contrib.admin.options import ModelAdmin

# Register your models here.


class PackageAdmin(ModelAdmin):
    list_display = ["name","no_of_Q","start_time","end_time","visibility","q_visibility","total_marks","duration"]
    list_filter = ["name","visibility","q_visibility","no_of_Q","total_marks"]
    search_fields = ["name","description","start_time","end_time"]

class PackageStudentAdmin(ModelAdmin):
    list_display = ["student","package","marks","submission"]
    list_filter =  ["package","student__username","submission"]
    search_fields = ["package__name","marks","student__username"]





admin.site.register(models.Package,PackageAdmin)
admin.site.register(models.PackageStudent,PackageStudentAdmin)