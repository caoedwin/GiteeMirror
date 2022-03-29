from django.urls import path
# 引入views.py
from . import views

app_name = 'CQM'

urlpatterns = [

    path('CQM_upload/', views.CQM_upload, name='CQM_upload'),

    path('CQM_edit/', views.CQM_edit, name='CQM_edit'),
    # path('CDM-update/<int:id>/', views.CDM_update, name='CDM_update'),
    path('CQM_search/', views.CQM_search, name='CQM_search'),
    # path('CDM-export/', views.CDM_export, name='CDM_search'),
    # path('apilogin/', views.LoginView.as_view(), name='apilogin'), # 用于登陆
    path('CQMSeriv/', views.CQMSeriView.as_view(), name='CQMSeriv'),# 用于认证测试


]