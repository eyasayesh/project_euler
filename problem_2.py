#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fib_sum = 2
fib_buffer = [1,2]
next_fib = 2
while (next_fib <= 4e6):
    next_fib = sum(fib_buffer)
    fib_sum += next_fib if next_fib%2== 0 else 0
    fib_buffer[0] = fib_buffer[1]
    fib_buffer[1] = next_fib
print(f"The answer is {fib_sum}")