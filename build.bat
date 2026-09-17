@echo off
setlocal
cd /d "%~dp0"
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py -m pip install pyinstaller
pyinstaller --noconfirm --clean Via_ProMax.spec
if errorlevel 1 (
  echo.
  echo BUILD FAILED.
  pause
  exit /b 1
)
echo.
echo BUILD COMPLETE: dist\Via_ProMax\Via_ProMax.exe
echo.
pause
