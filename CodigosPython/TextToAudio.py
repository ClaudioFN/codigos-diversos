# pip install gtts
# pip install playsound
# Maybe you will need pip install wheel before the playsound installation

from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'pt-br'

sp = gTTS (
    text='Text to audio using Python.',
    lang=language
)

sp.save(audio)
playsound(audio)