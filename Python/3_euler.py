#!/usr/bin/python

product = 600851475143
prime_factors = []

def isPrime(n):
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True

def findPrimeFactors(m):
    n = 2
    while n < m:
        if m % n == 0:
            if isPrime(n):
                prime_factors.append(n)
                findPrimeFactors(m / n)
        n += 1
    else:
        prime_factors.append(m)

findPrimeFactors(product)

print max(prime_factors)