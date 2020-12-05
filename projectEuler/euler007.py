import sys

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
x = 10001

def is_prime (n):
    for i in range(2, int(n ** 0.5) + 1):
        if not (n % i):
            return False
    else:
        return True

def solve (limit):
    nb_primes = 0

    for p in range(1, 1000000):
       if p > 1 and is_prime(p):
           nb_primes += 1
           if (nb_primes >= limit): return p

print(solve(x))
