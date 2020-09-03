import sys

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

allp = [1]

def pgcd (a, b):
    if (b == 0): return a
    c = a % b
    return pgcd(b , c)

def ppcm (a, b):
    return int(abs(a * b) / pgcd(a, b))

def fillAllp ():
    for i in range(2,40):
        allp.append(ppcm(i, allp[i - 2]))

fillAllp()

n = 20
print(allp[n - 1])
