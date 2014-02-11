#!/usr/bin/python

sum_square = 0
for i in range(1,101):
    sum_square = sum_square + (i * i)
print "sum_square= ", sum_square

sum = sum(range(1,101))
square_sum = sum * sum
print "square_sum= ", square_sum

diff = square_sum - sum_square
print "diff= ", diff