Set WshShell = WScript.CreateObject("WScript.Shell")
cmd = "python XXX\wallpaper_auto.py"
WshShell.Run cmd & Chr(34), 0 
Set WshShell = Nothing 

' schtasks /create /sc minute /mo 1 /tn "WP" /tr XXXX\run_wp.vbs
' schtasks /query /tn "WP"
' schtasks /delete /tn "WP"
