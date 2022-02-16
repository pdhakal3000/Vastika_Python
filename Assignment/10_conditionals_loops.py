"""
© https://sudipghimire.com.np

Conditional and loop Exercises
"""
import math


'''
1.  Write a program to input a number and check whether a number is an integer or not
    hint: you can use isnumeric() function
'''
#%%Answer

x = input('Enter a number: ')
if x.isnumeric():
    print(f'{x} is numeric. \n')
else:
    print(f'{x} is not numeric. \n')

#%%
'''
3. from the list below, separate a list that are even and odd and put them into the respective variables

the final output should be:

Odd numbers: [1, 5, 89, 167, 333, 5, 23]
Even numbers: [2, 32, 112, 20]
'''
#%%
num = [1, 5, 2, 89, 32, 112, 167, 333, 20, 5, 23]
odd_num = []
even_num=[]
# Answer
for value in num:
    if value%2==0:
        even_num.append(value)   
    else:
        odd_num.append(value)
        
print(f'This is a list of even number: \n {even_num} \n')
print(f'This is a list of odd number:\n {odd_num} \n')

even =[x for x in num if x%2==0]
odd =[y for y in num if y%2!=0]
print(f' Thsis is list of even numbers with list comprehension method:\n {even} \n' )
print(f' Thsis is list of odd numbers with list comprehension method:\n {odd}')

#%%

'''
4.  Write a program to input 2 different words and find out if the words are Palindrome or not.

    - A word is palindrome if reads the same from both backward and forward.

    Eg: EVE, HANNAH, BOB, ANNA, ROTATOR, REPAPER
________________________________________________________________________
The Output in the console should look like below
________________________________________________________________________
Enter a word: Hannah

Hannah is a palindrome word
________________________________________________________________________
'''
# answer here
#%%
word = input(f'Enter a word to test wheather it is palindrome or not: ')
word = word.lower()
word_list = []
for char in word:
    word_list.append(char)
    word_list_1 = word_list.copy()
    word_list_1.reverse()
#print(word_list)
#print(word_list_1)
if (word_list) == (word_list_1):
    print(f'Word "{word}" is palindrome.')
else:
    print(f'Word "{word}" is not palindrome.\n')

#%%
'''
5.  Write a program to print the first 20 fibbonnaccii numbers

    The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is
    the sum of the previous two numbers in the sequence.
    eg: 1, 1, 2, 3, 5, 8, 13, ...

    hint: use for loop in range of 20, add a and b and update values of a, b and others if necessary
'''
'''step:1. Initialize required variable
   step:2. Use condition, while loop up to 20
   step:3. Execution, print first two number 1, 1 meaning a and b as it is
           after that each number is sum of previous two numbers ie. n+n-1
   step:4. update loop condition
'''
#%%
list_1 = []
a, b = 1, 1
list_1.append(a)
list_1.append(b)
n = list_1.__len__()
while n !=20:
    sum_of_two = list_1[n-2] + list_1[n-1]
    list_1.append(sum_of_two)
    n+=1
print(list_1)
#%%
list_1 = [1, 1]
n = list_1.__len__()
while n !=20:
    sum_of_two = list_1[n-1] + list_1[n-2]
    list_1.append(sum_of_two)
    n+=1
print(list_1)
#%%
'''
6.  Write a program to enter a month and day of birth and find out the horoscope of a person:

- Aries: Mar 21 - Apr 19
- Taurus: Apr 20 - May 20
- Gemini: May 21 - Jun 20
- Cancer: Jun 21 - Jul 22
- Leo: Jul 23 - Aug 22
- Virgo: Aug 23 - Sep 22
- Libra: Sep 23 - Oct 22
- Scorpio: Oct 23 - Nov 21
- Sagittarius: Nov 22 - Dec 21
- Capricorn: Dec 22 - Jan 19
- Aquarius: Jan 20 - Feb 18
- Pisces: Feb 19: Mar 20

________________________________________________________________________
The Output in the console should look like below
________________________________________________________________________
Enter your Month and Day of Birth [Eg: Oct 20]: Oct 20

Your Horoscopic Sign is:    Libra
________________________________________________________________________

Hint:
    you can use `split()` function to split words from a string
'''
# date = 'Oct 20'
# month, day = date.split()
# day = int(day)
# print(month,'/', day)

#%% answer
from datetime import date, timedelta, datetime, timedelta

'''
TypeError: '<=' not supported between instances of 'datetime.date' and 'tuple is the error i am facing 
not allow me to compare.
'''
print('Enter your birth year, month and day in digits: ')
year = int(input(f'Please enter your year of the birth:'))
month = int(input(f'Please enter your month of the birth:'))
day =int(input(f'Please enter your day of the birth:'))
birth_day = (year, month, day)
#print (birth_day)
if date(2022, 3, 21) <= birth_day <= date(2022, 4, 19):
    print("You're Aries")
if date(2022, 4, 20) <= birth_day <= date(2022, 5, 20):
    print("You're Taurus")
if date(2022, 5, 21) <= birth_day <= date(2022, 6, 20):
    print("You're Gemini")
if date(2022, 6, 21) <= birth_day <= date(2022, 7, 22):
    print("You're Cancer")
if date(2022, 7, 23) <= birth_day <= date(2022, 8, 22):
    print("You're Leo")
if date(2022, 8, 23) <= birth_day <= date(2022, 9, 22):
    print("You're Virgo")
if date(2022, 9, 23) <= birth_day <= date(2022, 10, 22):
    print("You're Libra")
if date(2022, 10, 23) <= birth_day <= date(2022, 11, 21):
    print("You're Scorpio")
if date(2022, 11, 22) <= birth_day <= date(2022, 12, 21):
    print("You're Sagittarious")
if date(2022, 21, 22) <= birth_day <= date(2022, 1, 19):
    print("You're Capricorn")
if date(2022, 1, 20) <= birth_day <= date(2022, 2, 18):
    print("You're Aqarious")
if date(2022, 2, 19) <= birth_day <= date(2022, 3, 20):
    print("You're Pisces")



'''
BONUS QUESTION
1.  Suppose you went to a coffee shop. A shopkeeper asked you to create a program 
that serves coffee according to the customer's requirements.

    The coffee machine should ask user to enter any numbers below that should make a 
    coffee and serve it to the user.Please use the `make_coffee()` function below
    to prepare a coffee and serve it. below are the conditions:

    1. Espresso
        - price: $2
        - type: hard

    2. Americano
        - price: $2.5
        - type: mild

    3. Cappuccino
        - price: $3
        - type: soft

    The program should be able to ask user to input a number 1, 2 or 3 and display message according
    to the conditions above.

________________________________________________________________________
The Output in the console should look like below
________________________________________________________________________
Today's Menu:
1. Espresso
2. Americano
3. Cappuccino

Enter Number:   1

Dear Customer, Your Espresso is ready. please pay $2 at the counter.

Quick fact: Espresso is a hard coffee.
________________________________________________________________________
'''
#%% Answer
cofee_menu = {
    '1':'Espresso', 
    '2':'Americano',
    '3':'Cappuccino'
 }
menu_detail = {
    'Espresso':{'price': 2, 'type':'hard'}, 
    'Americano':{'price': 2.5, 'type':'mild'},
    'Cappuccino':{'price': 3, 'type':'soft'}
}
print(f'Hi! Welcome to our store. Here is our cofee menu for the day:\n {cofee_menu} \n')
print(f'Please select which one you like to have today using serial number.\n')
num_select = input('Please enter number here :')

if num_select == '1':
    x = cofee_menu[num_select]
    print(f'You selected {x} thank you. \n')
    print(f"Quick fact : {x} is {menu_detail[x]['type']} type cofee.\n Please pay ${menu_detail[x]['price']} in the register. \nThank you and enjoy your cofee.")
if num_select == '2':
    x = cofee_menu[num_select]
    print(f'You selected {x} thank you.\n')
    print(f"Quick fact : {x} is {menu_detail[x]['type']} type cofee.\n Please pay ${menu_detail[x]['price']} in the register.\nThank you and enjoy your cofee.")
if num_select == '3':
    x = cofee_menu[num_select]
    print(f'You selected {x} thank you. \n')
    print(f"Quick fact : {x} is {menu_detail[x]['type']} type cofee.\n Please pay ${menu_detail[x]['price']} in the register.\nThank you and enjoy your cofee.")

#%%

'''
BONUS QUESTION
2. Write a program to check whether a number is a special number or not.

   If the sum of the factorial of digits of a number (N) is equal to the number itself,
   the number (N) is called a special number.

Eg: 145 is a special number where, 1! + 4! + 5! = 145

try it with numbers:    145, 1, 35

Hint 1: you can get each digit using a modulus and integer division of a number by 10 until the number is less than 10
    eg: 145
        145//10 = 14        145%10=5                    (5 is ones digit)
        14//10 = 1          14 % 10 = 4                 (4 is tens digit)
        at the end, 1 (which is less than 10)           (1 is hundreds digit)

hint 2: you can use `math.factorial()` to find out factorial of a number.

'''
#%% answer here
'''
This is solution for now. I gues we can do with short cut with function later.
'''
import math
num = int(input('Please enter a number to check special or not :'))
original_num = num
num_length = len(str(num))
print(num_length)
if num_length ==5:
    unit = num % 10                
    num = num // 10
    tens = num % 10              
    num = num // 10     
    hundreds = num % 10           
    num = num // 10
    thousands = num % 10           
    num = num // 10
    factorial_sum = math.factorial(unit) + math.factorial(tens) + math.factorial(hundreds) +math.factorial(thousands) + math.factorial(num)
    print(factorial_sum)
    if factorial_sum == original_num:
        print('Your input was special number.')
    else:
        print('It is not special number.')

if num_length == 4:
    unit = num % 10                
    num = num // 10
    tens = num % 10              
    num = num // 10     
    hundreds = num % 10           
    num = num // 10
    factorial_sum = math.factorial(unit) + math.factorial(tens) + math.factorial(hundreds)+ math.factorial(num)
    print(factorial_sum)
    if factorial_sum == original_num:
        print('Your input was special number.')
    else:
        print('It is not special number.')

if num_length == 3:
    unit = num % 10                
    num = num // 10
    tens = num % 10              
    num = num // 10
    factorial_sum = math.factorial(unit) + math.factorial(tens) + math.factorial(num)
    print(factorial_sum)
    if factorial_sum == original_num:
        print('Your input was special number.')
    else:
        print('It is not special number.')     

if num_length == 2:
    unit = num % 10                
    num = num // 10
    factorial_sum = math.factorial(unit) + math.factorial(num)
    print(factorial_sum)
    if factorial_sum == original_num:
        print('Your input was special number.')
    else:
        print('It is not special number.')

   
#%% 
"""
BONUS QUESTION
3.  Hangman Game
    Create a Guessing game that gives you 3 chance for a person to make mistakes
    Use a word "Elephant" for now
________________________________________________________________________
HANGMAN !!

Guess the word:     E _ _ p _ _ n t

Enter the position, and character [eg: 2 l] to fill the blanks

 E _ _ p _ _ n t    ( 0 / 3 mistakes ):     2 l
 E l _ p _ _ n t    ( 0 / 3 mistakes ):     3 a

 E l * p _ _ n t    ( 1 / 3 mistakes ):

 Try your own logig, or ways. we'll be discussing answers for this game.
________________________________________________________________________
"""
#%%
'''
not exactly what question asked but I come with this solution some how similar.
'''
actual_word = 'Elephant'
question = 'E _ _ p _ _ n t'
remaining = ['l','e','h','a']

mistake = 0
enterred_letter = []
while mistake < 5:
    letter = input('Guess a letter :')
    if letter in remaining:
        enterred_letter.append(letter)
        print(f'{letter} is one of the required letter:')
        print(enterred_letter)
        if len(enterred_letter) ==4 and enterred_letter == remaining:
            print(f'your guess is right and final word is {actual_word}')
            break
        else:
            print('You are on right track go further.\n')
    else:
        mistake+=1
        print(f'The letter {letter} is not in required letter list: {5-mistake} more chance with you.\n ')


# %%
