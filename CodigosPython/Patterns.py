"""
Created Date: 10/05/2025
Last Update: 17/05/2025
Description: Examples of patterns using loops
Observation: Simple code to make different shapes like a pyramid and diamond
"""

rows = 6
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