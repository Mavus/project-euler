#!/usr/bin/python

from math import sqrt

def isPrime(n):
    if n == 2 : return True
    i = 2
    while i <= (int(sqrt(n / 2) + 1)):
        if n % i == 0:
            return False
        i += 1
    else:
        return True 

def primeGenerator(n=2):
    while True:
        if isPrime(n):
            yield n
        if n == 2:
            n += 1
        else: 
            n += 2

def nthPrime(N):
    primes = primeGenerator()
    number_of_primes = 0
    while True:
        n = primes.next()
        if isPrime(n):
            number_of_primes += 1
            if number_of_primes == N: return n