#!/usr/bin/python

import math

def isPalindrome(n):
    return str(int(n)) == str(int(n))[::-1]
    
a,b = 999,999
i = 1998

while i > 1:
    a,b = math.floor(i / 2.0),math.ceil(i /2.0)
    while b < 1000 and a > 0:
        if isPalindrome(a * b):
            print int(a), int(b), int(a*b)
            exit(0)
        else:
            a -= 1
            b += 1
    i -= 1

exit(1)