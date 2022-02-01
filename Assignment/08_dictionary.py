"""
© https://sudipghimire.com.np

Dictionary Exercises
Please read the note carefully and try to solve the problem below:

"""
"""
1. Create a dictionary of a person that contains key value pair of
    - name: str
    - age: int
    - profession: str
    - married: bool

    a. print the value of 'name' from the dictionary
    b. add the age of the dictionary be 10 and print the dictionary items in formatted string
        Eg: {name} will be {new_age} at 2031 AD.
    c. Try getting the value of 'employed' from the dictionary.
        - If exception occurs, note it and check what the excption says.
    d. try `get()` method instead of large brackets [] in the previous question (1.c)
    e. try `get()` method with second parameter: False and see what is printed.
        Eg: person.get('employed', False)
"""
#%% Answers:Create a dictionary of a person
from unicodedata import name


person = {
    'name': 'str',
    'age': 'int',
    'profession': 'str',
    'married': 'bool'
    }

#%% 1.a print the value of 'name' from the dictionary

print(f'Value of "name" from the dictionary is: ', (person['name']), end= '\n')

#%% 1.b add the age of the dictionary be 10 and print.

person['name'] = 'Hari' # Using real name.
person['age'] = 10
print(f"{person['name']} will be {person['age']} years old in 2032.")

#%% 1.c getting the value of 'employed' from the dictionary

print(f"person: {person['employed']}")

#%%1.d try `get()` method instead of large brackets [].

print(f'There is something empolyed? :{person.get("employed")}')

#%% 1.e try `get()` method with second parameter: False

print(f'There is something empolyed? :{person.get("employed", False)}')

#%%
"""
2. create a dictionary <car> with 3 keys and values (brand, model, price).
    a. add a new key 'engine' and set some random value in car.
    b. add 3 more dictionary keys with `update` method. (color, no_of_seats, transmission).
    c. remove the key 'color' from the dictionary.
    d. try using `popitem()` method in the dictionary and see what changes in dictionary
    e. use for loop to iterate through all keys from a dictionary.
    f. use for loop to iterate through all keys from a dictionary using `keys()` method.
    g. use for loop to iterate through all values from a dictionary using `values()` method.
    h. use for loop to iterate through all keys, values from a dictionary using `items()` method.
"""
#%% Answers:
car = {'brand' : 'Tesla', 'model': 'Splaid', 'price':'$140,000'}
#%% 2.aadd a new key 'engine' and set some random value in car

car['engine'] = 'Electric'
print(f'Updated dictionary "car" : {car}')

#%% 2.b add 3 more dictionary keys with `update` method. (color, no_of_seats, transmission)

car.update({'color' : 'White', 'no_of_seats' : 5, 'transmission' : 'Electric'})
print(f'Updated dictionary car after update function: \n {car}')

#%% 2.c remove the key 'color' from the dictionary

car.pop('color')
print(car)

#%% 2.d try using `popitem()` method in the dictionary and see what changes in dictionary

print(car)
print(f'Removing item: {car.popitem()} \n')
print(f'Is it same as above? : {car} \n')

#%% 2.e use for loop to iterate through all keys from a dictionary

for key in car:
    print(f'These are keys in the car dictionary : {key} \n')

#%% 2.f use for loop to iterate through all keys from a dictionary using `keys()` method.

print(f'These are keys in the car dictionary: ', car.keys())

#%% 2.g use for loop to iterate through all values from a dictionary using `values()` method.

for values in car.values():
    print(f'These are values of the dictionary car: {values} \n')

#%% 2.h use for loop to iterate through all keys, values from a dictionary using `items()` method.

for keys, values in car.items():
    print(f'{keys} --> {values} \n')

#%%
"""
3. Create a nested dictionary named yoda with following properties
    - age: 910
    - species: Yodas
    - gender: male
    - affilitions: ['Jedi', 'Galactic Republic']
    - master: <dict>
        - name: Qui-Gon Jinn
        - age: 48
        - affiliations: ['Jedi', 'Galactic Republic', 'Heliost Clan']
        - master: <dict>
            - name: Dooku
            - age: 83
            - affiliations: ['House Serenno', 'Jedi']

    a. print the value of the first affiliation of `Dooku` from the dictionary
    b. add new affiliation 'Sith' to Dooku
    c. pop the key 'master' from the dictionary

"""
#%% Answer 3 Create a nested dictionary named yoda
yoda = {
    'age': 910,
    'species': 'Yodas',
    'gender': 'male',
    'affilitions': ['Jedi', 'Galactic Republic'],
    'master': {'name': 'Qui-Gon Jinn',
    'age': 48,
    'affiliations': ['Jedi', 'Galactic Republic', 'Heliost Clan'],
    'master': {
            'name': 'Dooku',
            'age': 83,
            'affiliations': ['House Serenno', 'Jedi']
        }}
}

#%% 3.a print the value of the first affiliation of `Dooku` from the dictionary
#print(yoda)

print(yoda['master']['master']['affiliations'][0])

#%% 3.b add new affiliation 'Sith' to Dooku

adding = 'Sith'
yoda['master']['master']['affiliations'].append(adding)
print(f'This is dictionary after adding Sith :\n {yoda}')


#%% 3.c. pop the key 'master' from the dictionary
yoda.pop('master')
print(f'This is dictinary "yoda" after poping out "master": {yoda}')


# %%
