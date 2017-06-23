from django.contrib import admin
from .models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

# Register your models here.

class empinfoAdmin(admin.ModelAdmin):
    list_display=('Name','Tel')

class userAdmin(admin.ModelAdmin):
    list_display = ('username','password','times')
admin.site.register(Empinfo,empinfoAdmin)
admin.site.register(user,userAdmin)