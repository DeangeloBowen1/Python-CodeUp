from function_exercises import is_vowel as v, calculate_tip
import itertools

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

print(list(zip(['a', 'b', 'c'], [1, 2, 3])))

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

# 2nd option -----------------------------------------------------------------------------------------------------------
combination = itertools.product(letters, numbers)
for pairing in combination:
    print(pairing)

# ----------------------------------------------------------------------------------------------------------------------
# 2b
# ans: 6
print("combinations: ", len(list(itertools.combinations('ABCD', 2))))

# ----------------------------------------------------------------------------------------------------------------------
# 2c
# ans: 12
print("permutations: ", len(list(itertools.permutations('ABCD', 2))))
