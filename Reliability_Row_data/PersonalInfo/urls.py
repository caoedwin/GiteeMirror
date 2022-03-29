from django.urls import path
from . import views
app_name = 'PersonalInfo'
urlpatterns = [


    path('Infos-upload/', views.Infos_upload, name='Infos_upload'),
    path('PersonalInfo-search/', views.PersonalInfo_search, name='PersonalInfo_search'),
    path('PersonalInfo-edit/', views.PersonalInfo_edit, name='PersonalInfo_edit'),
    path('ManPower-search/', views.ManPower_search, name='ManPower_search'),
    path('ManPower-edit/', views.ManPower_edit, name='ManPower_edit'),
    path('Summary1/', views.Summary1, name='Summary1'),
    path('Summary2/', views.Summary2, name='Summary2'),
    path('Summary3/', views.Summary3, name='Summary3'),
    path('PublicArea/', views.PublicArea, name='PublicArea'),
]