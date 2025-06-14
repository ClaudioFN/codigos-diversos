"""
Created Date: 10/05/2025
Last Update: 17/05/2025
Description: Examples of patterns using loops
Observation: Simple code to make different shapes like a pyramid and diamond
"""

rows = 14
cols = 6
''' Pyramid '''
print("\n Making a Pyramid with *")
for i in range(1, rows +1):
    print(" " * (rows - i) + "* " * i)

''' Diamond '''
print("\n Making a Diamond with *")
# Up part of the diamond 
for i in range(1, rows + 1) :
    print(" " * (rows -i) +  "* " * i)

# Lower part of the diamond
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
    
''' Square '''
print("\n Making a Square with X and O")
for i in range(rows):
    for j in range(cols):
        if(i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()


''' Triangles Opposing in the Vertical Orientation '''
print("\n Making Triangles with *")
# Up part of the triangle 
for i in range(1, rows + 1) :
    print("*" * i +  " " * (2 * (rows - i)) + "*" * i)

# Lower part of the diamond
for i in range(rows, 0, -1):
    print("*" * i + " " * (2 * (rows - i)) + "*" * i)

''' Triangles Opposing in the Horizontal Orientation '''
print("\n Making Triangles with *")
# Up part of the triangle 
for i in range(1, rows + 1) :
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Lower part of the diamond
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

''' June Festival flag in the Horizontal Orientation (needs 14 or a number divisible for 2)'''
print("\n Making the flag with *")
print("*" * rows, end="\n")
i = (rows // 2) - 1
j = 2
while i != 0:
    while j <= (rows - 2):
        print("*" * i, end="")
        print(" " * j, end="")
        print("*" * i, end="\n")
        i = i - 1
        j = j + 2