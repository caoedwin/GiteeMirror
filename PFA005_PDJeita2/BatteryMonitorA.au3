
#include <File.au3>
#include <MsgBoxConstants.au3>
#RequireAdmin
;MsgBox($MB_SYSTEMMODAL, "", @WorkingDir &@ScriptDir)
;$settingfile = @ScriptDir & @CRLF & "\SysSettingsModifier_V4.2022\SysSettingsModifier.exe"
$Path = @ScriptDir & "\New Battery Manager\BatteryManager.exe"
$Path_video = @WorkingDir & "\JB2_0.mp4"
$Path_player = "C:\Program Files\WindowsApps\Microsoft.ZuneVideo_10.22041.10091.0_x64__8wekyb3d8bbwe\Video.UI.exe"

FileChangeDir(@ScriptDir)
Run($Path)
Sleep(1000)
If  WinExists("BattManager") Then
        
        WinActivate("BattManager")       

        
EndIf 
Local $hWin = WinWaitActive("BattManager", "", 2)
ControlFocus($hWin,"","[NAME:button1]")
ControlClick($hWin, "","[NAME:button1]")

Sleep(1000)
FileChangeDir(@ScriptDir)
;MsgBox($MB_SYSTEMMODAL, "", @WorkingDir&@ScriptDir)
Run("openvideo.bat")
Sleep(2000)
Send("{ENTER}")
Sleep(1000)
Send("{ENTER}")
Sleep(6000)
Send("{LWIN}")
Sleep(1000)
Send("{LWIN}")
Sleep(1000)
Local $hWin = WinWaitActive("[CLASS:ApplicationFrameWindow]" , "", 10)
If  WinExists("[CLASS:ApplicationFrameWindow]") Then
        
        WinActivate("[CLASS:ApplicationFrameWindow]")    
EndIf 
Sleep(1000)
Send("{CTRLDOWN}") 
Sleep(500)
Send("{T}")
Sleep(500)
Send("{CTRLUP}") 
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
;Sleep(1000)
Send("{TAB 7}") 

;MsgBox($MB_SYSTEMMODAL, "", $cmdyj)



			
IniWrite(@ScriptDir & "\Times.ini","section2", "Progress", "Time A")
IniWrite(@ScriptDir & "\Times.ini","section2", "时间", @YEAR & "-" & @MON & "-" & @MDAY & " " & @HOUR & ":" & @MIN & ":" & @SEC)
IniWrite(@ScriptDir & "\Times.ini","section1", "Restart", "2")

;IniWrite(@WorkingDir & "\Times.ini","section3", "Progress", "Time B")
;IniWrite(@WorkingDir & "\Times.ini","section3", "时间", @YEAR & "-" & @MON & "-" & @MDAY & " " & @HOUR & ":" & @MIN & ":" & @SEC)
;IniWrite(@WorkingDir & "\Times.ini","section1", "Restart", "3")
