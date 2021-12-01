@echo off

echo Setting up virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Updating pip...
python -m pip install --upgrade pip

echo Installing requirements...
pip install -r requirements.txt

echo Done!
pause