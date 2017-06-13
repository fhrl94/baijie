#coding='utf-8'

'''
Created on 2017年6月5日

@author: liu

'''

from django import forms
from .models import *
from django.contrib.admin import widgets as wg
#from django.forms.widgets import Widget

class Emp(forms.ModelForm):
    class Meta:
        model=Empinfo
        fields ='__all__'
        # fields = ['username','email']       #指定显示的字段
        # exclude = ['username']      #不显示的字段
        widgets={
            'BirthDate':wg.AdminDateWidget()
            }
    


class Education(forms.ModelForm):
    class Meta:
        model=Educationinfo
        fields ='__all__'
        # fields = ['username','email']       #指定显示的字段
        exclude = ['IDCardNo']      #不显示的字段
    #Educationinfo.StartTime=forms.fields

class Course(forms.ModelForm):
    class Meta:
        model=Courseinfo
        fields ='__all__'
        # fields = ['username','email']       #指定显示的字段
        exclude = ['IDCardNo']      #不显示的字段
        
    #Educationinfo.StartTime=forms.fields

class Job(forms.ModelForm):
    class Meta:
        model=Jobinfo
        fields ='__all__'
        # fields = ['username','email']       #指定显示的字段
        exclude = ['IDCardNo']      #不显示的字段
    #Educationinfo.StartTime=forms.fields

class Family(forms.ModelForm):
    class Meta:
        model=Familyinfo
        fields ='__all__'
        # fields = ['username','email']       #指定显示的字段
        exclude = ['IDCardNo']      #不显示的字段
    #Educationinfo.StartTime=forms.fields