from celery.task import task
from .views import ImportProjectinfoFromDCT

# 自定义要执行的task任务
#在项目manage.py统计目录下cmd或pycharmTerminal运行celery worker -A mydjango -l info -P eventlet，celery -A mydjango beat -l info
#窗口不能关闭
@task
def ProjectSync():
    print("Start")
    importPrjResult = ImportProjectinfoFromDCT()
    if importPrjResult:
        return "OK"
    else:
        return "Fail"