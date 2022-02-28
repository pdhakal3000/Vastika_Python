"""
© https://sudipghimire.com.np
Recursive Function Exercises
1.
write a program to calculate the factorial of a non-negative number using recursive function
"""
# answer
#%%
def factorial(num):
    if num < 0:
        return f'This "{num}" is negative'
    if num ==0:
        return 1
    return num * factorial(num-1)
print(factorial(0))
print(factorial(1))
print(factorial(-10))
print(factorial(5))

#%%
"""
2.
Write a recursive function to take a number and calculate the sum of its digits.
"""
#%%
def sum_of_digits(num: int):
    if num<10:
        return num
    return sum_of_digits (num//10) + num%10


sum = sum_of_digits(4359)
sum = sum_of_digits(123456789)
print(sum)      # the output should be 21
#%%

"""
3.
Write a recursive function to find out the sum of first n natural numbers
"""
# answer
#%%
def sum_of_natural_number(n):
    if n ==1:
        return 1
    return n + sum_of_natural_number(n-1)

print(sum_of_natural_number(10))
print(sum_of_natural_number(1))
print(sum_of_natural_number(100))
#%%
"""
4.
write a recursive function to print out the nth element of a fibbonacci series below
series = [1, 1, 2, 3, 5, 8, 13, 21, 44, 65, ...]
example:
fib(6) should return 8
"""
# answer
#%%
def fibo(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return fibo(n-1) + fibo(n-2)
print(fibo(4))
print(fibo(6))

#%%

"""
5. try the same for the fibonnaccii series below
series = [4, 6, 10, 16, 26, 42, ...]
"""
# answer
#%%
def fibo(n):
    if n==1:
        return 4
    if n==2:
        return 6
    return fibo(n-1) + fibo(n-2)
print(fibo(4))
#%%