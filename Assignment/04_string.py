"""
© https://sudipghimire.com.np


String Exercise


Please read the note carefully and try to solve the problem below:


"""

"""
1. Create two variablrs first_name, and last_name and print the sentence in the format below:
   suppose first_name is John and last_name is Doe
   "My name is John Doe"

   a. use + operator to concatenate strings
   b. use format() method to achieve the same result
   c. use f-strings to achieve the same result
   d. use %s formatting method to achieve the same result
"""
import math
from uuid import NAMESPACE_URL

# answer 1
# 1.a
first_name = "Prakash"
last_name = "Dhakal"

print("My name is " + first_name + " " + last_name)
# 1.b

print("My name is {} {}".format(first_name, last_name))
# 1.c

print( f"My name is {first_name} {last_name}")

# 1.d
print ('My name is %s %s' %(first_name, last_name))

"""
2. Assign a variable  pi and assign value 3.14159265
    a. use formatting strings to show pi with 3 digits after the decimal
    b. use formatting strings to show pi with 2 digits after the decimal but
       allocate 10 spaces for the variable
    c. use f-string to show the result in the following format:
        "The value of PIE is        3.14"

        hint: "%<a>.<b>f"
"""
# answer 2
# a
PI = 3.14159265
print("the value is:%5.3f" % PI)
# b

print("the value is:%5.2f" % PI)
# c
print(f"The value of  the PI is :  {PI:10.2f}")
"""
3. Use a function `input()`  to input the the name and age from the command line and
   display the formatted text as instructed below:

   a. use `input()` function to ask the name to the user. The console should show
      "What is your name?" to input the name
   
   b. similarly ask the user to input the age and assign it to another variable.

   c. Show a sentence describing the user name and age using different formatting methods.

      hint: Output would be a sentence similar to "Hello 20 years old John!!".
"""

# answer 3
#a.
print("Print your name and age in the console please")
name = input("Hello there what is your name:")
print(f"Thank you so much {name}" )

#b.
age = input(f"Would you mind to mention your age please!:" )

#c.
print(f"Thank you {name}. You are all set! let me know anything I messed up. So far you gave your name: {name} and age:{age} years")
print("Have a good day.")

# %%
