# -*- coding: utf-8 -*-
import os
import time

import xlwt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils.http import urlquote

from .forms import *
from . import models
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
import pdfkit
import sys
from django.http import StreamingHttpResponse
import zipfile
import glob

# 文件下载生成器
def file_iterator(file_name, chunk_size=512):
    with open(file_name, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
# Create your views here.
def home(request):
    return HttpResponse(u'你好')

@login_required(login_url='login')
def excel(request,DictIDS):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('人员基本信息')
    ws1 = wb.add_sheet('家庭成员')
    dateFormat = xlwt.XFStyle()
    dateFormat.num_format_str = 'yyyy/mm/dd'
    Empcolumn=['Name','get_Sex_display','BirthDate','IDCardNo','Tel','Email','CurrentResidentialAddress','HomeAddress',
               'EmergencyContactName', 'get_EmergencyContactRelation_display', 'EmergencyContactTel',]
    Empcolumnstyle=[None,None,dateFormat,None,None,None,None,None,None,None,None,]
    EFirst=['序号','姓名','性别','出生日期','身份证号','手机号码','电子邮箱','现居住地址','家庭地址',
            '紧急联系人姓名','与紧急联系人关系','紧急联系电话','毕业学校','学历','专业','学习性质','毕业时间',]
    Educolumn=['UniversityName','get_EducationBackground_display','Profession','get_EducationNature_display'
        ,'EndTime',]
    Educolumnstyle=[None,None,None,None,dateFormat]
    FFirst=['序号','身份证号','姓名','与本人关系','出生日期','工作单位','职务','电话']
    Fcolumn=['Name','get_Relation_display','BirthDate','WorkUnit','Duty','Tel',]
    Fcolumnstyle=[None,None,dateFormat,None,None,None,]
    l = len(Empcolumn)
    ws.col(3).width=256*11
    ws.col(4).width = 256 * 21
    ws.col(5).width = 256 * 13
    ws.col(6).width = 256 * 19
    ws.col(7).width = 256 * 22
    ws.col(8).width = 256 * 15
    ws.col(9).width = 256 * 20
    ws.col(11).width = 256 * 13
    ws.col(12).width=256*13
    ws.col(14).width=256*13
    ws.col(16).width=256*11
    ws1.col(1).width = 256 * 21
    ws1.col(4).width = 256 * 11
    ws1.col(7).width = 256 * 13
    for i in range(len(EFirst)):
        ws.write(0,i,EFirst[i])
    for i in range(len(FFirst)):
        ws1.write(0,i,FFirst[i])
    Fi=0
    for i,Dist in enumerate(DictIDS):
        # 待review
        Query=Empinfo.objects.filter(id=Dist['id']).get()
        ws.write(i + 1, 0, i + 1)
        for j, col in enumerate(Empcolumn):
            # print(Query.getcol(col))
            if Empcolumnstyle[j]==None:
                ws.write(i + 1, j + 1, Query.getcol(col))
            else:
                ws.write(i + 1, j + 1, Query.getcol(col), Empcolumnstyle[j])
        EQuery=Query.educationinfo_set.order_by('EducationBackground')[:1]
        # print(EQuery)
        if EQuery:
            for j, col in enumerate(Educolumn):
                # print(query.get(col))
                # print('______')
                # print(i+1,l+2,EQuery.get().getcol(col), Educolumnstyle[j])
                if Educolumnstyle[j]==None:
                    ws.write(i + 1, l + 1+j, EQuery.get().getcol(col))
                else:
                    ws.write(i + 1, l + 1+j, EQuery.get().getcol(col), Educolumnstyle[j])
        FQuery = Query.familyinfo_set.order_by('id')
        # print(type(FQuery))
        for i,query in enumerate(FQuery):
            ws1.write(Fi + 1, 0, i + 1)
            ws1.write(Fi + 1, 1, Query.getcol('IDCardNo'))
            # print(dir(query))
            for j,col in enumerate(Fcolumn):
                # print(query.get(col))
                if Fcolumnstyle[j]==None:
                    ws1.write(Fi + 1, j + 2, query.getcol(col))
                else:
                    ws1.write(Fi + 1, j + 2, query.getcol(col),Fcolumnstyle[j])
                # print(query.get(col))
            Fi=Fi+1

    wb.save(sys.path[0] + r'/information/Excel/'+'cs.xls')
    the_file_name = sys.path[0] + r'/information/Excel/cs.xls'
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}{1}.{2}"'.format(
        urlquote('员工信息表'),
        (time.strftime('%Y-%m-%d_%H-%M-%S',
                       time.localtime(
                           time.time()))), 'xls')
    return response

@login_required(login_url='login')
def pdfs(request,DictIDS):
    config = pdfkit.configuration(wkhtmltopdf=sys.path[0] + '/information/static/wkhtmltopdf-0.8.3.exe')
    # string=bytes("",encoding='utf-8')
    dirlist=sys.path[0] + r'/information/temp/'
    # 删除上一次生成的所有文件
    for delfile in os.listdir(dirlist):
        os.remove(sys.path[0] + r'/information/temp/'+delfile)
    for Dist in DictIDS:
        # 生成当前时间的文档（防止重复），再根据ID获取文件所在页面字符，然后生成PDF文档，再改名（避免中文名称PDF生成错误）
        str=sys.path[0] + '/information/temp/'+(time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(
                           time.time())))+'.pdf'
        # print(str)
        pdfkit.from_string(Form(request,Dist['id'],True,True).getvalue().decode('utf-8'),
                           str,configuration=config, )
        os.rename(str,sys.path[0] + '/information/temp/' + models.Empinfo.objects.filter(id=Dist['id']).get().Name + '.pdf')
    # 获取文件路径列表,如果存在test.zip则清除
    files=glob.glob(sys.path[0] + r'/information/temp/*')
    if os.path.exists(sys.path[0]+r'/information/test.zip'):
        os.remove(sys.path[0]+r'/information/test.zip')
    f = zipfile.ZipFile(sys.path[0]+r'/information/test.zip', 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        f.write(file,os.path.basename(file))
    f.close()
    # 生成文件
    the_file_name = sys.path[0]+r'/information/test.zip'
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}{1}.{2}"'.format(
        urlquote('员工信息表'),
        (time.strftime('%Y-%m-%d_%H-%M-%S',
                       time.localtime(
                           time.time()))), 'zip')
    return response

@login_required(login_url='login')
def pdf(request,ID):
    config = pdfkit.configuration(wkhtmltopdf=sys.path[0]+'/information/static/wkhtmltopdf-0.8.3.exe')
    # file=open(sys.path[0]+r'/information/temp.html','wb')
    # file.write(Form(request,ID,True,True).getvalue())
    # file.close()
    pdfkit.from_string(Form(request,ID,True,True).getvalue().decode('utf-8'),
                       sys.path[0]+'/information/out.pdf',configuration = config,)
    the_file_name = sys.path[0]+'/information/out.pdf'
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}{1}.{2}"'.format(urlquote(models.Empinfo.objects.filter(id=ID).get().Name),
                                                                                (time.strftime('%Y-%m-%d_%H-%M-%S',
                                                                                               time.localtime(
                                                                                                   time.time()))),'pdf')
    return response

def Index(request):
    logout(request)
    if request.method == 'POST':
        form = index(request.POST)
        if form.is_valid():
            form.save()
            ID = models.Empinfo.objects.filter(Tel=form.cleaned_data['Tel']).get().id
            request.session['id'] = ID
            # 设置session 过期时间60*60秒
            request.session.set_expiry(60 * 60)
            return HttpResponseRedirect(reverse('Form', kwargs={"ID": ID}))
    else:
        form = index()
    return render(request, 'information/index.html', {'title': u'欢迎你加入百捷集团', 'form': form,'ID':0,})



def my_login(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            un=form.cleaned_data['username']
            pw=form.cleaned_data['password']
            user=authenticate(request,username=un,password=pw)
            if user is not None:
                login(request,user)
                # request.session['_auth_user_id']为用户ID
                return HttpResponseRedirect(reverse(FormList))
            else:
                return render(request, 'information/index.html', {'title': u'密码错误请重新登录', 'form': form})
    else:
        form = loginform()
    return render(request,'information/index.html',{'title':u'请登录','form':form})

def my_logout(request,body):
    logout(request)
    return  HttpResponse(body)

@login_required(login_url='login')
def FormList(request):
    forms=models.Empinfo.objects.all().values('pk','Name','Tel','IDCardNo')
    return render(request,'information/FormList.html',{'forms':forms})

def Form(request,ID,status=False,flag=False):
    #个人信息表单页
    #ID是人员信息表中的PK值
    # status确定是否打印
    if (request.session.get('id')!=int(ID) and request.session.get('_auth_user_id')==None and flag==False):
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
                    'status':status
                    })



def PageManageOperate(request, ID, formtable, table, titlename, operate, name='Form', status=True):
    #PageManageOperate参数介绍：
    #ID一般是由URL中获取相应参数，如无设置为None           必须设置
    # operate 选填add、delete、edit，标明执行动作          必须设置
    #formtable 是form对象，指定对应表单                    必须设置
    #table 是数据表，对应存储的表单                        必须设置
    #titlename是表单的标题                                 必须设置
    #status  True为多行信息表 FALSE为人员信息表 默认是True
    #name  下一个跳转视图名称 默认是form
    if operate=='add':
        if (ID != None and request.session.get('id') != int(ID) and request.session.get('_auth_user_id')==None):
            return HttpResponse(u'请勿更改URL')
        if request.method=='POST':
            form=formtable(request.POST)
            if form.is_valid():
                #form.save()
                #form.IDCardNo=id
                # if (status!=True):
                #     form.save()
                #     ID = models.Empinfo.objects.filter(IDCardNo=form.cleaned_data['IDCardNo']).get().id
                #     # request.session['id'] = ID
                #     # #设置session 过期时间60*60秒
                #     # request.session.set_expiry(60*60)
                # else:
                new_info=form.save(commit=False)
                new_info.IDCardNo=models.Empinfo.objects.filter(id=ID).get()
                new_info.save()
                #if (name!=''):
                return HttpResponseRedirect(reverse(name,kwargs={"ID":ID}))
                #return HttpResponseRedirect(reverse("home",kwargs={}))
                #reverse
        else:
            form=formtable()
        return render(request, 'information/index.html', {'title': titlename, 'form': form,'ID':ID})

    #基本信息表无删除功能
    elif operate=='delete' and status==True :
        # pkID=table.objects.filter(pk=ID).get().IDCardNo.id
        obj = table.objects.filter(pk=ID).get()
        pkID=obj.IDCardNo.id
        if (request.session.get('id') != obj.IDCardNo.id and request.session.get('_auth_user_id')==None):
            return HttpResponse(u'请勿更改URL')
        table.objects.filter(pk=ID).delete()
        return HttpResponseRedirect(reverse(name, kwargs={"ID": pkID}))

    #表单数据回填
    elif operate=='edit':
        obj = table.objects.filter(pk=ID).get()
        if (request.session.get('id') != obj.id and request.session.get('_auth_user_id')==None
            and request.session.get('id') != obj.IDCardNo.id):
            return HttpResponse(u'请勿更改URL')
        if request.method=='POST':
            form=formtable(request.POST,instance=obj,)
            if form.is_valid():
                form.save()
                #form.IDCardNo=id
                if (status!=True):
                    ID = obj.id
                else:
                    ID=obj.IDCardNo.id
                #if (name!=''):
                return HttpResponseRedirect(reverse(name,kwargs={"ID":ID}))
                #return HttpResponseRedirect(reverse("home",kwargs={}))
                #reverse
        else:
            form=formtable(instance=obj)
            if (status != True):
                ID = obj.id
            else:
                ID = obj.IDCardNo.id
        return render(request, 'information/index.html', {'title': titlename, 'form': form,'ID':ID,})

    #其余情况报错（404或其他）

def FormBack(request,ID):
    if (request.session.get('id')!=int(ID) and request.session.get('_auth_user_id')==None):
        return HttpResponse(u'请勿更改URL')
    return HttpResponseRedirect(reverse('Form', kwargs={"ID": ID}))


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

'''
def PageManage(request,ID,formtable,titlename,name='form',flag=True):
    #ID是empinfo中的pk，formtable是表格中的类对象，name是下个跳转URL名称，titlename是标题名称
    if (request.session.get('id')!=int(ID) and flag):
        return HttpResponse(u'请勿更改URL')
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
'''
# 登录视图
# def login(request):
#     if request.method=='POST':
#         form=loginform(request.POST)
#         if form.is_valid():
#             un=form.cleaned_data['username']
#             pw=form.cleaned_data['password']
#             try:
#                 ob=models.user.objects.filter(username=un).get()
#             except :
#                 ob=None
#             if ob :#
#                 if ob.password==pw and ob.times<5:
#                     request.session['user']=un
#                     ob.times=0
#                     ob.save()
#                     return HttpResponse(u'登录成功')
#                 elif ob.times>=5:
#                     return HttpResponse(u'账户已冻结')
#                 ob.times=ob.times+1
#                 ob.save()
#
#         return render(request,'information/index.html',{'title':u'账户请登录','form':form})
#     else:
#         form = loginform()
#     return render(request,'information/index.html',{'title':u'请登录','form':form})

# def result(request):
#     logout(request)
#     return HttpResponse(u'提交成功')

# @login_required(login_url='login')
# def FormPrint(request,ID,status,flag):
#     return Form(request, ID, status=status, flag=flag)