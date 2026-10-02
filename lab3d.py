# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 2/10/2026
# Purpose: Practice adding and removing elements in list.
# Usage: ./lab3d.py

# Follow the specific instructions given in the README.md file

#create list and print
mylist = [1, 2, 3, 4, 5, 6]
print("Original list: ", mylist)

#append '7' to mylist and print
mylist.append(7)
print("List after append: ", mylist)

#insert '0' at index 0 of mylist and print
mylist.insert(0, 0)
print("List after insert: ", mylist)

#remove element from index 2 of mylist and print
mylist.pop(2)
print("List after pop: ", mylist)


#find index of element 6 in mylist and print
print("The element 6 is present at the index ", mylist.index(6), ".")

