"""
© https://sudipghimire.com.np

Sets Exercises

Please read the note carefully and try to solve the problem below:

"""

"""
1. Write a program to create two different set of countries
    i.  rich: {'USA', 'China', 'Japan', 'Germany', 'France', 'Australia', 'Italy'}
    ii. europe: {'Germany', 'France', 'England', 'Switzerland', 'Italy', 'Portugal', 'Sweden'}

    Use the Set methods to find out:

    a. countries that are rich but not in Europe
    b. countries that are in Europe but not rich
    c. countries that are both rich and are in Europe
    d. countries that are either rich or in Europe, but not both
    e. all the countries in either of the sets. (Names must be unique)
    f. see if two sets are disjoint or not
    g. now remove the common countries from the `rich` set and check if two sets are disjoint or not.
        - hint: use `difference_update()` method. for more, please refer to python documentation
"""
#%% # answer 1.Creating two sets- rich country and Europian country.

rich = {'USA', 'China', 'Japan', 'Germany', 'France', 'Australia', 'Italy'}
europe = {'Germany', 'France', 'England', 'Switzerland', 'Italy', 'Portugal', 'Sweden'}

#%% a. countries that are rich but not in Europe.

rich_not_in_europe = rich.difference(europe)
print(f' These are rich country which are not in Europe : {rich_not_in_europe}')
print ('These are rich which are not in Europe " a-b method"', rich-europe)

#%% b. Countries that are in Europe but not rich.

europian_not_rich  = europe.difference(rich)
print(f'These are contry in the Europe and not rich: \n {europian_not_rich}', end ='\n')
print(f'These are contry inside Europe but not rich "a-b method" : \n ', europe - rich , end ='\n')

#%% c. Countries that are both rich and are in Europe
# we can retrieve these by ommiting out not rich country from europe.

rich_europian_country = europe.difference(europian_not_rich)
print(f'These are rich and europain country: \n {rich_europian_country}')
print(f'Rich European contires are "Using & method": \n', rich & europe )

#%% d. Countries that are either rich or in Europe, but not both
#-> This means rich contry only belongs to rich or only in Europe but not rich (not common beteen them).
#-> Union of contries only belongs to one set.

rich_only = rich.difference(europe) # rich-europe
europian_only = europe.difference(rich) # europe-rich
union_ab = rich_only.union(europian_only)
print(f'Countries that are either rich or in Europe, but not both: \n {union_ab}')
print(f'Countries that are either rich or in Europe, but not both "Using | opreator": \n', rich_only |europian_only)

#%% e. All the countries in either of the sets. (Names must be unique)

print(f'All the countries in either of the sets are:\n', rich.union(europe))
print(f'All the countries in either of the sets "Using | operator"are:\n', rich | europe)

#%% # f. see if two sets are disjoint or not

print(f'Is rich and europe sets are disjoint? : \n', rich.isdisjoint(europe))

#%% # g Now remove the common countries from the `rich` set and check if two sets are disjoint or not.
      #  - hint: use `difference_update()` method. for more, please refer to python documentation
#->It means rich only and europian only is disjoint sets or not.

print(f'Is rich only and europian only sets are disjoint? : \n', rich_only.isdisjoint(europian_only))

#%%
"""
2. Create two more sets
    i.  `asian_rich` and add {'China', 'Japan'} to it.
    ii. `american_rich` and add {'USA', 'Canada'} to it.
   and check whether:

   a. `asian_rich` is a subset of `rich` or not
   b. `rich` is a superset of `asian_rich` or not
   c. `american_rich` is a subset of `rich` or not

"""
#%% # answer 2 Creating two sets 

asian_rich = {'China', 'Japan'}
american_rich = {'USA', 'Canada'}

#%% # a. asian_rich` is a subset of `rich` or not

print(f'Is asian_rich set is subset of rich set? : \n', asian_rich.issubset(rich))

#%%# b. `rich` is a superset of `asian_rich` or not

print(f'Is rich set is superset of asian_rich set? : \n', rich.issuperset(asian_rich))

#%%# c. american_rich` is a subset of `rich` or not

print(f'Is american_rich set is subset of rich set?: \n', asian_rich.issubset(rich))

# %%
