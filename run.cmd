@echo off

:a

echo Activating virtual environment...
call venv\Scripts\activate

echo Running script...
python -B main.py

echo Deactivating virtual environment...
venv\Scripts\deactivate

pause
goto a