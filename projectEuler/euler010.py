import sys

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

x = 2000000

def is_prime (n):
    for i in range(2, int(n ** 0.5) + 1):
        if not (n % i):
            return False
    else:
        return True

def solve (l):
    sum = 0
    for p in range(1, l):
       if p > 1 and is_prime(p):
           sum += p
    return sum

print(solve(x))
