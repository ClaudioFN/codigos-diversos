"""
Created Date: 23/12/2023
Last Update: 16/11/2024
Description: Change a audio recorded to another tone
Observation: It can record and change the voice recorded to another tone
"""
# pip install pydub sounddevice numpy
# pip install pyaudio

from pydub import AudioSegment
from pydub.playback import play
import sounddevice as sd
import numpy as np
import sys

# Funcao para gravar o audio
def record_audio(time=5, sample_rate=44100):
    print("Gravação Iniciada!")
    audio_data = sd.rec(int(sample_rate * time), 
                        samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()
    print("Gravação Concluída!")
    
    return AudioSegment(
        audio_data.tobytes(),
        frame_rate=sample_rate,
        sample_width=audio_data.dtype.itemsize,
        channels=1
    )
    
# Funcao para alterar o tom da voz
def modify_pitch(audio, tom=2):
    # Alterar o tom da voz
    pitched_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * (2 ** (tom/12.0)))
    })
    
    # Ajustar a taxa de quadros para manter a velocidade original do audio
    pitched_audio = pitched_audio.set_frame_rate(audio.frame_rate)
    
    return pitched_audio

# Funcao Principal
def main(time, tom):
    
    # Gravar o audio
    audio = record_audio(time)
    
    # Alterar o tom da voz do audio gravado (alterar parametro para ajuste do calibre)
    pitched_audio = modify_pitch(audio, tom)
    
    # Reproduz a voz com o tom alterado e mantem a velocidade original
    print(f"Reproduzindo voz com tom alterado...")
    play(pitched_audio)
    
if __name__ == "__main__":
    time = int(sys.argv[1])
    tom = int(sys.argv[2])
    main(time, tom)
    