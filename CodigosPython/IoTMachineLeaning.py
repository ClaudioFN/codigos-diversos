"""
Created Date: 22/10/2022
Last Update: 10/11/2024
Description: Recognizes voices
Observation: Using the microphone to caught voice chat and transform it into text
"""
# This Python file uses the following encoding: iso-8859-15 -*-
import speech_recognition as sr
import os 
import time

# Ouvir e Reconhecer falas 
def ouvir_microne():
    # Habilitar uso audio do microfone
    microfone = sr.Recognizer()

    # Captar o audio do microfone
    with sr.Microphone() as source:
        # Algoritmo pre existente para tratar da reducao de ruidos
        microfone.adjust_for_ambient_noise(source)
        # Frase de aviso
        print("Diga algo!")

        # Armazenar o que foi dito
        audio = microfone.listen(source)
    
    try:
        # Reconhecer padroes de fala em uma determinada lingua
        frase = microfone.recognize_google(audio, language='pt-BR')

        print("Sua frase: " + frase)

        # Dar um tempo apos mostrar a frase dita para que o usuario tenha nocao do que disse
        time.sleep(3)

        # Abrir programas
        if "opera" in frase or "navegador" in frase:
            os.system("start opera.exe")
        elif "google chrome" in frase or "chrome" in frase:
            os.system("start Chrome.exe")
        elif "word" in frase:
            os.system("start WINWORD.EXE")
        elif "power point" in frase or "powerpoint" in frase:
            os.system("start POWERPNT.EXE")
        elif "excel" in frase:
            os.system("start Excel.exe")

    except sr.UnknownValueError:
        print("N�o consegui compreender o que foi dito!")

        return frase

# Chamada da funcao definida acima
ouvir_microne()