import sys

'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def findPalindrome ():
    palindrome = []
    
    for i in range(101, 999):
        for j in range(101, 999):
            p = i * j

            if (len(str(p)) ==  6) and (str(p) == str(p)[::-1]) and (p not in palindrome):
                palindrome.append(p)
    
    return max(palindrome)

print(findPalindrome())

