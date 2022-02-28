"""
© https://sudipghimire.com.np
Lambda Exercises
"""


"""
1.
Convert the following function to a lambda function
"""
def odd_or_even(num):
    if num%2==0:
        return 'even'
    else:
        return 'odd'

# answer
#%%
odd_or_even = lambda num: "Even" if (num%2==0) else "odd"

print(odd_or_even(6))
print(odd_or_even(7))
#%%

"""
2.
Create a lambda that accepts a list of numbers and return the list of squares of them
hint:
you can use list comprehension to return the list of squares
"""
#answer
#%%
squre = lambda num : [element **2 for element in num]
print(squre([4,5,6]))
#%%

"""
3.
create a lambda function that converts the length from meter to feet
"""
# answer
#%%
m_to_f = lambda m: (f' The equivalent measure of meter in the feet is : {m*3.28}')
print(m_to_f(5))
#%%
"""
4.
Create a lambda function that takes an argument and finds out the square if it is even and cube if it is odd.
"""
# answer
#%%
square_or_cube = lambda num : f' The square of the even number {num} is: {num**2}' if (num%2==0) else f'The cube of the odd  number {num} is: {num**3}'
print(square_or_cube(7))
print(square_or_cube(8))

#%%


"""
5.
Create a lambda function `get_date` that takes 3 arguments month, year, and day that
returns a single string in a "YY/MM/DD" format.
"""
# answer

# uncomment below when you solve problems
# print(get_date(2001, 12, 14))    # "2001/12/14"
#%%
get_date = lambda year, month, day : f' Corresponding date is: "{year}/{month}/{day}"'
print(get_date(2001, 12, 14))
#%%

"""
6.
Create a lambda function that accepts a sentence that returns the sentence with spaces replaced by hyphens
example:
input => "A quick brown fox jumps over the lazy dog."
output => "A-quick-brown-fox-jumps-over-the-lazy-dog."
hint:
use string.replace() method
"""
# answer
#%%
input = "A quick brown fox jumps over the lazy dog."
hyphened = lambda input : input.replace(" ", '-')
print(hyphened(input))

#%%
 
"""
7.
Create a lambda function that checks whether the string provided is a number or not
"""
# answer
#%%
number_or_not = lambda m : f'Yes, "{m}" it is numeric.'if (m.isnumeric() ==True) else f'"{m}" It is not numeric.'
print(number_or_not('5'))
print(number_or_not("Prakash"))

#%%


"""
8. create a lambda function to count total number of even numbers in a list
"""
# answer
#%%
even_number_count = lambda list1: f'Total number of even element in the list is: {len([num for num in list1 if (num%2==0)])}'
print(even_number_count([5,10,15,16,17,18,20,25,30,35]))


#%%