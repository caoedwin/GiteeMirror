
#include <File.au3>
#include <MsgBoxConstants.au3>
#RequireAdmin
;$settingfile = @ScriptDir & @CRLF & "\SysSettingsModifier_V4.2022\SysSettingsModifier.exe"
$settingfile = @WorkingDir & "\SysSettingsModifier_V4.2022\SysSettingsModifier.exe"
;$Path = "C:\PythonProject\PFA005_PDJeita2\SysSettingsModifier_V4.2022\SysSettingsModifier.exe"
;MsgBox($MB_SYSTEMMODAL, "", $settingfile & $Path)         ;????????????????
;MsgBox($MB_SYSTEMMODAL, "", @WorkingDir)
Run($settingfile)
;Run(@ScriptDir & @CRLF & "\SysSettingsModifier_V4.2022\SysSettingsModifier.exe")
;Run($Path)
;Run(@ProgramFilesDir & "\AutoIt3\AutoIt3Help.exe")
;Run(@WindowsDir & "\Notepad.exe", "", @SW_MAXIMIZE)

Local $hWin = WinWaitActive("Notifications", "", 2)
ControlFocus($hWin,"","[CLASS:Button; ID:7; INSTANCE:2]")
ControlClick($hWin, "","[CLASS:Button; ID:7; INSTANCE:2]")
;ControlFocus($hWin, "","[ID:7]")
;ControlClick($hWin, "","[ID:7]")
;ControlFocus($hWin, "", "Button2") ;yong ClassnameNN yexing
;ControlClick($hWin, "", "Button2");
; Wait for 1 seconds.
Sleep(1000)
Local $hWin = WinWaitActive("Notifications", "", 2)
;ControlFocus("Notifications","","[CLASS:Button; ID:6;  INSTANCE:1]")
;ControlClick("Notifications", "","[CLASS:Button; ID:6;  INSTANCE:1")
ControlFocus($hWin, "","[ID:6]")
ControlClick($hWin, "","[ID:6]")
; Wait for 1 seconds.
Sleep(1000)
Local $hWin = WinWaitActive("Notifications", "", 2)
;ControlFocus("Notifications","","[CLASS:Button;  ID:2;  INSTANCE:1]")
;ControlClick("Notifications", "","[CLASS:Button;  ID:2;  INSTANCE:1]")
ControlFocus($hWin, "","[ID:2]")
ControlClick($hWin, "","[ID:2]")
; Wait for 1 seconds.
Sleep(1000)

If  WinExists("SysSettingsModifier") Then
        
        WinActivate("SysSettingsModifier")        
        
EndIf 
Local $hWin = WinWaitActive("SysSettingsModifier", "", 2)
ControlFocus($hWin,"","[CLASS:WindowsForms10.BUTTON.app.0.141b42a_r6_ad1; INSTANCE:4]")
ControlClick($hWin, "","[CLASS:WindowsForms10.BUTTON.app.0.141b42a_r6_ad1; INSTANCE:4]")

Sleep(10000)
While 1
	If  WinExists("Notifications") Then
			WinActivate("Notifications")
			IniWrite(@WorkingDir & "\Times.ini","section1", "Progress", "SysSettingsModifier");chengshikaishiqianxuyaozai python zhong delete
			IniWrite(@WorkingDir & "\Times.ini","section1", "时间", @YEAR & "-" & @MON & "-" & @MDAY & " " & @HOUR & ":" & @MIN & ":" & @SEC)
			IniWrite(@WorkingDir & "\Times.ini","section1", "Restart", "1")
			;Return
			ExitLoop
	EndIf 
WEnd		