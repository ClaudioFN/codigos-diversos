"""
Created Date: 10/12/2023
Last Update: 16/11/2024
Description: Recorder for audio
Observation: After setting a time limit for recording, the record starts till the time is reached
"""
# pip install sounddevice
# pip install scipy

import sounddevice
from scipy.io.wavfile import write
import time
import os

# Tempo de Gravacao
fs=44100
second = int(input("Quantos segundos de gravação devem ser efetuados? "))
minutes = 0
totalSeconds = 0

# Gravacao
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
for s in range(second):
    totalSeconds += s
    if totalSeconds == 60:
        minutes += 1
        totalSeconds = 0
    time.sleep(1)
    os.system('cls')
    print(f"Gravação em {minutes}:{s+1:02}")
    

sounddevice.wait()


    
# Salvar
write("gravacao.wav", fs, record_voice)
print("Gravação Concluída!")