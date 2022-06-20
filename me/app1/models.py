# -*- coding: utf-8 -*-
from django.db import models
import django.utils.timezone as timezone
# from DjangoUeditor.models import UEditorField #头部增加这行代码导入UEditorField

# Create your models here.
from django.contrib.auth.models import User

#导入Django自带用户模块

class UserInfo(models.Model):
    Account = models.CharField('Account', max_length=20,default="",)
    Password = models.CharField('Password', max_length=256,default="",)
    Username = models.CharField('Username', max_length=20,default="",unique=True)

    class Meta:
        verbose_name = 'UserInfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Username
# 文章分类
class TestLog(models.Model):
    Customer = models.CharField('Customer', max_length=10, default="", )
    Project = models.CharField('Project', max_length=100,default="",)
    Unit = models.CharField('Unit', max_length=100,default="",)
    Phase = models.CharField('Phase', max_length=10,default="",)
    Testitem = models.CharField('Testitem', max_length=100,default="",)
    Item_Des = models.CharField('Item_Des', max_length=500, default="", )
    # Testitem = UEditorField('内容', width=800, height=500,
    #                         toolbars="full", imagePath="upimg/", filePath="upfile/",
    #                         upload_settings={"imageMaxSize": 1204000},
    #                         settings={}, command=None, blank=True
    #                         )

    Tester = models.CharField('Tester', max_length=20,default="",)
    Comments = models.CharField('Comments', max_length=1000, blank=True,default="", )
    Start_time = models.CharField('Start_time', max_length=26 ,blank=True, default="",)
    End_time = models.CharField('End_time',max_length=26, blank=True,default="",)
    Result_time = models.CharField('Result_time',max_length=26, blank=True,default="",)
    Result = models.CharField('Result',max_length=26, blank=True,default="",)

    class Meta:
        verbose_name = 'TestLog'
        verbose_name_plural = verbose_name

    def __str__(self):
        # return str(self.id)#{'Project':self.Project,'Unit':self.Unit,'Phase':self.Phase,'Testitem':self.Testitem,'Start_time':self.Start_time,'End_time':self.End_time,'Tester':self.Tester,'Comments':self.Comments}
        return "%s+%s+%s+%s+%s+%s+%s+%s+%s+%s"%(self.id,self.Customer,self.Project,self.Unit,self.Phase,self.Testitem,self.Start_time,self.End_time,self.Comments,self.Tester)
    # def getothers(self):
    #     return "%s:%s:%s:%s:%s:%s:%s:%s"(self.Project,self.Unit,self.Phase,self.Testitem,self.Start_time,self.End_time,self.Comments,self.Tester)