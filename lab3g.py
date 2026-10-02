# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 2/10/2026
# Purpose: Use of list and functions.
# Usage: ./lab3g.py

# Follow the specific instructions given in the README.md file

#create empty list
mylist= []

#create while loop to get user input until numbers is of size 6, and multiply each input by 10
while len(mylist) < 6 :
     number = int(input("Enter a number: ")) #convert input to int
     mylist.append(number*10) #multiply int by 10 and append to mylist
print("Current list: ", mylist)

#alternative format to multiply numbers by 10
#print(mylist)
#for i in mylist:
#     mylist[i]=mylist[i]*10

#print(mylist)


#print list in reverse order
mylist.reverse()
print("List in reverse: ", mylist)