@echo off
if "%1"=="h" goto begin
start mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
cd /d C:\djangoproject\DMS
del celerybeat.pid
c:\Python372\mecheck\Scripts\celery.exe -A DMS beat -l info