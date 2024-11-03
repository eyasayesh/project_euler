#Find the largest palindrom made from the product of two 3-digit numbers

# I can't think of a way other than brute force
from math import log10


#flip number
def flip_num(num):
        order = int(log10(num))+1
        flipped_num = 0
        for o in range(1,order+1):
                flipped_num += (num%10)*10**(order-o)
                num = int(num/10)
        return flipped_num

#print(flip_num(1))
#print(flip_num(102))
#print(flip_num(3223))


#verify if it is a palindrome
def is_palindrome(num):
        #order of magnitude
        flipped_num = flip_num(num)
        return flipped_num == num

#print(is_palindrome(1))
#print(is_palindrome(102))
#print(is_palindrome(3223))

#generate all palindromes between min and max digit counts  
def generate_palindromes(min_digits = 1, max_digits = 1):
        palindromes = []
        if min_digits > max_digits:
            max_digits = min_digits
        for digits in range(min_digits, max_digits+1):
                half_digits = int(digits/2)
                if digits == 1:
                        palindromes = palindromes + [d for d in range(1,10)]
                else:
                    for n in range(10**(half_digits-1),10**half_digits):
                            #odd number of digits
                            if(digits%2 == 0):
                                palindromes.append(n*10**(half_digits)+flip_num(n))
                            else:
                                for d in range(10):
                                    palindromes.append(n*10**(half_digits+1)+d*10**(half_digits)+flip_num(n))
        return palindromes

"""
print(generate_palindromes())
print(generate_palindromes(2,1))
print(generate_palindromes(2,3))
print(generate_palindromes(4,4))
print(generate_palindromes(4))
print(generate_palindromes(7))"""

largest_prod = 999*999
smallest_prod = 100*100
max_digits = int(log10(largest_prod))+1
min_digits = int(log10(smallest_prod))+1

palindromes = generate_palindromes(min_digits,max_digits)
palindromes.reverse()
break_con = False
for palindrome in palindromes:
    for factor in range(999,99,-1):
            if palindrome%factor == 0 and int(log10(palindrome/factor)) == 2:
                  print(palindrome)
                  break_con = True
                  break
    if(break_con): break