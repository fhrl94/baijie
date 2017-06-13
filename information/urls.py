#coding=utf-8
'''
Created on 2017年6月5日

@author: liu
'''
from django.conf.urls import url, include
from . import views
from . import forms

urlpatterns=[
    url(r'^home/$',views.home,name='home'),
    #url(r'^EmpPage/',views.EmpPage,name='EmpPage'),
    #ID是empinfo中的pk，formtable是表格中的类对象，name是下个跳转URL名称，titlename是标题名称
    url(r'^EmpPage/',views.PageManage,{
        'ID':'0',
        'flag':False,
        'formtable':forms.Emp,
        'name':'EducationPage',
        'titlename':'教育经历表'
        },name='EmpPage'),

    url(r'^EducationPage/(?P<ID>[\d]+)',views.PageManage,{
        'formtable':forms.Education,
        'name':'CoursePage',
        'titlename':'教育经历表'
        },name='EducationPage'),
    
    url(r'^CoursePage/(?P<ID>[\d]+)',views.PageManage,{
        'formtable':forms.Course,
        'name':'JobPage',
        'titlename':'培训经历表'
        },name='CoursePage'),      
             
    url(r'^JobPage/(?P<ID>[\d]+)',views.PageManage,{
        'formtable':forms.Job,
        'name':'FamilyPage',
        'titlename':'工作经历表'
        },name='JobPage'),                   

    url(r'^FamilyPage/(?P<ID>[\d]+)',views.PageManage,{
        'formtable':forms.Family,
        'name':'',
        'titlename':'家庭成员表'
        },name='FamilyPage'),    
             
    #url(r'^EducationPage/(?P<ID>[\d]+)',views.EducationPage,name='EducationPage'),
    #url(r'^CoursePage/(?P<ID>[\d]+)',views.CoursePage,name='CoursePage'),
    #url(r'^JobPage/(?P<ID>[\d]+)',views.JobPage,name='JobPage'),
    #url(r'^FamilyPage/(?P<ID>[\d]+)',views.FamilyPage,name='FamilyPage'),
    ]


    


