from django.db import models
from django.contrib.auth.models import User  # 使用Django自带的用户模型
from django.contrib import admin
from django.utils.timezone import now
from myblog.models import *  # 导入所有模型类

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 200)
    nickname = models.CharField(max_length = 50, default='匿名')
    email = models.EmailField()
    created_time = models.CharField(max_length=50, default=now)
    canEdit = models.IntegerField(default=1)

    def __str__(self):
        return self.username

# 文章类别
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('类别', max_length=20, unique=True)

    class Meta:
        verbose_name_plural = verbose_name = '类别'

    def __str__(self):
        return self.name

# 文章状态
class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('状态', max_length=20, unique=True)

    class Meta:
        verbose_name_plural = verbose_name = '状态'

    def __str__(self):
        return self.name

# 文章标签
class Tag(models.Model):
    name = models.CharField('标签', max_length=20, unique=True)

    class Meta:
        verbose_name_plural = verbose_name = '标签'

    def __str__(self):
        return self.name

class Article(models.Model):  # 文章
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容')
    pub_time = models.DateField('日期', auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1, verbose_name='类别')
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=1, verbose_name='状态')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    # status = models.CharField('状态', max_length=10)
    total_views = models.PositiveIntegerField(default=0)
    permission = models.PositiveIntegerField(default=0)
    reason = models.CharField('理由', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = '文章'

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('昵称', max_length=20)
    email = models.EmailField('邮箱')
    content = models.TextField('内容')
    publish = models.DateField('时间', auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')
    reply = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='回复')

    class Meta:
        verbose_name_plural = verbose_name = '评论'

    def __str__(self):
        return self.content

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_time', 'status')  # 文章列表的显示项

admin.site.register((Category, Comment, Tag, Status, User))  # 多个模块注册到后台
