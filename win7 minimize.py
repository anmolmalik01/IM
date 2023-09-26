# =================== can be run on windows

import psutil
import subprocess

def startProgram():
    SW_HIDE = 0
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = SW_HIDE
    subprocess.Popen(r'C:\test.exe', startupinfo=info)
startProgram()


# def startProgram():
#     SW_MINIMIZE = 6
#     info = subprocess.STARTUPINFO()
#     info.dwFlags = subprocess.STARTF_USESHOWWINDOW
#     info.wShowWindow = SW_MINIMIZE
#     subprocess.Popen(r'C:\test.exe', startupinfo=info)
# startProgram()
