#!/usr/bin/python

for a in range (1,333):
    for b in range(a+1,1000-a):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            print (a,b,c)
            print 'abc = ', a*b*c
            exit(0)

print "nothing found"
exit(1)