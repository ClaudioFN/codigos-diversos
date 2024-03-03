"""
Created Date: 26/02/2024
Last Update: 26/02/2024
Description: Rename files from a directory adding a sequential number to the end of the name of the file
Observation: It will rename every file from the given directory
"""
import os
import sys

numberConcat = 1

for fileName in os.listdir('./test'):
    fileData = str(fileName).split(".")
    fileFullName = ""
    if len(fileData) > 2:
        for index, details in enumerate(fileData): 
            if index == len(fileData) - 1:
                continue
            else:
                fileFullName += details
    else:
        fileFullName = fileData[0]
    
    fileNewName = fileFullName + "_" + str(numberConcat) + "." + fileData[len(fileData)-1]
    
    os.rename("./test/"+fileName, "./test/"+fileNewName)
    print(f"\nFile {numberConcat} with name {fileName} changed to {fileNewName}")
    numberConcat += 1