@echo off
set PYFILE=bot.py
set SYNC_FOLDER="G:\My Drive\bots"

pyinstaller --onefile --noconfirm --distpath %SYNC_FOLDER% %PYFILE%
echo Build complete. EXE saved to %SYNC_FOLDER%
pause