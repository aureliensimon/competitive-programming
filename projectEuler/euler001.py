import sys

'''
Multiples of 3 and 5 :

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def ar(a):
    return a * (a + 1)

n = 1000

a = int(n / 3)
b = int(n / 5)
c = int(n / 15)

print(int(int(3*ar(a) + 5*ar(b) - 15*ar(c) >> 1)) - n)
