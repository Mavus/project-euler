#!/usr/bin/python

from eulib import is_prime, prime_generator

primes = prime_generator()
primesum = 0
p = 0
limit = 2000000

while True:
    if p < limit:
        primesum += p
        p = primes.next()
    else:
        print primesum
        exit(0)