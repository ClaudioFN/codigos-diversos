"""
Created Date: 24/08/2021
Last Update: 26/04/2025
Description: Open a program using que path to the executable
Observation: Simple code to open programs in the computer
"""

import subprocess, os
# Aqui em subprocess abrimos um executavel colocando o caminho ate ele
subprocess.Popen('CAMINHO DO EXECUTAVEL')

# Aqui em path colocamos o caminho fisico de uma pasta para abrir ela
path = "CAMINHO DA PASTA"
path = os.path.realpath(path)
os.startfile(path)