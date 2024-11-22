@echo off
setlocal

set /p name=Elige el nombre de la distro: 

wsl --import %name% C:\Users\%USERNAME%\distros\%name% .\images\ubuntu.tar

wsl -d %name%
::endlocal
