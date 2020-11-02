from django.contrib import admin
from . import models
# Register your models here.

class TestAdmin(admin.ModelAdmin):
    list_display = ["question","marks","package"]
    list_filter = ["package","marks"]
    search_fields = ["question","package__name"] 



admin.site.register(models.Test,TestAdmin)