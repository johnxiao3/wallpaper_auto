:: setup command in cmd of windows:
:: schtasks /create /sc minute /mo 1 /tn "wallpaper auto" /tr C:\Users\XXXXX\run_python.bat

:: echo %time%
:: timeout 5 > NUL

set batdir=%~dp0
python %batdir%wallpaper_auto.py

:: echo %time%
:: timeout 5 > NUL
