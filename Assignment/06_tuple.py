"""
© https://sudipghimire.com.np

Tuple Exercises

Please read the note carefully and try to solve the problem below:

"""

"""
1. Write a program to create a tuple to  add 5 different numbers.
    a. find out the length of the tuple
    b. find out the 3rd element of the tuple by accessing it through the index
    c. use `enumerate()` function to map each element with its index and print it using the foreach loop
        - please see the reference to the file 02_data_types/06_tuples.py

"""
# answer 1
#%% Creating a list with 5 element and changing it to the tuple using consle input.
list_1 = []
while(list_1.__len__()) <= 6:
    x = input('Enter the element :')
    list_1.append(x)
    print(f'More element please! This is/are your enterred elements so far: {list_1}')
    if (list_1.__len__()) == 5:
        tuple_1 = tuple(list_1)
        print(f'This is your 5 element tuple : {tuple_1} ')
        break
    

# %% Finding length of the tuple.

# a
p = tuple_1.__len__()
print(f'Length of the tuple is : {p}')

#%% Finding third elements of the tuple.
# b
print (f'Third element of the tuple is: ', tuple_1[2])

#%% Demonstrating enumarate function.
# c
enum = enumerate(tuple_1)
print('Here is the pair of index and element of the tuple-')
for (index, number) in enum:
    print(f'{index} - {number}')


#%%
"""
2. Write a program to create a nested tuple and access different elements of the inner tuple using
   positive and negative index positions.
"""
'''
-Create a for loop which can go n number 
-n is list number
-Turn each list ot the tuple
-merge or combined  n number of tuple in a single tuple
-Access elements of that nested tuple with various way.
'''
n = int(input('Enter how many tuple you want to include in your nested tuple : '))
for i in range(1, n):
    l1 = []
    while(l1.__len__()) <= 4:
        x = input('Enter the element :')
        l1.append(x)
        print(f'More element please! This is/are your enterred elements so far: {l1}')
        if (l1.__len__()) == 4:
            tup = tuple(l1)
            print(f'This is your tuple {i}: {tup} ')
            tup_i = tup
            break
i +=1


#%% Simple way making nested tuple and acessing elements
t1:tuple = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)
t3 = (11, 12, 13, 14, 15 )
tcomb = (t1, t2, t3)

print(f'This is nested tuple made up of three tuples \n {tcomb}')

# Accessing an element from the 2 form the nested tuple.
print (f' Accessing element "2" from nested tuple using positive index : ', tcomb[0][1])
print (f' Accessing element "2" from nested tuple using negative index : ',tcomb[-3][-4])

# Accessing an element from the 10 form the nested tuple.
print (f' Accessing element "10" from nested tuple using positive index : ', tcomb[1][4])
print (f' Accessing element "10" from nested tuple using negative index : ', tcomb[-2][-1])

# Accessing an element from the 13 form the nested tuple.
print (f' Accessing element "13" from nested tuple using positive index : ', tcomb[2][2])
print (f' Accessing element "13" from nested tuple using negative index : ', tcomb[-1][-3])


#%%

"""
Bonus:
3. create two different tuples t1 and t2 with different elements inside it
    a. create the next tuple t3 to add all values of t1 and t2 using the destructuring method

    - suppose t1 has (1,6,9,4,3)
    - and t2 has (2,7,8,3,5)
    -t3 must have (1,6,9,4,3,2,7,8,3,5)
    - make sure to use destructuring method using `*` operator in the tuples
"""
print(f'First unique tuple is : {t1} \n' )
print(f'Second unique tuple is : {t2} \n' )
print(f'Third unique tuple is : {t3} \n' )

print(f'After destructuring all three tuples in to single tuple is: \t', (*t1, *t2, *t3))
# %%
