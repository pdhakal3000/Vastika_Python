"""
© https://sudipghimire.com.np

Pattern Generation Exercises
"""

# Write programs to generate following patterns

"""
Pattern 1
*
*   *
*   *   *
*   *   *   *
*   *   *   *   *

"""
#%% Answer Here
'''
    num row: 1  col: 1  value: *
    num row: 2  col: 2  value: *    *
    num row: 3  col: 3  value: *    *   *
    num row: 4  col: 4  value: *    *   *   *
    num row: 5  col: 5  value: *    *   *   *   *

'''
#%%
print('Solving with for loop and regular method.')
for row in range(1,6):
    for col in range(1, row+1):
        print('*', end ="\t")
    print()

print('Solving with list comprehension method.')
result_1 = '\n'.join(['\t'.join(['*' for col in range(1, row+1)]) for row in range (1,6)])
print(result_1)
#%%
"""
Pattern 2
1
1   3
1   3   5
1   3   5   7
1   3   5   7   9

"""
# Answer Here
'''
    num row: 1  col: 1  value: 1
    num row: 2  col: 2  value: 1    3
    num row: 3  col: 3  value: 1    3   5   (odd numbers)
    num row: 4  col: 4  value: 1    3   5   7
    num row: 5  col: 5  value: 1    3   5   7   9
'''
#%%
print('Solving with for loop and regular method.')
for row in range(1, 6):
    for col in range(1, row+1):
        print(2*col-1, end='\t')
    print()

print('Solving with list comprehension method.')
result_2 = '\n'.join(['\t'.join([str(2*col-1) for col in range(1, row+1)])for row in range (1,6)])
print(result_2)
#%%
"""
Pattern 3
1
2   2
3   3   3
4   4   4   4
5   5   5   5   5
"""
'''
    num row: 1  col: 1  value: 1
    num row: 2  col: 2  value: 2    2
    num row: 3  col: 3  value: 3    3   3   (print row number)
    num row: 4  col: 4  value: 4    4   4   4
    num row: 5  col: 5  value: 5    5   5   5   5
'''
#%%
print('Solving with for loop and regular method.')
for row in range(1, 6):
    for col in range(1, row+1):
        print(row, end='\t')
    print()

print('Solving with list comprehension method.')
result_3 = '\n'.join(['\t'.join([str(row) for col in range(1,row+1)]) for row in range (1,6)])
print(result_3)
#%%
# Answer Here


"""
Pattern 4
1
2   1
3   2   1
4   3   2   1
5   4   3   2   1


"""
'''
    num row: 1  col: 1  value: 1
    num row: 2  col: 2  value: 2    1
    num row: 3  col: 3  value: 3    2   1   (value of column is in decending from row num)
    num row: 4  col: 4  value: 4    3   2   1
    num row: 5  col: 5  value: 5    4   3   2   1    
'''
#%% Answer Here
print('Solving with for loop and regular method.')
for row in range(1, 6):
    for col in range(1, row+1):
        print(row+1-col, end='\t')
    print()

print('Solving with list comprehension method.')
result_4 = '\n'.join(['\t'.join([str(row+1-col) for col in range(1,row+1)]) for row in range(1,6)])
print(result_4)
#%%
"""
Pattern 5

1   2   3   4   5
2  - 4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25

"""
'''
    num row: 1  col: 5  value: 1    2   3   4   5   
    num row: 2  col: 5  value: 2    4   6   8   10
    num row: 3  col: 5  value: 3    6   9   12  15  (col*row)
    num row: 4  col: 5  value: 4    8   12  16  20
    num row: 5  col: 5  value: 5    10  15  20  25
    '''
#%%Answer Here
print('Solving with for loop and regular method.')
for row in range(1, 6):
    for col in range(1, 6):
        print(row*col, end='\t')
    print()

print('Solving with list comprehension method.')
result_5 = '\n'.join(['\t'.join([str (row*col) for col in range(1,6)])for row in range(1,6)])
print(result_5)

#%%
'''
Pattern 6

A
A   P
A   P   P
A   P   P   L
A   P   P   L   E

'''

#%% Answer here
print('Solving with for loop and regular method.')
word = "APPLE"
length =len(word)
#print(length)
for i in range(length):
    for j in range (i+1):
        print(word[j], end='\t')
    print()

print('Solving with list comprehension method.')
result_6 ='\n'.join(['\t'.join([word[j] for j in range(i+1)])for i in range(length)])
print(result_6)
#%%
"""
Pattern 7

                *
            *   *
        *   *   *
    *   *   *   *
*   *   *   *   *

"""
"""
    num row: 1  col: 1(*)(" ") value: 1,4
    num row: 2  col: 2(*)(" ") value: 2,3
    num row: 3  col: 3(*)(" ") value: 3,2   (num of row increase by 1 similarly star and tab(space) decrease 4 to 0)
    num row: 4  col: 4(*)(" ") value: 4,1
    num row: 5  col: 5(*)(" ") value: 5,0  
                                                                            *
                                                                        *   *
                                                                    *   *   *
                                                                *   *   *   *
                                                            *   *   *   *   *
"""
#%% Answer Here
print('Solving with for loop and regular method.')
for row in range(1, 6):
    for space in range(5-row):
        print(' '*(5-row), end='\t')
    for col in range(1, row+1):
        print("*", end='\t')
    print()
#%%
'''
I am guessing following code is not working syntatically because of more than two task inside main for loop.

any comment or suggestion @Sudip?
'''
print('Solving with list comprehension method.')
result_7 = '\n'.join(['\t'.join(['\t'.join(['*' for col in range (1, row+1)])' ' for space in range(5-row)]) for row in range(1,6)])

# print(result_7)
#%%
"""
Pattern 8

                1
            1   3
        1   3   5
    1   3   5   7
1   3   5   7   9

"""
#%% Answer Here

for row in range(1, 6):
    print('\t'*(5-row), end='')
    for col in range(1, row+1):
        print(2*col-1, end='\t')
    print()
    
#%%
'''
Pattern 9

                A
            A   P
        A   P   P
    A   P   P   L
A   P   P   L   E

'''
word = "APPLE"
#%% Answer here
word = "APPLE"
length =len(word)
#print(length)
for i in range(length):
    print('\t'*(5-i), end='')
    for j in range (i+1):
        print(word[j], end='\t')
    print()

#%%
"""
Pattern 10  (Bonus Exercise)
                1
            1   2   1
        1   2   3   2   1
    1   2   3   4   3   2   1
1   2   3   4   5   4   3   2   1


"""

#%%
for x in range(1, 6):
    print('\t' * (5 - x), end='\t')
    for y in range(1, x+1):
        print(y, end='\t')
    for z in range(x-1,0,-1):
         print(z, end = '\t')
    print()
#%%