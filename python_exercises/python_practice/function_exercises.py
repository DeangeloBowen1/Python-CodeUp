import numpy as np

"""---------------------------------------------------------------------------------------------------------------------
1. Define a function named is_two. It should accept one input and return True
 if the passed input is either the number or the string 2, False otherwise.
---------------------------------------------------------------------------------------------------------------------"""


def is_two(t):
    # if statement take the int 2 or string 2 and returns true
    if t == 2 or t == '2':
        return True
    else:
        return False


"""---------------------------------------------------------------------------------------------------------------------
2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
---------------------------------------------------------------------------------------------------------------------"""


def is_vowel(v):
    # if statement reads if v is equal to a vowel in this set and returns true or false.
    if v in {'a', 'e', 'i', 'o', 'u'}:
        return True
    else:
        return False


"""---------------------------------------------------------------------------------------------------------------------
3. Define a function named is_consonant. 
It should return True if the passed string is a consonant, False otherwise. 
Use your is_vowel function to accomplish this.
---------------------------------------------------------------------------------------------------------------------"""


def is_consonant(vowel):
    # if statement reads, "if vowel is in this set", and returns false
    # this allows us to read that we are not looking for vowels.
    if vowel in {'a', 'e', 'i', 'o', 'u'}:
        return False
    else:
        return True


"""---------------------------------------------------------------------------------------------------------------------
4.Define a function that accepts a string that is a word.
 The function should capitalize the first letter of the word if the word starts with a consonant.
---------------------------------------------------------------------------------------------------------------------"""


def capital_consonant(c):
    # function c[0] reads the first position of the string and returns to capitalize if it is not in the set
    if c[0] in {'a', 'e', 'i', 'o', 'u'}:
        return c
    else:
        return c.capitalize()


"""---------------------------------------------------------------------------------------------------------------------
5. Define a function named calculate_tip. It should accept a tip percentage 
(a number between 0 and 1) and the bill total,
and return the amount to tip.
---------------------------------------------------------------------------------------------------------------------"""


def calculate_tip(n, payment):
    # calculation for tip. Takes the float n, and the float payment and performs percent calculation and simple addition
    n = (n * payment) / 100
    return n + payment


"""---------------------------------------------------------------------------------------------------------------------
6. Define a function named apply_discount. It should accept a original price, and a discount percentage,
and return the price after the discount is applied.
---------------------------------------------------------------------------------------------------------------------"""


def apply_discount():
    # takes inspiration from the tip amount but subtracts instead of adds.
    discount = (x * price) / 100
    discount_amount = price - discount
    return discount_amount


"""---------------------------------------------------------------------------------------------------------------------
7. Define a function named handle_commas. 
It should accept a string that is a number that contains commas in it as input, and return a number as output.
---------------------------------------------------------------------------------------------------------------------"""


def handle_commas(y):
    # @replace : replaces the comma string with a closed space.
    # considered a makeshift remove and concat.
    return int(y.replace(',', ''))


"""---------------------------------------------------------------------------------------------------------------------
8. Define a function named get_letter_grade.
It should accept a number and return the letter grade associated with that number (A-F)
---------------------------------------------------------------------------------------------------------------------"""


def get_letter_grade(grade):
    # if statement to take the int grade and prints a letter grade based on score
    if 100 >= grade >= 90:
        print(f"Grade score of {grade} is an A")  # formatted grade to be easily input in the string.
    elif 89 >= grade >= 80:
        print(f"Grade score of {grade} is a B")
    elif 79 >= grade >= 70:
        print(f"Grade score of {grade} is a C")
    elif 69 >= grade >= 60:
        print(f"Grade score of {grade} is a D")
    else:
        print(f"Grade score of {grade} is an F")
    return grade


"""---------------------------------------------------------------------------------------------------------------------
9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
---------------------------------------------------------------------------------------------------------------------"""


def remove_vowel(mylist):
    # forces vowels into a list
    vowels = ['a', 'e', 'i', 'o', 'u']
    # reads the length of the string mylist
    for i in range(len(mylist)):
        for v in vowels:  # assign v to vowels
            # similar to above, replaces the vowel in the string with an emtpy spot (removes)
            mylist[i] = mylist[i].replace(v, "")
    return mylist


"""---------------------------------------------------------------------------------------------------------------------
10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:

anything that is not a valid python identifier should be removed
leading and trailing whitespace should be removed
everything should be lowercase
spaces should be replaced with underscores

for example:

Name will become name
First Name will become first_name
% Completed will become completed
---------------------------------------------------------------------------------------------------------------------"""


def normalize_name(strn):
    # initialize output to be an empty space
    output = ''
    strn = strn.lower()  # sets all string input to lowercase
    for character in strn:
        if character.isidentifier() or character == ' ':
            output += character  # reads over spaces in string
    output = output.strip()
    output = output.replace(' ', '_')  # replaces spaces in string with "_"
    return output


"""---------------------------------------------------------------------------------------------------------------------
Write a function named cumulative_sum that accepts a list of numbers and returns a list that is
the cumulative sum of the numbers in the list.

Ex:

cumulative_sum([1, 1, 1]) returns [1, 2, 3]
cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
---------------------------------------------------------------------------------------------------------------------"""


def cumulative_sum(mynumlist):
    # simple np function that cumulates the number in a list or set.
    mynumlist = np.cumsum(mynumlist)
    return mynumlist


"""---------------------------------------------------------------------------------------------------------------------
Bonus: 
Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that
 is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
---------------------------------------------------------------------------------------------------------------------"""


# using a list, we change the driver set time to change the values of time from 12 hour to 24 hour.


def twelveto24(str1):
    # Checking if last two elements of time are am and the first two are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    # as 12 to hours and remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]
    # Checks if last two elements of time are pm and the first two are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]


"""---------------------------------------------------------------------------------------------------------------------
Bonus 2:
Create a function named col_index. It should accept a spreadsheet column name, 
and return the index number of the column:

col_index('A') returns 1
col_index('B') returns 2
col_index('AA') returns 27
---------------------------------------------------------------------------------------------------------------------"""


def col_index(col_str):
    # Convert base26 column string to number.
    expn = 0
    col_num = 0
    for char in reversed(col_str):
        col_num += (ord(char) - ord('A') + 1) * (26 ** expn)
        expn += 1

    return col_num


"""---------------------------------------------------------------------------------------------------------------------
Main run
---------------------------------------------------------------------------------------------------------------------"""

if __name__ == '__main__':
    print("Is Two Function: ")
    print(is_two(2))
    print(is_two('2'))
    print(is_two(50))
    print(is_two('50'))
    print(" ")

    print("Is Vowel Function: ")
    print(is_vowel('a'))
    print(is_vowel('f'))
    print(is_vowel('h'))
    print(is_vowel('e'))
    print(" ")

    print("Is Consonant Function: ")
    print(is_consonant('a'))
    print(is_consonant('f'))
    print(is_consonant('h'))
    print(is_consonant('e'))
    print(" ")

    print("Capital consonant function: ")
    print(capital_consonant('forgotten'))
    print(capital_consonant('apple'))
    print(capital_consonant('ringo'))
    print(" ")

    print(calculate_tip(1, 100))

    price = float(input("Please enter the price of the object: "))
    x = float(input("Enter a discount amount: "))
    print("The total amount is $", apply_discount())
    print(" ")

    print(handle_commas('67,342,123'))
    print(handle_commas('56,812'))
    print(handle_commas('12,221'))
    print(" ")

    get_letter_grade(89)
    get_letter_grade(71)
    get_letter_grade(100)
    get_letter_grade(62)
    print(" ")

    print('Before: ', ["apple", "pie", "1", "banana", "jackson", "455"])
    print("After: ")
    print(remove_vowel(["apple", "pie", "1", "banana", "jackson", "455"]))
    print(" ")

    print(normalize_name("Deangelo Bowen"))
    print(normalize_name("! & gulag %"))
    print(" ")

    print(twelveto24("10:45 AM"))
    print(twelveto24("04:30 PM"))

    print(cumulative_sum([1, 1, 1]))
    print(cumulative_sum([1, 2, 3, 4]))

    print(col_index('A'))
    print(col_index('B'))
    print(col_index('AA'))
