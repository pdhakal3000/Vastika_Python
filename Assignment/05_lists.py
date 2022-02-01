"""
© https://sudipghimire.com.np

Lists Exercises

Please read the note carefully and try to solve the problem below:

"""

"""
1. Write a program to create an empty list named `my_list` and

    a. add numbers 5 and 9 to the list using `append()` method

    b. ask the user to input any number in the console and add the number to the list.
        - you can use int() to change the type from string to integer if you want.

    c. create another list `more_items` with 3 items on it and extend the list `my_list`
        using `extend` method.

    d. now find the length of the list and print the length of list describing it in a sentence.
        - you can always use string formatting for better outputs.

    e. now remove the second item using `pop()` method and see if the item exists in the list
        - you can print the list before and after using the `pop()` method.
"""
#%%
# answer 1
# a
my_list = []
my_list.append(5)
my_list.append(9)
print(f"List after appending given integer is : {my_list} \n")

#%%
# b
print("Enter integer in the : ")
x = int(input())
my_list.append(x)
print(f"\nlist after adding integer form the console is : {my_list} \n")

#%%
# c
more_items = [20, 30, 40]
my_list.extend(more_items)
print(f"list extending with more items is: {my_list} \n")

#%%
# d
print(f"The length of the my_list is: {len(my_list)} \n")

#%%
# e
print(f"list before poping out an element: {my_list} \n")
(my_list.pop(1))
print(f"The final list after removing an element : {my_list} \n")
#%%
"""
2. Write a program to add 5 different wild animals to a list named `wild`.
    - tiger, lion, deer, bear, zebra

    a. sort them in ascending using the `sort()` method.
    b. reverse the list using the `reverse()` method.
    c. now add 3 more animals to the list `wild`.  ['leopard', 'elephant', 'rhino']
    d. find the position of `leopard` using the `index()` method and remove  it using `the pop()` method.
        - pop should have the index value returned using the `index()` method.
        - do not hard-code the position of leopard by manually counting it from the list.
        - check whether the leopard is removed from the list or not by `index()` method again.
          if the value error occurs, you have successfully removed it from the list.
          otherwise, try to do it again.
        - you can then comment the line that gives exception to continue to the next question.
    e. Now add `leopard` agin in the index 2 using `insert()` method.
    f. Again, remove `rhino` from the list using remove() method.

    note: you can print the values of list after each successful operations to see what is being changed.
"""
#%%
# answer 2
# a
wild = ["tiger", "lion", "deer", "bear", "zebra"]
print(f"The list of wild animals {wild} \n")
wild.sort()
print(f"sorted list of the wild animal list: {wild} \n")

#%%
# b
wild.reverse()
print(f"Reverse of the wild animal list is : {wild} \n")

#%%
# c
extra_animal = ['leopard', 'elephant', 'rhino']
wild = wild.__add__(extra_animal)
print(f" The list after adding extra three animals is : {wild} \n")

#%%
# d
leo_index = (wild.index('leopard'))
print(f"The index of the leopard in the list is {leo_index} \n")
wild.pop(leo_index)
print(f"The list after pop-out leo from the list is : {wild}\n")

#print("Checking presence of the loopard in the list")
#leo_index = (wild.index('leopard'))
#%%
# e
wild.insert(2,'leopard')
#print(wild)
print(f"Inserting leopard in the index number 2 in the wild animal list : {wild}\n")
#%%
# f
wild.remove('rhino')
print(f"List after removing rhino form the wild list is : {wild}\n")

#%%
"""
3. Try creating a multi-dimensional list or nested list `multi` of different numbers.
    eg: [[12,52,37],[46,51,16],[17,82,39]]

    a. access the number 51 from the list.
    b. access the number 82 using the negative indices.
    c. append another list [40, 61, 10] inside the list `multi`.
        the final list should be: [[12,52,37],[46,51,16],[17,82,39],[40, 61, 10]]
    d. use foreach in the list `multi` to print each list item to the console.
        - Bonus: try using nested foreach to access each item inside of the inner list
    e. finally clear the list `multi` using the `clear()` method and verify if the list is empty or not
"""

#%%
# answer 3
list1 = [12, 52, 37]
list2 = [46, 51, 16]
list3 = [17, 82, 39]
#multi = [*list1, *list2, *list3] It is for a single list from multiple list.
multi = [list1, list2, list3] # Single list with multiple list or nested list from list.
print (f"The nested list multi is: {multi} \n")

#%%
# a
print(f"Accesing 51 from the list : ", multi[1][1], end='\n')
#print(multi.index(51)) does not work because 51 is element of the nested list.

#%%
# b
print(f"Acessing 82 from the list: ", multi[-1][-2], end='\n')

#%%
# c
multi.append([40, 61, 10])
print(f"\nlist after appendig given list is: \n {multi} \n")

#%%
# d
print("Exposing list of nested list - \n")
for list in multi:
    print(f'\nThis was one of the list inside nested list "multi": {list}')
    print(f'These are correspnding elements in list:')
    for i in list:
        print(f'{i}')
     

#[[(a+b) for b in range(3)] for a in range(3)]
#%%
# e
multi.clear()
print(f" \n The list \" multi\" after clear function is empty: {multi} \n")
#multi = []
