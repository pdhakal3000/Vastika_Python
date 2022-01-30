"""msg = "Hello world"
print(msg)
print("Hello World wats up")
"""
"""
x = range(11)
for n in x:
    print(n)
"""

print("Please insert number for the range in the console: ")
y = (int(input()))
print(f"The number you inserted is: {y}")
t = range(1, y, 2)
for n in t:
    print(n)

"""
import sys
a = xrange(1,20)
"""
x = [1,2,3]
a = [4,5,6]
b = [7,8,9]
[[[(x+a+b) for b in range(3)] for a in range(3)] for x in range(5)]

x =[]
for a in range(11):
	x.append(a)