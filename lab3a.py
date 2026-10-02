# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 2/10/2026
# Purpose: Use of sort list method and random module
# Usage: ./lab3a.py

#import module
import random 

#create variable to use module
r = random

#create a list of 20 random ints between 0 and 99
my_list = r.sample((range (0, 100)), 20)

#print generated list
print("List: ", my_list)

#sort my_list
my_list.sort()

#print sorted list
print("Sorted list: ", my_list)
