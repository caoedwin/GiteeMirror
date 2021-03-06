"""
Django settings for me project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os,sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR,'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z9*kg&)8&7&o8s5n-pis0yj==uvp$d##e%1xc+7j5l!-x^1-eq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1.apps.App1Config',
    'DjangoUeditor', #注册APP应用
    'captcha',
    'rbac',
    'xadmin',
    'crispy_forms',
]


MIDDLEWARE = [
    # 'middleware.m1.SecureRequiredMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rbac.middleware.rbac.RbacMiddleware'  # 加入自定义的中间件到最后
]

ROOT_URLCONF = 'me.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'me.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'metestcourse',
        'USER': 'edwin',
        'PASSWORD': 'DCT@2019',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
# HERE = os.path.dirname(os.path.abspath(__file__))
# HERE = os.path.join(HERE, '../')
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),


)
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Session setting
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
#从Django 1.6开始session里面的数据都是用JSON来serialize。JSON的session只能接受简单的数据结构比如str, list, dict。 有两个选择，可以先把cart的数据放在一个dict里面再存到 session或者可以换一个SessionSerializer。Django还提供一个用pickle来serialize的选择可以存任何一个数据结构。
#不加的话当用数据库存储session会报无法序列化的错误

SESSION_SAVE_EVERY_REQUEST=True
SESSION_COOKIE_AGE = 12 *60 * 60#setting中设置session的cookie失效时间12h
SESSION_ENGINE = 'django.contrib.sessions.backends.db'#'django.contrib.sessions.backends.cache'#设置session存储方式为缓存
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# 定义session 键：
# 保存用户权限url列表
# 保存 权限菜单 和所有 菜单
# session_permisson_key
# SESSION_PERMISSION_URL_KEY = "perUrl"
# SESSION_MENU_KEY = "menu"
# MENU_ALL = "menuAll"
# MENU_PERMISSON = "menuPer"
SESSION_PERMISSION_URL_KEY = 'cool'

SESSION_MENU_KEY = 'awesome'
ALL_MENU_KEY = 'k1'
PERMISSION_MENU_KEY = 'k2'

LOGIN_URL = '/login/'
REGEX_URL = r'{url}'  # url作严格匹配

# 配置url权限白名单
# 不需要做菜单权限管理所以将所有菜单都加到白名单
SAFE_URL = [
    '/admin/.*',
    '/',
    '/xadmin/.*',
    r'/login/',
    r'/logout/',
    '/Change_Password/',
    '/Change_Skin/'
    '/index/',
    '/dashboard-project/',
    '/mini-dashboard-project/',
    '/dashboard-units/',
    '/SearchExport/',
    '/Manage/',
    '^/rbac/',
    '^media/(?P<path>.*)',
    '^static/(?P<path>.*)',
    # '/test/',
    # '/index/',
    # '^/rbac/',
]
# SECURE_REQUIRED_PATHS = (
#
#     '/admin/.*',
#     r'/login/',
#     r'/logout/',
#     '/Change_Password/',
#     '/index/',
#     '/dashboard-project/',
#     '/dashboard-units/',
#     '/SearchExport/',
#     '/Manage/',
#     '^/rbac/',
#     '^media/(?P<path>.*)',
#     '^static/(?P<path>.*)',
#
# )
# HTTPS_SUPPORT=True