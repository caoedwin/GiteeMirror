import subprocess, os, sys,shutil

try:
    path1 = os.path.dirname(os.path.realpath(sys.executable))
    startupfile = path1 + "\Jeita2_Startup.exe"
    startup_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
    os.putenv('Jeita2Path', path1)
    shutil.copy(startupfile, startup_path)
    # os.system(r'reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v AUTORUN /t REG_SZ /d C:\DCTtools\DCTCLient_startup.exe /f>nul')
    # os.system(r'start C:\DCTtools\startup.bat')
    subprocess.call(startupfile)
except Exception as e:
    with open('errorTest.txt', 'w') as f:  # 设置文件对象
        print(e, file=f)