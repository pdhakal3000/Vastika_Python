# %%
"msg = "Hello world"
print(msg)
print("Hello World wats up")

# %%

x = range(11)
for n in x:
    print(n)
# %%

print("Please insert number for the range in the console: ")
y = (int(input()))
print(f"The number you inserted is: {y}")
t = range(1, y, 2)
for n in t:
    print(n)
#%%
import sys
a = xrange(1,20)

x = [1,2,3]
a = [4,5,6]
b = [7,8,9]
[[[(x+a+b) for b in range(3)] for a in range(3)] for x in range(5)]

x =[]
for a in range(11):
	x.append(a)
#%%

t1 = (1,2,3,4,5,6)
t2 = (7,8,9,10,11)
t3 = (12,13,14,15,16)

t5 = (t1, t2, t3)
print(t5)

x = t5[1][0]
print(x)

t4 = (*t1,*t2,*t3)
print(t4)

# © https://sudipghimire.com.np
# %% [markdown]
"""
## While Loop
- It is used for iterating until the condition fails to satisfy

Basic Syntax:

while <condition>:
    # statements
    <update>

"""
x = 0
while x < 10:
    print(f'current value of x is {x}')
    x += 1
    # x++  # incorrect in case of python

# %% another example
value = 'y'
while value.lower() != 'e':
    value = input('Enter text[`e` to exit]: ')
    print(f'You Entered: {value}')
print('exiting now!!')

# %% another example with numbers
value = 1
while value != 0:
    value = int(input('Enter a number to display[0 to exit]: '))
    print(f'You Entered: {value}')
print('exiting now!!')
# %% infinite loop:
# while True:
#     print('This loop does not end')

# %% break and continue statements in a loop
x = 0
while x < 10:
    x += 1
    if x == 5:
        continue
    if x == 8:
        break
    print(f'current value of x is {x}')
print('loop complete')

# %% printing out only odd numbers below 10
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)
print('loop complete')

# %% while else statement
x = 0
while x < 10:
    x += 1
    # These lines do not fulfill else condition in while else
    # if x == 5:
    #     continue
    # print(f'current value of x is {x}')
    # if x == 8:
    #     break
else:
    print(f'x is now {x}, now Exiting!!')

# %% nested loops
"""
1
1 2
1 2 3
1 2 3 4
"""
x = 1
while x <= 4:
    y = 1
    while y <= x:
        print(y, end=' ')
        y += 1
    print()
    x += 1
