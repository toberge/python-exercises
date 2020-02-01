#!/usr/bin/env python3
from math import sqrt, floor

# Simple implementation of the Sieve of Erasthothenes
def erasthothenes(n):
    # Fill an array with markers
    is_prime = [True] * n
    
    for i in range(2, floor(sqrt(n))):
        # If this number is prime
        if is_prime[i-1]:
            # Start marking all multiples of this number as non-prime
            # - because they must all be divisible by this prime!
            index = i*i - 1
            while index < n:
                is_prime[index] = False
                index += i

    numbers = []

    # Find the numbers that are primes
    for i in range(1, n):
        if is_prime[i]:
            numbers.append(i + 1)
    
    return numbers

# Finding the first 1000 prime numbers
#print(len(erasthothenes(8000)[:1000]))

for prime in erasthothenes(8000)[:1000]:
    print(prime)
