# pip install gtts
# pip install playsound
# Some cases, when the installation of playsound fail, install 'pip install wheel' before the playsound installation

from gtts import gTTS
from playsound import playsound
import os

# Look for any archive with the same name
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

audio = input("Nome do arquivo MP3 que será criado? ")
while True:
    anyFileFound = find(audio+".mp3", os.getcwd())
    if anyFileFound:
        audio = input("Nome " + audio + " já em uso. Indique outro: ")
    else:
        break

# Witch language should the voice of the translation use
language = 'pt-br'

textToAudio = input("Digite o texto para execução: ")
while True:
    if !textToAudio || textToAudio == "":
        audio = input("Texto vazio. Digite o texto para execução: ")
    else:
        break

# Create the audio using the text typed above
sp = gTTS (
    text=textToAudio,
    lang=language
)

# Save the audio of the converted text
sp.save(audio)

# Play the audio
playsound(audio)