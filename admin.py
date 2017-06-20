from django.contrib import admin
from .models import Empinfo

# Register your models here.
class empinfoAdmin(admin.ModelAdmin):
    list_display=('Name','Tel')
admin.site.register(Empinfo,empinfoAdmin)
