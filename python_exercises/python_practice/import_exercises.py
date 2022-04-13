from function_exercises import is_vowel as v, calculate_tip
import itertools
import json
from collections import Counter

"""_____________________________________________________________________________________________________________________
Import and test 3 of the functions from your functions exercise file. Import each function in a different way:

1a. Run an interactive python session and import the module. Call the is_vowel function using the . syntax.

1b. Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly.
Call this function with values you choose and print the result.
_____________________________________________________________________________________________________________________"""

# calling is_vowel
print(v('a'))

# calling calculate_tip
print(calculate_tip(0.5, 50))

"""
Read about and use the itertools module from the python standard library to help you solve the following problems:

2a. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
2b. How many different combinations are there of 2 letters from "abcd"?
2c. How many different permutations are there of 2 letters from "abcd"?
"""

# 2a:
# 1st option -----------------------------------------------------------------------------------------------------------
print(" ")

print(list(zip(['a', 'b', 'c'], [1, 2, 3])))

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

# 2nd option -----------------------------------------------------------------------------------------------------------
print(" ")

combination = itertools.product(letters, nums)
for pairs in combination:
    print(pairs)

# ----------------------------------------------------------------------------------------------------------------------
print(" ")

# 2b
# ans: 6
print("{} combinations".format(len(list(itertools.combinations('ABCD', 2)))))

# ----------------------------------------------------------------------------------------------------------------------
print(" ")
# 2c
# ans: 12
print("{} permutations".format(len(list(itertools.permutations('ABCD', 2)))))

"""---------------------------------------------------------------------------------------------------------------------
Your code should produce a list of dictionaries.
Using this data, write some code that calculates and outputs the following information: 
---------------------------------------------------------------------------------------------------------------------"""
print(" ")

dictionaries = list(json.load(open('profiles.json')))

# printing dictionary of profiles from json

print(dictionaries[0].keys())
print(dictionaries[0].values())

"""---------------------------------------------------------------------------------------------------------------------
Total number of users:  
---------------------------------------------------------------------------------------------------------------------"""
print(" ")

# Number of users

users = len(dictionaries)
print("{} users. ".format(users))

"""---------------------------------------------------------------------------------------------------------------------
Total number ACTIVE of users:  
---------------------------------------------------------------------------------------------------------------------"""
print(" ")


# function for active users


def active_users():
    y = 0
    for profile in dictionaries:
        if profile["isActive"]:
            y += 1
    return y


print("{} active users. ".format(active_users()))

"""---------------------------------------------------------------------------------------------------------------------
Total number INACTIVE of users:  
---------------------------------------------------------------------------------------------------------------------"""
print(" ")


# inactive users not in active users


def inactive_users():
    x = 0
    for profile in dictionaries:
        if not profile["isActive"]:
            x += 1
    return x


print("{} inactive users. ".format(inactive_users()))

"""---------------------------------------------------------------------------------------------------------------------
Grand total balance of all users:  
---------------------------------------------------------------------------------------------------------------------"""
print(" ")

balance = [(float(dictionary['balance'].replace('$', '').replace(',', '')),
            dictionary['name']) for dictionary in dictionaries]
total_balance = sum([b[0] for b in balance])

print('${} total balance for all users'.format(total_balance))

"""---------------------------------------------------------------------------------------------------------------------
Average balance per users:  
---------------------------------------------------------------------------------------------------------------------"""
print(" ")

# average balance per user

average_balance = total_balance / users
print("${:.2f} is the average balance".format(average_balance))

"""---------------------------------------------------------------------------------------------------------------------
Lowest balance per amount:  
---------------------------------------------------------------------------------------------------------------------"""
print(" ")

balances = []
for dictionary in dictionaries:
    balances.append(dictionary['balance'])
print("{} is the minimum balance.".format(min(balances)))

"""---------------------------------------------------------------------------------------------------------------------
Lowest balance per amount:  
---------------------------------------------------------------------------------------------------------------------"""
print(" ")

balances = []
for dictionary in dictionaries:
    balances.append(dictionary['balance'])
print("{} is the maximum balance.".format(max(balances)))

"""---------------------------------------------------------------------------------------------------------------------
Most common favorite fruit
---------------------------------------------------------------------------------------------------------------------"""

print(" ")

# using count to count repeatable objects in the dictionary
fruit_counts = Counter([dictionary['favoriteFruit'] for dictionary in dictionaries])

# searching through the dictionary for favoriteFruits in a for loop
# then grabbing the entire item instead of string-by-string (I'd done that before)

most_common_fruit = max(dict(Counter([dictionary['favoriteFruit']
                                      for dictionary in dictionaries])).items(), key=lambda item: item[1])
print("The most common fruit is {}".format(most_common_fruit))
print(" ")

"""---------------------------------------------------------------------------------------------------------------------
Least common favorite fruit
---------------------------------------------------------------------------------------------------------------------"""

# using count to count repeatable objects in the dictionary
fruit_count = Counter([dictionary['favoriteFruit'] for dictionary in dictionaries])

# searching through the dictionary for favoriteFruits in a for loop
# then grabbing the entire item instead of string-by-string (I'd done that before)

least_common_fruit = min(dict(Counter([dictionary['favoriteFruit']
                                       for dictionary in dictionaries])).items(), key=lambda item: item[1])
print("The least common fruit is {}".format(least_common_fruit))

"""---------------------------------------------------------------------------------------------------------------------
Total Number of unread messages
---------------------------------------------------------------------------------------------------------------------"""
print(" ")

all_msgs = [dictionary['greeting'] for dictionary in dictionaries]
messages = []
for msg in all_msgs:
    for n in msg.split():  # split message
        if n.isdigit():  # define digit
            messages.append(n)  # append split and digit
unread_msgs = ([int(x) for x in messages])  # convert str to int in list (1 by 1 w/for loop)

print("{} is the sum of all unread messages in the json file".format(sum(unread_msgs)))
