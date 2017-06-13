# coding=utf-8
from django.db import models
from django.core.validators import RegexValidator



# Create your models here.
class Empinfo(models.Model):
    Sex_choices=(
         (None,u'请选择'),
        (1,u'男'),
        (2,u'女'),
        )
    MaritalStatus_choice=(
        (None,u'请选择'),
        (1,u'已婚'),
        (2,u'未婚')
        )
    
    Name=models.CharField('姓名',max_length=20)
    Sex=models.IntegerField('性别',choices=Sex_choices)
    Nationality=models.IntegerField('民族')
    BirthDate=models.DateField('出生日期',)#help_text='格式规范1970-01-01'
    NativePlace=models.CharField('籍贯',max_length=50)
    PoliticsStatus=models.IntegerField('政治面貌')
    MaritalStatus=models.IntegerField('婚姻状况',choices=MaritalStatus_choice)
    Tel=models.CharField('联系电话',max_length=11,validators=[RegexValidator(r'^^[\d]{11}')],unique=True)
    Email=models.EmailField('电子邮箱',max_length=50,unique=True)
    IDCardNo=models.CharField('身份证号',max_length=18,validators=[RegexValidator(r'^[\d]{17}[x,X,\d]{1}')],unique=True)
    EmergencyContactName=models.CharField('紧急联系人姓名',max_length=20)
    EmergencyContactRelation=models.IntegerField('与紧急联系人关系')
    EmergencyContactTel=models.CharField('紧急联系电话',max_length=11,validators=[RegexValidator(r'^[\d]{11}')])
    CurrentResidentialAddress=models.CharField('现居住地址',max_length=255)
    HomeAddress=models.CharField('家庭地址',max_length=255)
    IDAddress=models.CharField('身份证地址',max_length=255)
    
    def __str__(self):
        return self.IDCardNo    
    
class Educationinfo(models.Model):
    UniversityName=models.CharField('学校全称',max_length=50)
    StartTime=models.DateField('开始时间',)
    EndTime=models.DateField('结束时间')
    Profession=models.CharField('专业',max_length=50)
    EducationBackground=models.IntegerField('学历')
    EducationNature=models.CharField('学习性质',max_length=50)
    DiplomaName=models.CharField('所学证书或奖励',max_length=50)
    IDCardNo=models.ForeignKey("Empinfo",on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.id)
    
class Courseinfo(models.Model):
    TrainingName=models.CharField('培训机构名称',max_length=50)
    StartTime=models.DateField('开始时间',)
    EndTime=models.DateField('结束时间')
    CourseLength=models.IntegerField('培训时长',)
    CoursePlace=models.CharField('培训地点',max_length=50)
    DiplomaName=models.CharField('证书名称',max_length=50)
    IDCardNo=models.ForeignKey("Empinfo",on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.id)

class Jobinfo(models.Model):
    CompanyName=models.CharField('公司全称',max_length=50)
    StartTime=models.DateField('开始时间',)
    EndTime=models.DateField('结束时间')
    JobPosition=models.CharField('工作职位',max_length=50)
    JobDuties=models.CharField('工作内容',max_length=50)
    Certifier=models.CharField('证明人',max_length=50)
    CertifierDuty=models.CharField('证明人职务',max_length=20)
    CertifierTel=models.CharField('证明人电话',max_length=11,validators=[RegexValidator(r'^[\d]{11}')])
    IDCardNo=models.ForeignKey("Empinfo",on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.id)

class Familyinfo(models.Model):
    Name=models.CharField('姓名',max_length=50)
    Relation=models.IntegerField('与本人关系',)
    BirthDate=models.DateField('出生日期')
    WorkUnit=models.IntegerField('工作单位',)
    Duty=models.CharField('职务',max_length=50)
    Tel=models.CharField('联系电话',max_length=11,validators=[RegexValidator(r'^[\d]{11}')])
    IDCardNo=models.ForeignKey("Empinfo",on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.id)