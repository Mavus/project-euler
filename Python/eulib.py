#!/usr/bin/python

from math import sqrt

def is_prime(n):
    if n == 2 : return True
    i = 2
    while i <= (int(sqrt(n) + 1)):
        if n % i == 0:
            return False
        i += 1
    else:
        return True 

def prime_generator(n=2):
    while True:
        if is_prime(n):
            yield n
        if n == 2:
            n += 1
        else: 
            n += 2

def nth_prime(N):
    primes = prime_generator()
    number_of_primes = 0
    while True:
        n = primes.next()
        if is_prime(n):
            number_of_primes += 1
            if number_of_primes == N: return n
