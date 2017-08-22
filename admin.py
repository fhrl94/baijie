from django.contrib import admin
from .views import *

# Register your models here.

class empinfoAdmin(admin.ModelAdmin):
    list_display=('id','Name','Tel')
    search_fields=('Name',)

    actions = ['FormAdmin','FormPrint','Excelroster']

    def FormAdmin(modeladmin,request,queryset):
        return Form(request,queryset.get().id)

    def FormPrint(modeladmin,request,queryset):
        print(queryset.values('id'))
        return pdfs(request,queryset.values('id'))

    def Excelroster(modeladmin,request,queryset):
        # print(queryset.values('id'))
        return excel(request,queryset.values('id'))


    FormAdmin.short_description='页面查看'
    FormPrint.short_description='页面信息下载'
    Excelroster.short_description='花名册excel下载'
#
# class userAdmin(admin.ModelAdmin):
#     list_display = ('username','password','times')
admin.site.register(Empinfo,empinfoAdmin,)
# admin.site.register(user,userAdmin)