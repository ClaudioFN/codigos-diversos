import subprocess, os
# Aqui em subprocess abrimos um executavel colocando o caminho ate ele
subprocess.Popen('CAMINHO DO EXECUTAVEL')

# Aqui em path colocamos o caminho fisico de uma pasta para abrir ela
path = "CAMINHO DA PASTA"
path = os.path.realpath(path)
os.startfile(path)