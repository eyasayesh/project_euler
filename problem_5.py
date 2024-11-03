def prime_finder(num):
    #returns all primes less than or equal to num
    primes = []
    if num < 2:
        return primes
    else:
        for p in range(2,num+1):
            prime = True
            for factor in range(2,int(p**0.5)+1):
                if(p%factor == 0):
                    prime = False
                    break
            if prime: primes.append(p)

    return primes

def prime_dictionary(num):
    #return an empty dictionary with keys being all primes less than num
    primes = prime_finder(num)
    prime_dict = {}
    for prime in primes:
        prime_dict[str(prime)] = 0
    return prime_dict

def prime_factorization(num):
    #returns a dictionary of the counts of the prime factors of num
    prime_dict = prime_dictionary(num)
    factors = [int(key) for key in prime_dict.keys()]
    factor_ind = 0
    while(num > 1 and factor_ind < len(factors)):
        factor = factors[factor_ind]
        if(num%factor == 0):
            prime_dict[str(factor)] += 1
            num = num/factor
        else:
            if prime_dict[str(factor)] == 0: 
                prime_dict.pop(str(factor))
            factor_ind += 1
    if factor_ind < len(factors): 
        for i in range(factor_ind+1,len(factors)): prime_dict.popitem() 
    return prime_dict

def smallest_multiple(num):
    main_dict = prime_dictionary(num)
    for n in range(2,num+1):
        prime_factors = prime_factorization(n)
        for key in prime_factors.keys():
            if prime_factors[key] > main_dict[key]: main_dict[key] = prime_factors[key]  
    multiple = 1
    for key in main_dict.keys():
        multiple *= int(key)**main_dict[key]
    return multiple

print(smallest_multiple(20))