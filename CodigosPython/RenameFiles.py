"""
Created Date: 26/02/2024
Last Update: 26/02/2024
Description: Rename files in a directory adding a sequential number to the end of the name of the file
Observation: It will rename every file from the given directory
"""
import os
import sys

numberConcat = 1

for fileName in os.listdir('./test'):
    fileData = str(fileName).split(".")
    fileFullName = ""
    # If the name have more than one dot, this area will concatenate everything before the last dot
    if len(fileData) > 2:
        for index, details in enumerate(fileData): 
            if index == len(fileData) - 1:
                continue
            else:
                fileFullName += details
    else:
    # If the name have only one dot, the text before the dot will just be assigned to the variable
        fileFullName = fileData[0]
    
    # With the full name, concatenate with a number starting with 1
    fileNewName = fileFullName + "_" + str(numberConcat) + "." + fileData[len(fileData)-1]
    
    os.rename("./test/"+fileName, "./test/"+fileNewName)
    print(f"\nFile {numberConcat} with name {fileName} changed to {fileNewName}")
    numberConcat += 1