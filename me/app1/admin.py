# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from .models import TestLog#,UserInfo
from rbac.models import Menu,Permission,Role,UserInfo,Item_Spec,Project_Spec

admin.site.site_url = '/index/'

# admin.site.register(Role)
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'url','menu','Proj_perm',)
        }),
    )
    list_display = ('title',)
    # 列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-title',)
    # 后台数据列表排序方式
    list_display_links = ('title', )
#导入需要管理的数据库表

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('account', 'password', 'username','email','roles','perm',)
        }),
    )
    list_display = ('account', 'password', 'username', 'email',)
    # 列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-username',)
    # 后台数据列表排序方式
    list_display_links = ('username', )
    search_fields = ('account', 'password', 'username','email','roles','perm')  # 搜索字段
#导入需要管理的数据库表

@admin.register(Item_Spec)
class Item_SpecAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('Cus_I', 'Item_I', 'Category', 'Item_Description','Sample_Demand',)
        }),
    )
    list_display = ('Cus_I', 'Item_I', 'Category', 'Item_Description','Sample_Demand',)
    # 列表里显示想要显示的字段
    # list_per_page = 50
    list_max_show_all = 100
    # 满50条数据就自动分页
    ordering = ('-Cus_I',)
    # 后台数据列表排序方式
    list_display_links = ('Cus_I', )
    # list_filter = ('Project', 'Result', 'Tester')  # 过滤器
    search_fields = ('Cus_I', 'Item_I', 'Category', 'Item_Description','Sample_Demand')  # 搜索字段


@admin.register(Project_Spec)
class Project_SpecAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('Cus_P', 'Project_P', 'Phase_P', 'Item_P',)# 'Owner_P',)
        }),
    )
    list_display = ('Cus_P', 'Project_P', 'Phase_P',)
    # 列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-Cus_P',)
    # 后台数据列表排序方式
    list_display_links = ('Cus_P', )
#导入需要管理的数据库表

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'permissions',)# 'Owner_P',)
        }),
    )
    list_display = ('title', )
    # 列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-title',)
    # 后台数据列表排序方式
    list_display_links = ('title', )
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'parent',)# 'Owner_P',)
        }),
    )
    list_display = ('title',)
    # 列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-title',)
    # 后台数据列表排序方式
    list_display_links = ('title', )

@admin.register(TestLog)
class TestLogAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields' : ('Customer','Project', 'Unit', 'Phase', 'Testitem','Item_Des', 'Tester')
        }),
        ('Advanced options',{
            'classes': ('collapse',),
            'fields' : ('Start_time', 'End_time', 'Result_time','Result','Comments')
        }),
    )
    list_display = ('Customer','Project', 'Unit', 'Phase', 'Tester', 'Testitem','Result', 'Start_time', 'End_time', 'Result_time','Item_Des', 'Comments')
    # 列表里显示想要显示的字段
    list_per_page = 200
    # 满50条数据就自动分页
    ordering = ('-Start_time',)
    #后台数据列表排序方式
    list_display_links = ('Customer','Project', 'Unit', 'Phase', 'Tester', 'Testitem','Result', 'Start_time', 'End_time', 'Result_time','Item_Des', 'Comments')
    # 设置哪些字段可以点击进入编辑界面
    # list_editable = ('Tester',)
    # 筛选器
    # list_filter = ('Customer','Project', 'Unit', 'Phase', 'Tester', 'Testitem','Result', 'Start_time', 'End_time', 'Result_time','Item_Des', 'Comments')  # 过滤器
    list_filter = ('Project','Result', 'Tester')  # 过滤器
    search_fields = ('Customer','Project', 'Unit', 'Phase', 'Tester', 'Testitem','Result', 'Start_time', 'End_time', 'Result_time','Item_Des', 'Comments')  # 搜索字段
    # date_hierarchy = 'Start_time'  # 详细时间分层筛选
