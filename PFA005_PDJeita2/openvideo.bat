@echo off
rem echo 当前盘符：%~d0
rem echo 当前盘符和路径：%~dp0
rem echo 当前批处理全路径：%~f0
rem echo 当前盘符和路径的短文件名格式：%~sdp0
rem echo 当前CMD默认目录：%cd%
rem echo 目录中有空格也可以加入""避免找不到路径
rem echo 当前盘符："%~d0"
rem echo 当前盘符和路径："%~dp0"
rem echo 当前批处理全路径："%~f0"
rem echo 当前盘符和路径的短文件名格式："%~sdp0"
rem echo 当前CMD默认目录："%cd%"
rem pause

echo dangqian:"%~dp0"
echo VideoUIPath:"%VideoUIPath%"
cd /d "%~dp0"
rem start "C:\Program Files\WindowsApps\Microsoft.ZuneVideo_10.22041.10091.0_x64__8wekyb3d8bbwe\Video.UI.exe" "JB2_0.mp4"
start "%VideoUIPath%" "JB2_0.mp4"
rem pause
