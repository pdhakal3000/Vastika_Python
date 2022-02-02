"""
© https://sudipghimire.com.np

Type-casting and Hinting Exercises

Please read the note carefully and try to solve the problem below:

"""


"""
1. Type Hinting
    a. create a variable <odd> with hinting as `int` and assign a value to it.
    b. create a variable <PI> with hinting as `float` and assign 3.1415 to it.

    c. create any variable with `string` type hinting and assign `integer` value to it.
        - Check whether the program gives error in execution or not.
        - If it gives or does not give error, then why it gives or does not give error?
"""
#%% 1a create a variable <odd> with hinting as `int` and assign a value to it.

odd:int = 10

#%%Answer 1b create a variable <PI> with hinting as `float` and assign 3.1415 to it.

PI: float = 3.1415

#%% Answer 1c
string:str = 5 # integer 5 is hinted as str
print(string) # just printing output
print(type(string)) # Checking type of the variable string.

# Hinting in python programming is not forcefull to do whatever we hint rather 
# it goes with its own internal guidence and recognise the type of value and process accordingly further.

#%%
"""
2. Type Conversion
"""
# ----------------------------------------[ a ]-----------------------------------------------
#%%
PI = 3.1415
# I want to print the value of PI to be 3. How should I convert the data to an integer
PI_int = int(PI)
print(PI_int)
# ----------------------------------------[ b ]-----------------------------------------------
#%%
str_1 = "20"
str_2 = "30"

print(str_1 + str_2)
# above line gives us output of "2030" but I want the answer to be 50.
# How would you solve the problem using type conversion?
print(f'Here is the answer after type conversion : {int(str_1) + int(str_2)} ')

#%%
# ----------------------------------------[ c ]-----------------------------------------------
x = ['1', '2', '3', '4', '5']
sum = 0
"""
- I want the value of sum to be 15.
- The way I get 15 is by adding all items from the list `x`.

Hint: the addition may involve
- for loops in the list
- type conversion
"""
for i in x :
    sum += int(i)

print(f'{sum} is sum of the elements of the list x after type conversion.')


# ----------------------------------------[ d ]-----------------------------------------------
#%%
odd = [1, 3, 5, 7, 9, 11, 13, 15]
prime = [2, 3, 5, 7, 11, 13, 17]
"""
use type conversion to these lists to appropriate data type and find out
    - numbers that are odd but not prime
    - numbers that are either odd or prime
    - numbers that are prime but not odd.

Final values should be converted into list again and stored to variables.
"""
# Changing list odd and prime to the sets for the operations.
odd_set = set(odd.copy())
#print(odd_set)
prime_set = set(prime)
#(prime_set)

# print(f'This is the set of odd not prime: \n {odd_set.difference(prime_set)}')
# print(f'This is the set of either odd or prime: \n {odd_set.union(prime_set)}')
# print(f'This is the set of prime not odd: \n {prime_set.difference(odd_set)}')

odd_only = list(odd_set.difference(prime_set))
either_odd_or_prime = list(odd_set.union(prime_set))
prime_not_odd = list(prime_set.difference(odd_set))

print(f'This is the list of odd not prime: \n {odd_only} \n')
print(f'This is the list of either odd or prime: \n {either_odd_or_prime} \n')
print(f'This is the list of prime not odd: \n {prime_not_odd} \n')

# %%
