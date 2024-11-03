def sum_square_difference(n):
    #difference between he sum of the squares of the first n numbers and the square of the sum
    n_arr = [i for i in range(1,n+1)]
    n_sqr = [i**2 for i in range(1,n+1)]
    return sum(n_arr)**2 - sum(n_sqr) 
print(sum_square_difference(100))