#Find the largest palindrom made from the product of two 3-digit numbers

# I can't think of a way other than brute force
from math import log10
def is_palindrome(num):
        digits = int(log10(num)+1)
        