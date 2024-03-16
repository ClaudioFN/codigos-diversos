"""
Created Date: 16/03/2024
Last Update: 16/03/2024
Description: Menu to define which kind o change menu shall be used
Observation: -
"""
import RenameFiles
import time

print('Welcome to Rename Files Menu!')
time.sleep(2)

option = 0
while option != 10:
    print('\nMENU')
    print('Choose an option: ')
    print('1. Rename all files of a folder by adding 1 in the end 1')
    print('10. Exit')
    option = int(input())
    if option == 1: 
        fName = input('Give the folder name: ')
        RenameFiles.renameFilesWithOne(fName)
        print('--------------------------------------------------')
    elif option == 10:
        print('Bye!')
    else:
        print('Invalid selection. Try again!')
