@echo off
if "%1"=="h" goto begin
start mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
cd /d C:\djangoproject\Reliability_Row_data
c:\Python372\mecheck\Scripts\celery.exe worker -A Reliability_Row_data -l info -P eventlet