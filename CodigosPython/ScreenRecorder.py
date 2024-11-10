"""
Created Date: 09/12/2023
Last Update: 10/11/2024
Description: Record the screen with sound and with MKV extension
Observation: Using a Webcam and libraries to do a face recognition
"""

# pip install opencv-python 
# pip install numpy
# pip install pyautogui
import cv2 as c
import numpy as np
import pyautogui as auto
import os

# To not substitute the file
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

timeLimit = True
# Define the sizer of the screen
screenSize = (1920, 1080)

# FourCC is a 4-byte code used to specify the video codec. 
fourcc = c.VideoWriter_fourcc(*"XVID")

# Name the file and define the rest of the required items
# filename: gravacao.avi
# fourcc: fourcc
# fps: 30.0
# frameSize: (screenSize)
fileName = input("Indique o nome do arquivo: ")
while True:
    anyFileFound = find(fileName+".mkv", os.getcwd())
    if anyFileFound:
        fileName = input("Nome " + fileName + " já em uso. Indique outro: ")
    else:
        break
    
out = c.VideoWriter(fileName+".mkv", fourcc, 30.0, (screenSize))
while True:
    img = auto.screenshot()
    frame = np.array(img)
    frame = c.cvtColor(frame, c.COLOR_BGR2RGB)
    out.write(frame)
    
    if c.waitKey(1) == ord("q"):
        break
    
c.destroyAllWindows()
out.release()