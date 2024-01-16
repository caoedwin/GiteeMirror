"""
Django settings for Reliability_Row_data project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os,sys
import time, datetime
from datetime import timedelta

# 管理员邮箱
ADMINS = (
    ('Admin', 'Edwin_Cao@compal.com'),
)

# 非空链接，却发生404错误，发送通知MANAGERS
SEND_BROKEN_LINK_EMAILS = True
MANAGERS = ADMINS

# Email设置1-外網qq
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com' # 腾讯QQ邮箱 SMTP 服务器地址
EMAIL_PORT = 25 # SMTP服务的端口号
EMAIL_HOST_USER = '416434871@qq.com' #你的qq邮箱，邮件发送者的邮箱
EMAIL_HOST_PASSWORD = 'umjszfmhjjmbbgdj' #你申请的授权码（略）
EMAIL_USE_TLS = False #与SMTP服务器通信时,是否启用安全模式

# Email设置2-内網OA
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'webmail.compal.com'  # QQ邮箱SMTP服务器(邮箱需要开通SMTP服务)
# # EMAIL_PORT = 25  # QQ邮箱SMTP服务端口
# EMAIL_PORT = 443
# EMAIL_HOST_USER = 'Edwin_Cao@compal.com'  # 我的邮箱帐号
# # EMAIL_HOST_PASSWORD = '*******'  # 授权码
# EMAIL_HOST_PASSWORD = '!1234zxcv'
# EMAIL_SUBJECT_PREFIX = 'DDIS'  # 为邮件标题的前缀,默认是'[django]'
# EMAIL_USE_TLS = True  # 开启安全链接
# DEFAULT_FROM_EMAIL = SERVER_EMAIL = EMAIL_HOST_USER  # 设置发件人

cur_path = os.path.dirname(os.path.realpath(__file__))  # log_path是存放日志的路径
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
if not os.path.exists(log_path): os.mkdir(log_path)  # 如果不存在这个logs文件夹，就自动创建一个

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # 日志格式
        'standard': {
            'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'},
        'simple': {  # 简单格式
            'format': '%(levelname)s %(message)s'
        },
    },
    # 过滤
    'filters': {
    },
    # 定义具体处理日志的方式
    'handlers': {
        # 默认记录所有日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'all-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        # 输出错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'error-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },
        # 控制台输出
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 输出info日志
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'info-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',  # 设置默认编码
        },
    },
    # 配置用哪几种 handlers 来处理日志
    'loggers': {
        # 类型 为 django 处理所有类型的日志， 默认调用
        'django': {
            'handlers': ['default', 'console', 'error'],
            'level': 'INFO',
            'propagate': False
        },
        # log 调用时需要当作参数传入
        'log': {
            'handlers': ['error', 'info', 'console', 'default'],
            'level': 'INFO',
            'propagate': True
        },
    }
}
import logging

logger = logging.getLogger('Django')
# logger.debug('Debug')
# logger.info('Info')
# logger.warning('Warning')
# logger.error('Error')
# logger.critical('Critical')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g!4+oe!rx(r%pm^=ryc)j57sieed1eea3_de63o&6+u0tu2%^i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# DjangoUeditor3
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
# Application definition

INSTALLED_APPS = [
    # 'mongonaut',
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    # 'mongoengine.django.mongo_auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    # 'rest_framework.authtoken'# TokenAuthentication认证模式，在settings.py中添加这个app后，它会帮我们在数据库中生成一张authtoken表，所以我们要确保manage.py migrate在更改设置后运行。该rest_framework.authtoken应用程序提供Django数据库迁移。
    # 1.用户向登陆时服务会创建一个token值返回给用户，同时也将这个token值保存到了服务器数据库表中，如果是一个分布式系统的话，想通过一套认证系统的token表用来验证用户登陆，就会出现问题。
    # 2.authtoken表中存放的token值没有过期时间字段，如果token值一旦泄露，非常危险。
    # 3.随着用户的增多，token值会占用服务器大量空间，同时也会加大数据库的查询压力，性能下降
    'djcelery', #此处是新加入的djcelery
    'notifications',#需要用django自带的用户模型
    # 'app01.apps.App01Config',
    'app01',
    # 'app01.templatetags',
    'DjangoUeditor', #注册APP应用
    'CDM',
    'CQM',
    'Bouncing',
    'Package',
    'TestPlanME',
    'LessonProjectME',
    'DriverTool',
    'TestPlanSW',
    'TestPlanSWOS',
    'MQM',
    'QIL',
    'mongotest',
    'INVGantt',
    'SpecDownload',
    'Issue_Notes',
    'KnowIssue',
    'PersonalInfo',
    'OBIDeviceResult',
    'AutoResult',
    'ABOTestPlan',
    'PersonalExperience',
    'NonDQALesson',
    'LowLightList',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',#这里要注意中间件加载顺序，列表是有序的。django-cors-headers
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.checkper.RbacMiddleware',
    'middleware.UserIP.LogMiddle',  #自定义中间键获取IP内容
]

ROOT_URLCONF = 'Reliability_Row_data.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Reliability_Row_data.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
import mongoengine,pymongo,parse,urllib

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reliabilityrowdata',
        'USER': 'edwin',
        'PASSWORD': 'DCT@2019',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    },
    # 'mongotest': {
    #     'ENGINE': 'django_mongodb_engine',
    #     'NAME': 'mongotest',
    #     }#可以不要
}
_MONGODB_USER = urllib.parse.quote_plus("edwin")#'edwin'
_MONGODB_PASSWD = urllib.parse.quote_plus("DCT@2019")#'DCT@2019'
_MONGODB_HOST = '127.0.0.1:27017'
_MONGODB_NAME = 'admin'#数据集的名字与账户密码要对应，也就是说账户密码要有当前数据集的权限
_MONGODB_DATABASE_HOST = 'mongodb://%s:%s@%s/%s' % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)
mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)

# user = urllib.parse.quote_plus("edwin")
# passwd = urllib.parse.quote_plus("DCT@2019")
#
# #连接MongoDB
# myclient = pymongo.MongoClient("mongodb://{0}:{1}@127.0.0.1:27016/mongotest".format(user,passwd))


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

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S'

TIMEOUT = 600 # 设置超时时间为30秒

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/



# 允许跨域源 生产环境开启跨域
CORS_ORIGIN_ALLOW_ALL = False
# 配置指定跨域域名
CORS_ORIGIN_WHITELIST = []

# 允许ajax请求携带cookie
CORS_ALLOW_CREDENTIALS = True

# must inherit from AbstractUsers (django)
# AUTH_USER_MODEL = 'custom_auth.users'
# AUTH_USER_MODEL = 'app01.UserInfo'#自定义用户模型必须要继承AbstractUser类，或AbstractBaseUser类（AbstractBaseUser的子类有一些必须定义的关键的字段和方法），或者 使用OneToOneField，
REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
    # 用户登陆认证方式
    # SessionAuthentication, BasicAuthentication，为了兼容drf自带的页面认证方式
    # 若使用drf默认登录认证，不能使用自定义表的用户信息，只可以用默认User表用户登录，通过python manage.py createsuperuser创建
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.SessionAuthentication',
    #     'rest_framework.authentication.BasicAuthentication',
    # )
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

}
# jwt
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(minutes=20),
    # 'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}
#
# AUTHENTICATION_BACKENDS = (
#     "django.contrib.auth.backends.ModelBackend",
#     # "allauth.account.auth_backends.AuthenticationBackend",
#     # "master_password.auth.ModelBackend"
#     'CQM.authentication.CustomAuthBackend',
# )



# REST_FRAMEWORK = {
# # # 身份认证
#     'DEFAULT_AUTHENTICATION_CLASSES': (#（全局需要用DRF写用户的注册登陆接口，可以另外创建一个用于DRF的用户module）
#         # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#         # 'rest_framework.authentication.SessionAuthentication',
#         # 'rest_framework.authentication.BasicAuthentication',#Django自带的用户reliabilityrowdata.auth_user（edwin，DCT@2019）
#         # 'rest_framework.authentication.TokenAuthentication',
#         # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',#Django自带的用户reliabilityrowdata.auth_user（edwin，DCT@2019）
#         # 'CQM.authentication.MyOwnTokenAuthentication',# 全局自定义Token认证（基于传统的 token 认证，JWT也是基于auth.user，并且可以自动分发token，不需要手动）
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (#（全局需要用DRF写用户的注册登陆接口，可以另外创建一个用于DRF的用户module）
#         'rest_framework.permissions.IsAuthenticated',#(有效打勾的就有权限)如果未指定，则此设置默认为允许无限制访问'rest_framework.permissions.AllowAny',
#         # 'rest_framework.permissions.IsAdminUser',#(职员状态打勾的才有权限)
#     ),
# }
# JWT_AUTH = {
#                'JWT_ENCODE_HANDLER':
#                    'rest_framework_jwt.utils.jwt_encode_handler',
#
#                'JWT_DECODE_HANDLER':
#                    'rest_framework_jwt.utils.jwt_decode_handler',
#
#                'JWT_PAYLOAD_HANDLER':
#                    'rest_framework_jwt.utils.jwt_payload_handler',
#
#                'JWT_PAYLOAD_GET_USER_ID_HANDLER':
#                    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
#
#                'JWT_RESPONSE_PAYLOAD_HANDLER':
#                    'rest_framework_jwt.utils.jwt_response_payload_handler',
#
#            # 这是用于签署JWT的密钥，确保这是安全的，不共享不公开的
#                 # 'JWT_SECRET_KEY': settings.SECRET_KEY,
#                 'JWT_GET_USER_SECRET_KEY': None,
#                 'JWT_PUBLIC_KEY': None,
#                 'JWT_PRIVATE_KEY': None,
#                 'JWT_ALGORITHM': 'HS256',
#                 # 如果秘钥是错误的，它会引发一个jwt.DecodeError
#                 'JWT_VERIFY': True,
#                 'JWT_VERIFY_EXPIRATION': True,
#                 'JWT_LEEWAY': 0,
#                 # Token过期时间设置
#                 'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
#                 'JWT_AUDIENCE': None,
#                 'JWT_ISSUER': None,
#
#                 # 是否开启允许Token刷新服务，及限制Token刷新间隔时间，从原始Token获取开始计算
#                 'JWT_ALLOW_REFRESH': False,
#                 'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
#
#                 # 定义与令牌一起发送的Authorization标头值前缀
#                 'JWT_AUTH_HEADER_PREFIX': 'JWT',
#                 'JWT_AUTH_COOKIE': None,
# }




STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),


)
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = 'c:\media'
MEDIA_URL = 'c:/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 即项目路径下的media文件夹，没有则自动创建
MEDIAFILES_DIRS = (
    os.path.join(BASE_DIR, 'media'),

    r'c:/media',

)
#服务器路径
# MEDIA_ROOT = 'I:\DMS_D disk\DDISvirtualmedia\media'
# MEDIA_URL = 'I:/DMS_D disk/DDISvirtualmedia/media/'
# MEDIAFILES_DIRS = (
#     os.path.join(BASE_DIR, 'media'),
#
#     r'I:/DMS_D disk/DDISvirtualmedia/media',
#
# )#


# MEDIA_URL = '/media/'  # 这个是在浏览器上访问该上传文件的url的前缀


# Session setting
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
#从Django 1.6开始session里面的数据都是用JSON来serialize。JSON的session只能接受简单的数据结构比如str, list, dict。 有两个选择，可以先把cart的数据放在一个dict里面再存到 session或者可以换一个SessionSerializer。Django还提供一个用pickle来serialize的选择可以存任何一个数据结构。
#不加的话当用数据库存储session会报无法序列化的错误

SESSION_SAVE_EVERY_REQUEST=True
SESSION_COOKIE_AGE = 5 * 12 * 60 * 60#setting中设置session的cookie失效时间12h
SESSION_ENGINE = 'django.contrib.sessions.backends.db'#'django.contrib.sessions.backends.cache'#设置session存储方式为缓存
SESSION_EXPIRE_AT_BROWSER_CLOSE = False



LOGIN_URL = '/login/'
REGEX_URL = r'{url}'  # url作严格匹配

SESSION_PERMISSION_URL_KEY='URL_per'
SESSION_MENU_KEY = 'awesome'
ALL_MENU_KEY = 'k1'
PERMISSION_MENU_KEY = 'k2'
PERMISSION_MENU_KEY1 = 'k3'

# 配置url权限白名单
SAFE_URL = [
    r'/login/',
    '/admin/.*',
    r'/api-token-auth/',
    r'/api-token-verify/',
    r'/Project_log/',
    r'/index/',
    r'/FilesDownload/',
    r'/Navigation/',
    r'/ueditor/',
    r'/logout/',
    r'/ttt/',
    r'/ctest/',
    # r'/ProjectInfoSearch/',
    r'/Change_Password/',
    r'/Change_Skin/',
    r'/media/.*',
    r'/static/.*',
    '/LessonProjectME/LessonProjectME-edit/.*',
    r'/test/',
    '/mongotest/.*',
    '/INVGantt/INVGantSeri/.*',
    '/INVGantt/INVGantSerire/.*',
    '/INVGantt/INVGantSeriv/.*',
    '/INVGantt/apilogin/.*',
    '/CQM/CQMapi/.*',
    '/CQM/CQMapi1/.*',
    '/api-auth/.*',
    '/api/token/.*',
    '/CQM/api/.*',
    '/PersonalInfo/api_Per/.*',
    '/PersonalInfo/Perapi/',
    '/docs/.*',
    # '/redit_Lesson/.*',
    # r'/CDM/CDM-upload/',
    # r'/CDM/CDM-edit/',
    # r'/CDM/CDM-update/.*',
    # r'/CDM/CDM-search/',
]

# import djcelery
# djcelery.setup_loader()
# BROKER_URL = 'redis://127.0.0.1:6379/6'
# CELERY_IMPORTS = ('app01.tasks', )
# CELERY_TIMEZONE = TIME_ZONE
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

CELERY_BROKER_URL = 'redis://:DCT2019@localhost:6379/1'
#Redis 16个库任你选,同一台机器启动多个celery，BROKER_URL必须不同才行。Redus在Celery体系中充当消息中间件（message broker）作用，如果都放在一个redis库中，当两个celery都启动时，读取任务会将另一个项目的任务也读取过来，直接报错。
CELERY_RESULT_BACKEND = 'redis://:DCT2019@localhost:6379/2'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_TIMEZONE = 'Asia/Shanghai'#要与系统时区TIME_ZONE一致

from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
    'task-flag': {
        'task': 'app01.tasks.Ongoing_flag',
        'schedule': 60.0#5.0, # 每5秒执行一次
        # 'schedule': crontab(minute='30', hour='8', day_of_week='1,2,3,4,5')#每周的1-5，10点0分执行
        # 'args': ()
    },
    # 周期性任务
    'task-one': {
        'task': 'app01.tasks.ProjectSync',
        # 'schedule': 86400.0#5.0, # 每5秒执行一次
        'schedule': crontab(minute='30', hour='8', day_of_week='1,2,3,4,5')#每周的1-5，10点0分执行
        # 'args': ()
    }
}
