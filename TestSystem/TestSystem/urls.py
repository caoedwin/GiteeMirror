"""TestSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from myblog import views as blog_view
urlpatterns = [

    path('index/', blog_view.Index, name='index'),
    path('', blog_view.Login),
    path('login/', blog_view.Login, name='login'),
    # path('logsuccess/', blog_view.logsuccess, name='logsuccess'),
    path('logout/', blog_view.logout, name='logout'),
    path('admin/', admin.site.urls),
    path('register', blog_view.Register, name='register'),
    path('category/<int:pd>', blog_view.CategoryList, name='category'),
    path('search/', blog_view.Search, name='search'),
    path('detail/<int:pk>', blog_view.ArticleDetail.as_view(), name='detail'),
    path('updateArticle/<int:id>', blog_view.article_update, name='updateArticle'),
    path('comment/', blog_view.pub_comment, name='comment'),
    path('addArticle/', blog_view.article_create, name='addArticle'),
    path('delete/<int:id>', blog_view.article_delete, name='delete'),
    path('myArticle/', blog_view.MyArticle, name='myArticle'),
    path('close/', blog_view.closeComment, name='close'),
    path('addTag/', blog_view.Tag_add, name='addTag'),
    path('auditing/', blog_view.examine_article, name='auditing'),
    path('changeStatus/', blog_view.ChangeStatus, name='changeStatus'),
    path('changPass/', blog_view.changPassword, name='changPass'),
    path('changeFlag/', blog_view.change_flag, name='changeFlag'),

]

