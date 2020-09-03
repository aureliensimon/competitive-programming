import sys

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

target = 600851475143

def primefactor (n):
    i = 2
    l = i

    while (i**2 <= n):
        while not(n % i):
            l = i
            n //= i
        i += 1
    
    if (n > l): return n
    else: return l

print(primefactor(target))