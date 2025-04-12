"""
Created Date: 14/07/2024
Last Update: 04/08/2024
Description: Execute prompt command 'winget update --all --include-unknown' in administrator mode.
Observation: Command to update programs throw CMD (last line is available to create a executable)
"""
import ctypes
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def open_cmd_as_admin():
    if is_admin():
        subprocess.run("cmd /c winget update --all --include-unknown", shell=True)
    else:
        # Solicita privilegios elevados
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", "/c winget update --all --include-unknown", None, 1)

if __name__ == "__main__":
    open_cmd_as_admin()

# pyinstaller --onefile update_programms.py
