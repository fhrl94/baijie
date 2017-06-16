# coding=utf-8
from django.db import models
from django.core.validators import RegexValidator

EmergencyContactRelation_choice = (
    (None, u'请选择'),
    (1, u'本人'),
    (2, u'户主'),
    (3, u'小集体户户主'),
    (10, u'配偶'),
    (11, u'夫'),
    (12, u'妻'),
    (20, u'子'),
    (21, u'独生子'),
    (22, u'长子'),
    (23, u'次子'),
    (24, u'三子'),
    (25, u'四子'),
    (26, u'五子'),
    (27, u'养子或继子'),
    (28, u'女婿'),
    (29, u'其他子'),
    (30, u'女'),
    (31, u'独生子'),
    (32, u'长女'),
    (33, u'二女'),
    (34, u'三女'),
    (35, u'四女'),
    (36, u'五女'),
    (37, u'养女'),
    (38, u'儿媳'),
    (39, u'其他女儿'),
    (40, u'孙子、孙女或外孙子、外孙女'),
    (41, u'孙子'),
    (42, u'孙女'),
    (43, u'外孙子'),
    (44, u'外孙女'),
    (45, u'孙媳妇或外孙媳妇'),
    (46, u'孙女婿或外孙女婿'),
    (47, u'曾孙子或外曾孙子'),
    (48, u'曾孙女或外曾孙女'),
    (49, u'其他孙子、孙女或外孙子、外孙女'),
    (50, u'父母'),
    (51, u'父亲'),
    (52, u'母亲'),
    (53, u'公公'),
    (54, u'婆婆'),
    (55, u'岳父'),
    (56, u'岳母'),
    (57, u'继父或养父'),
    (58, u'继母或养母'),
    (59, u'其他父母关系'),
    (60, u'祖父母或外祖父母'),
    (61, u'祖父'),
    (62, u'祖母'),
    (63, u'外祖父'),
    (64, u'外祖母'),
    (65, u'配偶的祖父母或外祖父母'),
    (66, u'曾祖父'),
    (67, u'曾祖母'),
    (68, u'配偶的曾祖父母'),
    (69, u'其他祖父母或外祖父母关系'),
    (70, u'兄弟姐妹'),
    (71, u'兄'),
    (72, u'嫂'),
    (73, u'弟'),
    (74, u'弟媳'),
    (75, u'姐姐'),
    (76, u'姐夫'),
    (77, u'妹妹'),
    (78, u'妹夫'),
    (79, u'其他兄弟姐妹'),
    (80, u'其他'),
    (81, u'伯父'),
    (82, u'伯母'),
    (83, u'叔父'),
    (84, u'婶母'),
    (85, u'舅父'),
    (86, u'舅母'),
    (87, u'姨父'),
    (88, u'姨母'),
    (89, u'姑父'),
    (90, u'姑母'),
    (91, u'堂兄弟、堂姐妹'),
    (92, u'表兄弟、表姐妹'),
    (93, u'侄子'),
    (94, u'侄女'),
    (95, u'外甥'),
    (96, u'外甥女'),
    (97, u'其他亲属'),
    (98, u'保姆'),
    (99, u'非亲属'),
)

# Create your models here.
class Empinfo(models.Model):
    Sex_choices=(
        (None, u'请选择'),
        (1, u'男性'),
        (2, u'女性'),
        (9, u'未说明'),
    )
    MaritalStatus_choice=(
        (None, u'请选择'),
        (1, u'未婚'),
        (2, u'已婚'),
        (4, u'离婚'),
        (9, u'其它'),
    )
    Nationality_choice=(
        (None, u'请选择'),
        (1, u'汉族'),
        (2, u'蒙古族'),
        (3, u'回族'),
        (4, u'藏族'),
        (5, u'维吾尔族'),
        (6, u'苗族'),
        (7, u'彝族'),
        (8, u'壮族'),
        (9, u'布依族'),
        (10, u'朝鲜族'),
        (11, u'满族'),
        (12, u'侗族'),
        (13, u'瑶族'),
        (14, u'白族'),
        (15, u'土家族'),
        (16, u'哈尼族'),
        (17, u'哈萨克族'),
        (18, u'傣族'),
        (19, u'黎族'),
        (20, u'傈僳族'),
        (21, u'佤族'),
        (22, u'畲族'),
        (23, u'高山族'),
        (24, u'拉祜族'),
        (25, u'水族'),
        (26, u'东乡族'),
        (27, u'纳西族'),
        (28, u'景颇族'),
        (29, u'柯尔克孜族'),
        (30, u'土族'),
        (31, u'达斡尔族'),
        (32, u'仫佬族'),
        (33, u'羌族'),
        (34, u'布朗族'),
        (35, u'撒拉族'),
        (36, u'毛南族'),
        (37, u'仡佬族'),
        (38, u'锡伯族'),
        (39, u'阿昌族'),
        (40, u'普米族'),
        (41, u'塔吉克族'),
        (42, u'怒族'),
        (43, u'乌孜别克族'),
        (44, u'俄罗斯族'),
        (45, u'鄂温克族'),
        (46, u'德昂族'),
        (47, u'保安族'),
        (48, u'裕固族'),
        (49, u'京族'),
        (50, u'塔塔尔族'),
        (51, u'独龙族'),
        (52, u'鄂伦春族'),
        (53, u'赫哲族'),
        (54, u'门巴族'),
        (55, u'珞巴族'),
        (56, u'基诺族'),
    )
    PoliticsStatus_choice=(
        (None, u'请选择'),
        (1, u'中国共产党党员'),
        (2, u'中国共产党预备党员'),
        (3, u'中国共产主义青年团团员'),
        (4, u'中国国民党革命委员会会员'),
        (5, u'中国民主同盟盟员'),
        (6, u'中国民主建国会会员'),
        (7, u'中国民主促进会会员'),
        (8, u'中国农工民主党党员'),
        (9, u'中国致公党党员'),
        (10, u'九三学社社员'),
        (11, u'台湾民主自治同盟盟员'),
        (12, u'无党派民主人士'),
        (13, u'群众'),
    )

    Name=models.CharField('姓名',max_length=20)
    Sex=models.IntegerField('性别',choices=Sex_choices)
    Nationality=models.IntegerField('民族',choices=Nationality_choice)
    BirthDate=models.DateField('出生日期',)#help_text='格式规范1970-01-01'
    NativePlace=models.CharField('籍贯',max_length=50)
    PoliticsStatus=models.IntegerField('政治面貌',choices=PoliticsStatus_choice)
    MaritalStatus=models.IntegerField('婚姻状况',choices=MaritalStatus_choice)
    Tel=models.CharField('联系电话',max_length=11,validators=[RegexValidator(r'^^[\d]{11}')],unique=True)
    Email=models.EmailField('电子邮箱',max_length=50,unique=True)
    IDCardNo=models.CharField('身份证号',max_length=18,validators=[RegexValidator(r'^[\d]{17}[x,X,\d]{1}')],unique=True)
    EmergencyContactName=models.CharField('紧急联系人姓名',max_length=20)
    EmergencyContactRelation=models.IntegerField('与紧急联系人关系',choices=EmergencyContactRelation_choice)
    EmergencyContactTel=models.CharField('紧急联系电话',max_length=11,validators=[RegexValidator(r'^[\d]{11}')])
    CurrentResidentialAddress=models.CharField('现居住地址',max_length=255)
    HomeAddress=models.CharField('家庭地址',max_length=255)
    IDAddress=models.CharField('身份证地址',max_length=255)

    def __str__(self):
        return self.IDCardNo    
    
class Educationinfo(models.Model):
    EducationNature_choice=(
        (None, u'请选择'),
        (1, u'统招'),
        (2, u'成教'),
        (3, u'自考'),
        (4, u'专升本'),
        (4, u'网教'),
        (5, u'其他'),
    )
    EducationBackground_choice=(
        (None, u'请选择'),
        (1, u'博士'),
        (10, u'硕士'),
        (20, u'本科'),
        (30, u'大专'),
        (40, u'大专以下'),
    )

    UniversityName=models.CharField('学校全称',max_length=50)
    StartTime=models.DateField('开始时间',)
    EndTime=models.DateField('结束时间')
    Profession=models.CharField('专业',max_length=50)
    EducationBackground=models.IntegerField('学历',choices=EducationBackground_choice)
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
    Relation=models.IntegerField('与本人关系',choices=EmergencyContactRelation_choice)
    BirthDate=models.DateField('出生日期')
    WorkUnit=models.CharField('工作单位',max_length=50)
    Duty=models.CharField('职务',max_length=50)
    Tel=models.CharField('联系电话',max_length=11,validators=[RegexValidator(r'^[\d]{11}')])
    IDCardNo=models.ForeignKey("Empinfo",on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.id)