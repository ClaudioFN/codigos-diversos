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

''' Hollow Diamond '''
print("\n Making the hollow diamond with *")
n = 5
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end=" ")
    for j in range(1, 2*i):
        if j == 1 or j == 2*i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(n-1, 0, -1):
    for j in range(1, n-i+1):
        print(" ", end=" ")
    for j in range(1, 2*i):
        if j == 1 or j == 2*i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

''' Hollow Square '''
print("\n Making the hollow square with *")
for i in range(rows):
    if i == 0 or i == rows - 1:
        print('*' * rows)
    else:
        print('*' + ' ' * (rows - 2) + '*')


''' Hour Glass '''
print("\n Making the hour glass with *")
n = 10
# Upper-Half
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()

# Lower-Half
for i in range(2, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()