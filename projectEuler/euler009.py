import sys

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def uniqueTriplet (target):
    val = -1
    for a in range(1, int(target / 3)):
        b = int((target * (target - 2 * a)) / (2 * (target - a)))
        c = target - a - b
        if ((a**2 + b**2) == c**2) and (a*b*c > val):
            val = a * b *c
            break
    return val

n = 1000
print(uniqueTriplet(n))
