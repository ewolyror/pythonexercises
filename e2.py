"""9/24/2019
e2.py
The second exercise of the python exercise series

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
import numpy as np
l=[]
f=float(input("What integer for factorial?"))
while f>1:
    l.append(f)
    f=f-1
f1=np.prod(l)
print(f1)
