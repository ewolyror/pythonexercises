"""9/24/2019
e1.py
The first exercise of the python exercise series

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
Consider use range(#begin, #end) method
"""
#construct array of all the numbers
an=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        an.append(str(i))
print (','.join(an))
