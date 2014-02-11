#!/usr/bin/python

fib1 = 1
fib2 = 2
fibsum = 0

for i in range(1,4000000):
    if fib2 > 4000000:
        print fibsum
        exit(0)
    if fib2 % 2 == 0:
        fibsum += fib2
    fib1, fib2 = fib2, fib1 + fib2
exit(1)