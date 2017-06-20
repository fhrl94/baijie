#coding=utf-8
'''
Created on 2017年6月5日

@author: liu
'''
from django.conf.urls import url

from information import views
from information import forms
from information import models

urlpatterns=[
    url(r'^home/$', views.home, name='home'),
    #flag是验证是否有修改ID
    url(r'^Form/(?P<ID>[\d]+)', views.Form, {
        'flag':False
    }, name='Form'),
    url(r'^FormBack/',views.FormBack,name='FormBack'),
    #PageManageOperate参数介绍：
    #ID一般是由URL中获取相应参数，如无设置为None           必须设置
    # operate 选填add、delete、edit，标明执行动作          必须设置
    #formtable 是form对象，指定对应表单                    必须设置
    #table 是数据表，对应存储的表单                        必须设置
    #titlename是表单的标题                                 必须设置
    #flag  True为多行信息表 FALSE为人员信息表 默认是True
    #name  下一个跳转视图名称 默认是form

    # 新增员工信息表无ID，设置为空
    url(r'^EmpPageAdd', views.PageManageOperate, {
        'operate': 'add',
        'table': models.Empinfo,
        'formtable': forms.Emp,
        'titlename': '员工基本信息填写',
        'flag': False,
        'ID': None,
    }, name='EmpPageAdd'),

    #编辑员工基本信息
    url(r'^EmpPageEdit/(?P<ID>[\d]+)', views.PageManageOperate, {
        'operate':'edit',
        'table': models.Empinfo,
        'formtable': forms.Emp,
        'titlename':'修改员工基本信息',
        'flag':False,
         }, name='EmpPageEdit'),


    #教育经历信息新增
    url(r'^EducationPageAdd/(?P<ID>[\d]+)',views.PageManageOperate,{
        'operate':'add',
        'table':models.Educationinfo,
        'formtable':forms.Education,
        'titlename':'教育经历信息填写',
    },name='EducationPageAdd'),
    # 教育经历信息修改
    url(r'^EducationPageEdit/(?P<ID>[\d]+)', views.PageManageOperate, {
        'operate': 'edit',
        'table': models.Educationinfo,
        'formtable': forms.Education,
        'titlename': '教育经历信息填写',
    }, name='EducationPageEdit'),
    # 教育经历信息删除
    url(r'^EducationPageDelete/(?P<ID>[\d]+)', views.PageManageOperate, {
        'operate': 'delete',
        'table': models.Educationinfo,
        'formtable': forms.Education,
        'titlename': '教育经历信息删除',
    }, name='EducationPageDelete'),

    # 培训经历信息新增
    url(r'^CoursePageAdd/(?P<ID>[\d]+)', views.PageManageOperate, {
        'operate': 'add',
        'table': models.Courseinfo,
        'formtable': forms.Course,
        'titlename': '培训经历信息填写',
    }, name='CoursePageAdd'),
    # 培训经历信息修改
    url(r'CoursePageEdit/(?P<ID>[\d]+)', views.PageManageOperate, {
        'operate': 'edit',
        'table': models.Courseinfo,
        'formtable': forms.Course,
        'titlename': '培训经历信息填写',
    }, name='CoursePageEdit'),
    # 培训经历信息删除
    url(r'CoursePageDelete/(?P<ID>[\d]+)', views.PageManageOperate, {
        'operate': 'delete',
        'table': models.Courseinfo,
        'formtable': forms.Course,
        'titlename': '培训经历信息删除',
    }, name='CoursePageDelete'),

    # 工作经历信息新增
    url(r'JobPageAdd/(?P<ID>[\d]+)', views.PageManageOperate, {
        'operate': 'add',
        'table': models.Jobinfo,
        'formtable': forms.Job,
        'titlename': '工作经历信息填写',
    }, name='JobPageAdd'),
    # 工作经历信息修改
    url(r'JobPageEdit/(?P<ID>[\d]+)', views.PageManageOperate, {
        'operate': 'edit',
        'table': models.Jobinfo,
        'formtable': forms.Job,
        'titlename': '工作经历信息填写',
    }, name='JobPageEdit'),
    # 工作经历信息删除
    url(r'JobPageDelete/(?P<ID>[\d]+)', views.PageManageOperate, {
        'operate': 'delete',
        'table': models.Jobinfo,
        'formtable': forms.Job,
        'titlename': '工作经历信息删除',
    }, name='JobPageDelete'),

    # 家庭成员信息新增
    url(r'FamilyPageAdd/(?P<ID>[\d]+)', views.PageManageOperate, {
        'operate': 'add',
        'table': models.Familyinfo,
        'formtable': forms.Family,
        'titlename': '家庭成员信息填写',
    }, name='FamilyPageAdd'),
    # 家庭成员信息修改
    url(r'FamilyPageEdit/(?P<ID>[\d]+)', views.PageManageOperate, {
        'operate': 'edit',
        'table': models.Familyinfo,
        'formtable': forms.Family,
        'titlename': '家庭成员信息填写',
    }, name='FamilyPageEdit'),
    # 家庭成员信息删除
    url(r'FamilyPageDelete/(?P<ID>[\d]+)', views.PageManageOperate, {
        'operate': 'delete',
        'table': models.Familyinfo,
        'formtable': forms.Family,
        'titlename': '家庭成员信息删除',
    }, name='FamilyPageDelete'),
    

    ]

# ID是empinfo中的pk，formtable是表格中的类对象，table是数据表,name是下个跳转URL名称，titlename是标题名称,flag是否是多行信息表
'''url(r'^EmpPageadd/',views.PageManage1,{
    'operate':'add',

}),'''
'''
   #无效待注释
   url(r'^EmpPage/', views.PageManage, {
       'ID':'0',
       'flag':False,
       'formtable': forms.Emp,
       'titlename':'基本信息表',
       }, name='EmpPage'),

   url(r'^EducationPage/(?P<ID>[\d]+)', views.PageManage, {
       'formtable': forms.Education,
       'name':'CoursePage',
       'titlename':'教育经历表'
       }, name='EducationPage'),

   url(r'^CoursePage/(?P<ID>[\d]+)', views.PageManage, {
       'formtable': forms.Course,
       'name':'JobPage',
       'titlename':'培训经历表'
       }, name='CoursePage'),

   url(r'^JobPage/(?P<ID>[\d]+)', views.PageManage, {
       'formtable': forms.Job,
       'name':'FamilyPage',
       'titlename':'工作经历表'
       }, name='JobPage'),

   url(r'^FamilyPage/(?P<ID>[\d]+)', views.PageManage, {
       'formtable': forms.Family,
       'name':'',
       'titlename':'家庭成员表'
       }, name='FamilyPage'),

   #url(r'^EducationPage/(?P<ID>[\d]+)',views.EducationPage,name='EducationPage'),
   #url(r'^CoursePage/(?P<ID>[\d]+)',views.CoursePage,name='CoursePage'),
   #url(r'^JobPage/(?P<ID>[\d]+)',views.JobPage,name='JobPage'),
   #url(r'^FamilyPage/(?P<ID>[\d]+)',views.FamilyPage,name='FamilyPage'),'''