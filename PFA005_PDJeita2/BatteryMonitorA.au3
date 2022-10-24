
#include <File.au3>
#include <MsgBoxConstants.au3>
#RequireAdmin
;$settingfile = @ScriptDir & @CRLF & "\SysSettingsModifier_V4.2022\SysSettingsModifier.exe"
$Path = @WorkingDir & "\New Battery Manager\BatteryManager.exe"
$Path_video = @WorkingDir & "\JB2_0.mp4"
$Path_player = "C:\Program Files\WindowsApps\Microsoft.ZuneVideo_10.22041.10091.0_x64__8wekyb3d8bbwe\Video.UI.exe"

Run($Path)
Sleep(1000)
If  WinExists("BattManager") Then
        
        WinActivate("BattManager")       

        
EndIf 
Local $hWin = WinWaitActive("BattManager", "", 2)
ControlFocus($hWin,"","[NAME:button1]")
ControlClick($hWin, "","[NAME:button1]")

Sleep(1000)
FileChangeDir(@WorkingDir)
;MsgBox($MB_SYSTEMMODAL, "", @WorkingDir)
Run("openvideo.bat")
Sleep(8000)
Local $hWin = WinWaitActive("[CLASS:ApplicationFrameWindow]" , "", 10)
If  WinExists("[CLASS:ApplicationFrameWindow]") Then
        
        WinActivate("[CLASS:ApplicationFrameWindow]")    
EndIf 
Sleep(1000)
Send("{TAB 5}")
Send("{ENTER}")
Sleep(1000)
Send("{TAB 2}")
Send("{ENTER}")
Sleep(1000)
Send("{ESC}")
Sleep(1000)
;Send("{a ALT}") ;Holds the A key down
;Sleep(500)
;Send("{ENTER}")
;Sleep(500)
;Send("{a ALT}") ;Releases the A key
Send("{ALTDOWN}") 
Sleep(500)
Send("{ENTER}")
Sleep(500)
Send("{ALTUP}") 

;MsgBox($MB_SYSTEMMODAL, "", $cmdyj)



			
IniWrite(@WorkingDir & "\Times.ini","section2", "Progress", "Time A")
IniWrite(@WorkingDir & "\Times.ini","section2", "时间", @YEAR & "-" & @MON & "-" & @MDAY & " " & @HOUR & ":" & @MIN & ":" & @SEC)
IniWrite(@WorkingDir & "\Times.ini","section1", "Restart", "2")

;IniWrite(@WorkingDir & "\Times.ini","section3", "Progress", "Time B")
;IniWrite(@WorkingDir & "\Times.ini","section3", "时间", @YEAR & "-" & @MON & "-" & @MDAY & " " & @HOUR & ":" & @MIN & ":" & @SEC)
;IniWrite(@WorkingDir & "\Times.ini","section1", "Restart", "3")
