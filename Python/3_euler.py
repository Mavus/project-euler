#!/usr/bin/python

product = 600851475143

def isPrime(n):
    i = 2
    while i <= (n / 2):
        if n % i == 0:
            return False
        i += 1
    else:
        return True 
def findPrimeFactors(m):
    n = 2
    while n <= m:
        print "Checking: ", n
        if m % n == 0 and isPrime(n):
            if isPrime(m):
                return m
            else:
                m = m / n
        else:
            n += 1

print findPrimeFactors(product)
