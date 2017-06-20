#coding='utf-8'

'''
Created on 2017年6月5日

@author: liu

'''

from django import forms
from .models import *
#from django.contrib.admin import widgets as wg
#from django.forms.widgets import Widget
#from datetimewidget.widgets import DateWidget


class Emp(forms.ModelForm):
    class Meta:
        model=Empinfo
        fields ='__all__'
        # fields = ['username','email']       #指定显示的字段
        # exclude = ['username']      #不显示的字段
        widgets={
            'BirthDate':forms.DateInput(attrs={'type':'date',},format='%Y-%m-%d')
                #(usel10n = True,bootstrap_version=3,)
            }




class Education(forms.ModelForm):
    class Meta:
        model=Educationinfo
        fields ='__all__'
        # fields = ['username','email']       #指定显示的字段
        exclude = ['IDCardNo']      #不显示的字段
        widgets={
            'StartTime':forms.DateInput(attrs={'type':'date',},format='%Y-%m-%d'),
            'EndTime':forms.DateInput(attrs={'type': 'date'})
            }

class Course(forms.ModelForm):
    class Meta:
        model=Courseinfo
        fields ='__all__'
        # fields = ['username','email']       #指定显示的字段
        exclude = ['IDCardNo']      #不显示的字段
        widgets={
            'StartTime':forms.DateInput(attrs={'type':'date',},format='%Y-%m-%d'),
            'EndTime':forms.DateInput(attrs={'type': 'date'})
            }

class Job(forms.ModelForm):
    class Meta:
        model=Jobinfo
        fields ='__all__'
        # fields = ['username','email']       #指定显示的字段
        exclude = ['IDCardNo']      #不显示的字段
        widgets={
            'StartTime':forms.DateInput(attrs={'type':'date',},format='%Y-%m-%d'),
            'EndTime':forms.DateInput(attrs={'type': 'date'})
            }

class Family(forms.ModelForm):
    class Meta:
        model=Familyinfo
        fields ='__all__'
        # fields = ['username','email']       #指定显示的字段
        exclude = ['IDCardNo']      #不显示的字段
        widgets={
            'BirthDate':forms.DateInput(attrs={'type':'date',},format='%Y-%m-%d' )
                #(usel10n = True,bootstrap_version=3,)
            }
    #Educationinfo.StartTime=forms.fields