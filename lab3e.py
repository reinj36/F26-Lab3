# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 2/10/2026
# Purpose: Use of for loop
# Usage: ./lab3e.py

# Follow the specific instructions given in the README.md file

#create list of student names
students = ["Ama", "Elina", "Maija", "Daniel", "Ibrahim"]

#change element at index 1 to "Maggy"
students.insert(1, "Maggy")

#print each element on a separate line
for i in students :
    print(i) #you can just use the index as you are already iterating through students
             #(not students[i])