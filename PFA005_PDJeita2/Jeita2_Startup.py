import os,subprocess

try:
    path1 = os.getenv('Jeita2Path')
    Processfile = path1 + "\Jeita2_Process.exe"
    with open('dataSt.txt', 'w') as f:  # 设置文件对象
        print(path1, Processfile, file=f)
    # os.system(r'reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v AUTORUN /t REG_SZ /d C:\DCTtools\DCTCLient_startup.exe /f>nul')
    # os.system(r'start C:\DCTtools\startup.bat')
    subprocess.call(Processfile, shell=True)
except Exception as e:
    with open('errorStart.txt', 'w') as f:  # 设置文件对象
        print(e, file=f)