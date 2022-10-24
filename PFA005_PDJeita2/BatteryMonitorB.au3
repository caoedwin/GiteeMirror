
#include <File.au3>
#include <MsgBoxConstants.au3>
#RequireAdmin
;$settingfile = @ScriptDir & @CRLF & "\SysSettingsModifier_V4.2022\SysSettingsModifier.exe"
$Path = @WorkingDir & "\New Battery Manager\BatteryManager.exe"

Run($Path)
Sleep(1000)
If  WinExists("BattManager") Then
        
        WinActivate("BattManager")        
        
EndIf 
Local $hWin = WinWaitActive("BattManager", "", 2)
ControlFocus($hWin,"","[NAME:button1]")
ControlClick($hWin, "","[NAME:button1]")

			
;IniWrite(@WorkingDir & "\Times.ini","section2", "Progress", "Time A")
;IniWrite(@WorkingDir & "\Times.ini","section2", "时间", @YEAR & "-" & @MON & "-" & @MDAY & " " & @HOUR & ":" & @MIN & ":" & @SEC)
;IniWrite(@WorkingDir & "\Times.ini","section1", "Restart", "2")

IniWrite(@WorkingDir & "\Times.ini","section3", "Progress", "Time B")
IniWrite(@WorkingDir & "\Times.ini","section3", "时间", @YEAR & "-" & @MON & "-" & @MDAY & " " & @HOUR & ":" & @MIN & ":" & @SEC)
IniWrite(@WorkingDir & "\Times.ini","section1", "Restart", "3")
