#!/usr/bin/pyton

primes = [ 2, 3, 5, 7, 11, 13, 17, 19 ]
step = reduce(lambda x, y: x * y, primes)
product = step

while True:
    for f in range(1,20):
        if product % f != 0:
            break
    else:
        print product
        exit(0)
    product += step