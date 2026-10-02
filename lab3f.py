# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 2/10/2026
# Purpose: Use of two-dimensional lists
# Usage: ./lab3f.py

# Follow the specific instructions given in the README.md file

#code from example
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

element = matrix[1][2]  # Output: 6

#print element 5
print("Element 5: ", matrix[1][1])

#print element 2
print("Element 2: ", matrix[0][1])

#print element 9
print("Element 9: ", matrix[2][2])

#print individual lists
print("\nIndividual lists: ")
for i in matrix :
    print(i)