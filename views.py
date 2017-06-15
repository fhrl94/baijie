from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
from . import models
from django.core.urlresolvers import reverse


# Create your views here.
def home(request):
    return HttpResponse(u'你好')

def Form(request,ID,flag=True):
    if (request.session.get('id')!=int(ID) and flag):
        return HttpResponse(u'请勿更改URL')
    empform=models.Empinfo.objects.filter(id=ID)
    educationform=models.Educationinfo.objects.filter(IDCardNo=ID).order_by('-StartTime')[:2]
    courseform=models.Courseinfo.objects.filter(IDCardNo=ID).order_by('-StartTime')[:2]
    jobform = models.Jobinfo.objects.filter(IDCardNo=ID).order_by('-StartTime')[:3]
    familyform = models.Familyinfo.objects.filter(IDCardNo=ID)
    return  render(request,'information/info.html',
                   {'empform':empform,
                    'educationform':educationform,
                    'courseform':courseform,
                    'jobform':jobform,
                    'familyform':familyform,
                    'ID':ID,
                    })



def PageManage(request,ID,formtable,titlename,name='form',flag=True):
    #ID是empinfo中的pk，formtable是表格中的类对象，name是下个跳转URL名称，titlename是标题名称
    '''if (request.session.get('id')!=int(ID) and flag):
        return HttpResponse(u'请勿更改URL')'''
    if request.method=='POST':
        form=formtable(request.POST)
        if form.is_valid():
            #form.save()
            #form.IDCardNo=id
            if (flag!=True):
                form.save()
                ID = models.Empinfo.objects.filter(IDCardNo=form.cleaned_data['IDCardNo']).get().id
                request.session['id'] = ID
            else:
                new_Educationinfo=form.save(commit=False)
                new_Educationinfo.IDCardNo=models.Empinfo.objects.filter(id=ID).get()
                new_Educationinfo.save()
            if (name!=''):
                return HttpResponseRedirect(reverse(name,kwargs={"ID":ID}))
            return HttpResponseRedirect(reverse("home",kwargs={}))
            #reverse
    else:
        form=formtable()
    return render(request, 'information/index.html',{'title':titlename,'form':form})


def PageManageOperate(request,ID,formtable,table,titlename,operate='add',name='Form',flag=True):
    #ID是empinfo中的pk，formtable是表格中的类对象，table是数据表,name是下个跳转URL名称，titlename是标题名称,flag是否是多行信息表
    '''if (request.session.get('id')!=int(ID) and flag):
        return HttpResponse(u'请勿更改URL')'''
    if operate=='add':
        if request.method=='POST':
            form=formtable(request.POST)
            if form.is_valid():
                #form.save()
                #form.IDCardNo=id
                if (flag!=True):
                    form.save()
                    ID = models.Empinfo.objects.filter(IDCardNo=form.cleaned_data['IDCardNo']).get().id
                    request.session['id'] = ID
                else:
                    new_Educationinfo=form.save(commit=False)
                    new_Educationinfo.IDCardNo=models.Empinfo.objects.filter(id=ID).get()
                    new_Educationinfo.save()
                #if (name!=''):
                return HttpResponseRedirect(reverse(name,kwargs={"ID":ID}))
                #return HttpResponseRedirect(reverse("home",kwargs={}))
                #reverse
        else:
            form=formtable()
        return render(request, 'information/index.html', {'title': titlename, 'form': form})

    #基本信息表无删除功能
    elif operate=='delete' and flag==True :
        pkID=table.objects.filter(pk=ID).get().IDCardNo.id
        table.objects.filter(pk=ID).delete()
        return HttpResponseRedirect(reverse(name, kwargs={"ID": pkID}))

    #表单数据回填
    elif operate=='edit':
        obj = table.objects.filter(pk=ID).get()
        if request.method=='POST':
            form=formtable(request.POST,instance=obj,)
            if form.is_valid():
                form.save()
                #form.IDCardNo=id
                if (flag!=True):
                    ID = models.Empinfo.objects.filter(IDCardNo=form.cleaned_data['IDCardNo']).get().id
                else:
                    ID=table.objects.filter(id=ID).get().IDCardNo.id
                #if (name!=''):
                return HttpResponseRedirect(reverse(name,kwargs={"ID":ID}))
                #return HttpResponseRedirect(reverse("home",kwargs={}))
                #reverse
        else:
            form=formtable(instance=obj)
        return render(request, 'information/index.html', {'title': titlename, 'form': form})

    #其余情况报错（404或其他）


'''
def EmpPage(request):
    if request.method=='POST':
        form=Emp(request.POST)
        if form.is_valid():
            #name=form.cleaned_data['name']
            #tel=form.cleaned_data['tel']
            #return HttpResponse(str(name)+str(tel))
            form.save()
            id=models.Empinfo.objects.filter(IDCardNo=form.cleaned_data['IDCardNo']).get().id
            request.session['id']=id
            request.session.set_expiry(7200)
            #return HttpResponseRedirect('/information/Educationinfo/')
            return HttpResponseRedirect(reverse("EducationPage",kwargs={"ID":id}))
            #return HttpResponse(u'你好')
    else:
        form=Emp()
    return render(request,  'information/index.html',{'title':'基本信息表','form':form})

def EducationPage(request,ID):
    if (request.session.get('id')!=int(ID)):
        return HttpResponse(u'请勿更改URL')
    if request.method=='POST':
        form=Education(request.POST)
        if form.is_valid():
            #form.save()
            #form.IDCardNo=id
            new_Educationinfo=form.save(commit=False)
            new_Educationinfo.IDCardNo=models.Empinfo.objects.filter(id=ID).get()
            new_Educationinfo.save()
            return HttpResponseRedirect(reverse("CoursePage",kwargs={"ID":ID}))
            #reverse
    else:
        form=Education()
    return render(request, 'information/index.html',{'title':'教育经历表','form':form})

def CoursePage(request,ID):
    if (request.session.get('id')!=int(ID)):
        return HttpResponse(u'请勿更改URL')
    if request.method=='POST':
        form=Course(request.POST)
        if form.is_valid():
            #form.save()
            #form.IDCardNo=id
            new_Courseinfo=form.save(commit=False)
            new_Courseinfo.IDCardNo=models.Empinfo.objects.filter(id=ID).get()
            new_Courseinfo.save()
            return HttpResponseRedirect(reverse("JobPage",kwargs={"ID":ID}))
            #reverse
    else:
        form=Course()
    return render(request, 'information/index.html',{'title':'培训经历表','form':form})

def JobPage(request,ID):
    if (request.session.get('id')!=int(ID)):
        return HttpResponse(u'请勿更改URL')
    if request.method=='POST':
        form=Job(request.POST)
        if form.is_valid():
            #form.save()
            #form.IDCardNo=id
            new_Jobinfo=form.save(commit=False)
            new_Jobinfo.IDCardNo=models.Empinfo.objects.filter(id=ID).get()
            new_Jobinfo.save()
            return HttpResponseRedirect(reverse("FamilyPage",kwargs={"ID":ID}))
            #reverse
    else:
        form=Job()
    return render(request, 'information/index.html',{'title':'工作经历表','form':form})

def FamilyPage(request,ID):
    if (request.session.get('id')!=int(ID)):
        return HttpResponse(u'请勿更改URL')
    if request.method=='POST':
        form=Family(request.POST)
        if form.is_valid():
            #form.save()
            #form.IDCardNo=id
            new_Familyinfo=form.save(commit=False)
            new_Familyinfo.IDCardNo=models.Empinfo.objects.filter(id=ID).get()
            new_Familyinfo.save()
            return HttpResponseRedirect(reverse("home",kwargs={}))
            #reverse
    else:
        form=Family()
    return render(request, 'information/index.html',{'title':'家庭成员表','form':form})
'''


def FamilyPage(request,ID):
    if (request.session.get('id')!=int(ID)):
        return HttpResponse(u'请勿更改URL')
    if request.method=='POST':
        form=Family(request.POST,)
        if form.is_valid():
            #form.save()
            #form.IDCardNo=id
            new_Familyinfo=form.save(commit=False)
            new_Familyinfo.IDCardNo=models.Empinfo.objects.filter(id=ID).get()
            new_Familyinfo.save()
            return HttpResponseRedirect(reverse("home",kwargs={}))
            #reverse
    else:
        form=Family()
    return render(request, 'information/index.html',{'title':'家庭成员表','form':form})