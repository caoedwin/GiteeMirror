# -*- coding:utf-8 -*-
import subprocess, os, sys,shutil
path1 = os.path.dirname(os.path.realpath(sys.executable))

os.environ['Jeita2Path'] = path1
# os.system(r'reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v AUTORUN /t REG_SZ /d C:\DCTtools\DCTCLient_startup.exe /f>nul')
# os.system(r'start C:\DCTtools\startup.bat')
pathe = os.getenv('Jeita2Path')
print(pathe)
command = r'setx "Jeita2Path" "%s" /m' % path1
# print(command)
os.system(command)
pathe = os.getenv('Jeita2Path')
print(pathe)
