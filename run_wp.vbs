Set WshShell = WScript.CreateObject("WScript.Shell")
cmd = "python C:\Users\XXXX\wallpaper_auto.py"
WshShell.Run cmd & Chr(34), 0 
Set WshShell = Nothing 
