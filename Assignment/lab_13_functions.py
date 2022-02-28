"""
© https://sudipghimire.com.np
Function Exercises
"""

"""
1. Write a python function to find the largest out of 3 numbers
You should use comparison operator to find out the maximum of 3 numbers.
"""
# answer
#%%
from tkinter.messagebox import YES


def largest_num(a,b,c):
    if a >= (b and c):
        return print(f' {a} is largest among three numbers.')
    elif b >= (a and c):
        return print(f' {b} is largest among three numbers.')
    else:
        return print(f' {c} is largest among three numbers.')

largest_num(100,15,100)

#%%


"""
2. Write a python function that calculates the number of upper case characters, lower case characters
 and spaces in the string and returns them as a tuple.
for example
x = "A Quick Brown Fox Jumps Over The Lazy Dog."
Number of upper case characters: 9
Number of lower case characters: 14
Number of spaces: 8
"""
#%%
def count(a:str):
    upper_case = 0
    lower_case = 0
    spaces = 0
    for letter in a :
        if letter.isupper() == True:
            upper_case +=1
        
        if letter.islower() == True:
            lower_case +=1
        
        if letter == " ":
            spaces +=1
             
    print(f'Numbers of upper case character are: {upper_case}')
    print(f'Numbers of lower case character are: {lower_case}')
    print(f'Numbers of spaces are: {spaces}')

count("A Quick Brown Fox Jumps Over The Lazy Dog.")

#%%

'''
3.
Suppose you went to a coffee shop. A shopkeeper asked you to create a program that serves coffee
according to the customer's requirements.
The coffee machine should ask user to enter any numbers below that should make a coffee and serve it to the user.
Please use the `make_coffee()` function below to prepare a coffee and serve it.
Followings are the ingredients for coffee:
Sugar: no. of spoons
beans: no. of spoons
milk: volume in ml.
The total volume of coffee should be 250ml. The maximum volume of milk can be only upto  150ml. greater than that
should give the error saying not acceptable.
Finally print the line describing the coffee you prepared along with  milk and water composition.
'''
# answer
#%%
def make_cofee():
    print('Wellcome in our coffee shop. please follow the instruction for your composition of cofee from console:')
    sugar = int(input(f'How many spoon of sugar would you like to put in your cofee?'))
    beans = int(input(f'How many spoon of grinded cofee beans would you like to put in your cofee?'))
    milk =0
    while milk<=150:
        milk = int(input(f'How much milk in ml would you like to put in your cofee [only allowed max 150 ml]?'))
        if milk <=150:
            print (f'Your coffe is ready with {milk} ml milk and {250-milk} water.\n Thank you and enjoy your coffee.')
            break
    else:
        print(f'The max amount of milk you are allowed in your coffe is 150 ml.')

make_cofee()


#%%
"""
4.
Write a program to create a multiplication table of the given number.
The `mul_table()` function should have the following arguments:
- `number`: the number to print multiplication table of.
- `limit`: the number upto which multiples are printed which should have the default value of 10
Multiplication table for 13
| 13  X   1|    13|
| 13  X   2|    26|
| 13  X   3|    39|
| 13  X   4|    52|
| 13  X   5|    65|
| 13  X   6|    78|
| 13  X   7|    91|
| 13  X   8|   104|
| 13  X   9|   117|
| 13  X  10|   130|
"""
# Answer Here
#%%
def mul_table (number:int, limit:int):
    for num in range(1, limit+1):
        print(f'| {number}  x  {num}|  \t{number*num}|')
mul_table(13,10)

#%%

"""
5.
Write a function that takes a string and checks whether the word is palindrome or not.
- A palindrome is a string that reads the same backward or forward.
- Examples: eve, dad, rotator
Your program should be able to ask user to enter the word and check whether it is palindrome or not.
The program should not end until user enters no.
The program should start with the
The output should show inside a box as shown below with text justified center.
Example Output:
=============================[ Palindrome Finder ]=============================
Enter a word: rotator
+-----------------------------------------------------------------------------+
|                   The word 'rotator' is a palindrome                        |
+-----------------------------------------------------------------------------+
The word 'rotator' is a palindrome word
Do you want to check again? [yes/no]: yes
Enter a word: dad
+-----------------------------------------------------------------------------+
|                     The word 'dad' is a palindrome                          |
+-----------------------------------------------------------------------------+
Do you want to check again? [yes/no]: no
=================================[ exiting now ]================================
"""
#%%
# Using while loop for the infinite words.
def palindrome_finder(word):
    condition = (input(f' Please enter yes for continue and no for exit out'))
    #condition = 'yes'
    if condition== 'yes':
        word = input(f'Please enter a word to check wheather it is palindrome or not.')
        if word == word[::-1]:
            value = (f'The word you enterred "{word}" is palindrome.')
            print(f'+{"-"*78}+')
            print(f'|{value.center(78)}|')
            print(f'+{"-"*78}+')
            print(f'would you like to check another word? please enter yes or no')
            palindrome_finder(word)
        else:
            value = (f'The word you enterred "{word}" is not palindrome.')
            print(f'+{"-"*78}+')
            print(f'|{value.center(78)}|')
            print(f'+{"-"*78}+')
            print(f'would you like to check another word? please enter yes or no')
            palindrome_finder(word)
            
    return 'Exiting out.'

palindrome_finder("n")


# Need more action

#%%

"""
6.
Write a function that accepts words that are separated by hyphen returns the 
alphabetically sorted words
separated by hyphen.
Hint:
- split the words using string.split() method
- sort the list
- join the list to a string with string.join() method
"""
#%%
word = "cat-apple-dog-ball-ears-goose-fish"
def sort_words(word: str):
    # change your function body here
    word = word.split("-")
    word.sort()
    word = '-'.join(word)
    return word

word = sort_words(word)
print(word)

# "apple-ball-cat-dog-ears-fish-goose"
#%%

"""
7.
Write a function that accepts a number x
- if x is a multiple of 2, it should return the value y = x**2 + 2x + 3
- if x is a multiple of 3, it should return the value y = x**3 + 4x + 5
- if x is a multiple of both 2 and 3, it should return the value y = x**3 + 4x**2 + 5x + 6
- in other cases it should return negative value of the given number
"""
# answer
#%%
def number_filer(x):
    if x%2 == 0:
        y = x**2 + 2*x + 3 
        return y
    if x%3 == 0:
        y = x**3 + 4*x + 5
        return y
    if x%2 and x%3 == 0:
        y = x**3 + 4*x**2 + 5*x + 6
        return y
    else:
        return -x

print(number_filer(10))
print(number_filer(12))
print(number_filer(5))
#print(number_filer(0))

#%%
"""
8.
Write a function that accepts any number of arguments
find out the sum of all numbers by multiplying by 2 if it is odd and dividing by 2 if the number is even.
Example if arguments are (5,6,7,8)
the result should be 31 [ 5*2 + 6/2 + 7*2 + 8/2 ]
"""
# answer
#%%
def numeric (*args):
    sum = 0
    for num in args:
        if num%2 !=0:
            sum +=2*num
        if num%2 ==0:
            sum += num/2
    return sum
    
print(numeric(5,6,7,8))

#%%