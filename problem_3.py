#prime_factorization!
#What is the largest prime factor of the number 600851475143?

def largest_prime(number):
    for factor in range(2,int(number**0.5)+1):
        if number%factor == 0:
            lpf = max([largest_prime(factor),largest_prime(int(number/factor))])
            return lpf
    return number

lpf = largest_prime(600851475143)
print(f"The largest prime factor of 600851475143 is {lpf}")
