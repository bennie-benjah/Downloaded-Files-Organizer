@echo off

REM Run the Python script using pythonw (for GUI applications)
pythonw "C:\Users\Bee_gee\Desktop\SORT FILES\index.py"

REM Display a message box using VBScript
echo MsgBox "Files have been organized.", vbOKOnly, "File Organization" > "%temp%\popup.vbs"
cscript /nologo "%temp%\popup.vbs"
del "%temp%\popup.vbs"
