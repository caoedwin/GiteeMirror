"""me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include , re_path
from django.conf.urls import url, include
#留意上面这行比原来多了一个include
from django.views.static import serve
#导入静态文件模块
from django.conf import settings
#导入配置文件里的文件上传配置
from app1 import views
import xadmin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path(r'login/', views.login),
    path(r'', views.login),
    path(r'logout/', views.logout),
    path(r'Change_Password/', views.Change_Password),
    path(r'Change_Skin/', views.Change_Skin),
    path(r'index/', views.index),
    path(r'mini-dashboard-project/', views.miniDashboardProject),
    path(r'dashboard-project/', views.DashboardProject),
    path(r'dashboard-units/', views.DashboardUnits),
    path(r'SearchExport/', views.SearchExport),
    path(r'Manage/', views.Manage),
    # path(r'test/', views.DashboardUnits),
    path(r'rbac/', include('rbac.urls') ),
    path('ueditor/', include('DjangoUeditor.urls')), #添加DjangoUeditor的URL
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),#增加此行
    re_path('^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),#增加此行
    # path(r'', views.login),
    # url(r'^admin/', admin.site.urls),
    # # url(r'',views.login()),
    # url(r'^login/$', views.login),
    # url(r'^logout/$', views.logout),
    # url(r'^Change_Password/$', views.Change_Password),
    # url(r'^index/$', views.index),
    # url(r'^dashboard-project/$', views.DashboardProject),
    # url(r'^dashboard-units/$', views.DashboardUnits),
    # url(r'^Search/$', views.Search),
    # url(r'^rbac/', include('rbac.urls') ),
    # re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),#增加此行
    # re_path('^statuc/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),#增加此行
]