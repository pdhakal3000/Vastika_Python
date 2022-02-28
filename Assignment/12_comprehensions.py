"""
© https://sudipghimire.com.np

Comprehension Exercises
"""

'''

1. convert the following loop to list comprehension
'''
#%%
# list = []
# for x in range(10):
#     list.append(2*x+1)
# print(list)
# Answer Here
list = [2*x+1 for x in range(10)]
print(f'This is the list out-come after list comprension:\n {list}')

#%%
'''

2.  Generate a dictionary from a list of first 10 numbers and it's square values
    using dictionary comprehension.

    Final value should be in format: {1:1, 2:4, 3:9, 4:16, ..., 10, 100}
'''

#%%Answer Here
# list_1 = []
# list_2 = []
# for x in range(10):
#     list_1.append(x)
#     list_2.append(x**2)
# dict = {list_1 : list_2}
# print(dict)
list3 = [x for x in (range(1,11,1))]
print(list3)
result ={x:x**2 for x in list3}
print(result)
#%%
'''
3.  Create the following pattern using list comprehension, `join()` method, and others if needed.
    Try to solve in a single line or single statement.

    1
    1   2
    1   2   3
    1   2   3   4
    1   2   3   4   5
'''
#%% Answer Here

# for row in range(1,6):
#     for col in range(1, row+1):
#         print(col, end = ' ')
#     print()
# # list comprehension
# result1 = [col for col in range(1, row+1) for row in range(1,6)]
# result1 = [str(col) for col in range(1, row+1) for row in range(1,6)]
result1 = '\n'.join([' ' .join([str(col) for col in range(1, row+1)]) for row in range(1,6)])
print(result1)

#%%
'''
4.  A mathematical function is defined by y = (4x ** 2) + (3 * x) - 6
    i. Create a generator function to generate first 1000 integers starting from -100 and store to a variable y.
    ii. Create a list using list comprehension to generate the same values
    iii. Compare the memory usage by those variables created in steps (i) and (ii) using __sizeof__() method.
    iv. Try to generate values of y for first million integers and compare memory usage as done in step (iii).

    To learn more about __sizeof__() method, please visit https://www.javatpoint.com/sizeof-in-python
'''
# Answers
#%%
#i
y = [((4*x ** 2) + (3 * x) - 6) for x in range (-100,900)]
#print(y)
#%%
#ii
y1 = (((4*x ** 2) + (3 * x) - 6) for x in range (-100,900))
#print(y1)
#%%
#iii
print(y.__sizeof__())
print(y1.__sizeof__())

#%%
#iv
y3 = (((4*x ** 2) + (3 * x) - 6) for x in range(1,1000000))
print(y3.__sizeof__())
#%%

#%%

'''
5.  Write a program to split a string 'Apple' into a dictionary of
    ASCII values of each characters using comprehension methods.

    To learn more about ASCII please refer to the site https://www.asciitable.com/

    Use the `ord()` method to find out the ASCII values

    final output should be: {'A': 65, 'p': 112, 'l': 108, 'e': 101}
'''
# Answer Here
#%%
# split function change its outcome in to list.
word = "Apple"
result = {letter : ord(letter) for letter in word}
print(result)
#%%
'''
6.  Write a program to generate a dictionary from the given nested tuple using dictionary 
comprehension.
'''
#%%
abbreviations = (
    ('ABC', 'Atanasoff Berry Computer'),
    ('BCD', 'Binary Coded Decimal'),
    ('CD', 'Compact Disc'),
    ('DVD', 'Digital Video Disc'),
    ('HTTP', 'Hyper Text Transfer Protocol'),
    ('WWW', 'World Wide Web'),
)
# Answer Here
abb_dict = {key:value for key,value in abbreviations}
print(abb_dict)
#%%
'''
BONUS EXERCISES

7.  Try All of the pattern generation exercises (if possible) with list comprehension
'''
# ANSWERS HERE
'''
All the answer are in pattern generation exercise with list comprehension and regular method.
Thank you.
'''

# %%
