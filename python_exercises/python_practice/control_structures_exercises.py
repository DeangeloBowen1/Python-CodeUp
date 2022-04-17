# Conditional Basics
# A. prompt the user for a day of the week, print out whether the day is Monday or not
import sys

day = input("Enter the day: ")
if day.lower() == 'monday':
    print('Today is Monday!')
else:
    print('Today is not Monday.')

# B.　prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day = input("Enter the day: ")
if day.lower() in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
    print('Today is a weekday.')
else:
    print('Today is a weekend.')

# C.　create variables and make up values for
#
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hours_worked = 43
hourly_rate = 25

if hours_worked <= 40:
    paycheck = hours_worked * hourly_rate
    print(paycheck)
else:
    paycheck = (hours_worked - 40) * 1.5 * hourly_rate + (40 * hourly_rate)
    print(paycheck)

# Question 2 - Loop Basics
# A. While
#
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1

i = 0
while i <= 100:
    print(i)
    i += 2

i = 100
while i >= -10:
    print(i)
    i -= 5

i = 2
while i <= 100_000_000:
    print(i)
    i **= 2

# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= 5:
    print(i)
    i -= 5

# B. Write some code that prompts the user for a number,
# then shows a multiplication table up through 10 for that number.
#
# For example, if the user enters 7, your program should output:

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(str(number) + " x " + str(i) + " = " + str(i * number))

for n in range(1, 10):
    print(str(n) * n)

# C. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement
# to continue prompting the user if they enter invalid input.
# (Hint: use the isdigit method on strings to determine this)
# . Use a loop
# and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered

while True:
    number = input("Enter an odd number between 1 and 50: ")
    print("\n")

    if number.isdigit():
        if int(number) % 2 == 1 and int(number) < 50:
            break

print("Number to skip is: " + str(number))
print("\n")

for n in range(1, 50, 2):
    if n == int(number):
        print("Skipping number: ", number)
        continue
    print("Here is an odd number: ", n)

# D. The input function can be used to prompt for input and use that input in your python code.
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number.
# (Hints: first make sure that the value the user entered is a valid number,
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)

while True:
    pos_number = input("Enter a positive number: ")

    if pos_number.isdigit():
        if int(pos_number) > 0:
            break

for n in range(0, int(pos_number) + 1):
    print(n)

# E. Write a program that prompts the user for a positive integer.
# Next write a loop that prints out the numbers from the number the user entered down to 1.

while True:
    pos_int = input("Enter a positive integer: ")

    if pos_int.isdigit():
        if int(pos_int) > 0:
            break

for n in range(int(pos_int), 0, -1):
    print(n)

# Question 3 - Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test.
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
#
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

# Question 4 - Table of Powers
# Display a table of powers.
#
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
table = True

while table:
    try:
        number = int(input("Press any key to open menu, or enter an integer: "))
        print("\n")
        print("Here is your table!")
        print("\n")
        print("number | squared | cubed")
        for i in range(1, number + 1):
            first = str(i)
            square = str(i ** 2)
            cube = str(i ** 3)
            print(first + " " * (7 - len(first)) + "| ", end="")
            print(square + " " * (8 - len(square)) + "| ", end="")
            print(cube)
    except ValueError:
        print("You did not enter an integer.")
        print(" ")
        cont = input("Would you like to continue? (Y/N)").upper()
        if cont == 'Y':
            continue
        elif cont == 'N':
            table = False
        else:
            continue

"""--------------------------------------------------------------------------------------------------------------------
Question 5: 
Convert given number grades into letter grades.

Prompt the user for a numerical grade from 0 to 100.
Display the corresponding letter grade.
Prompt the user to continue.
Assume that the user will enter valid integers for the grades.
The application should only continue if the user agrees to.
--------------------------------------------------------------------------------------------------------------------"""

grades = True

while grades:
    grade = input("Enter a numerical grade from 0 to 100: ")
    grade = int(grade)

    if grade >= 88:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 67:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")
    grades = input(f'Would you like to enter another grade? ("Y/N"):') == "Y"

"""--------------------------------------------------------------------------------------------------------------------
Question 6: 
Create a list of dictionaries where each dictionary represents a book that you have read.
 Each dictionary in the list should have the keys title, author, and genre. 
 Loop through the list and print out information about each book.

Prompt the user to enter a genre,
then loop through your books list and print out the titles of all the books in that genre.
--------------------------------------------------------------------------------------------------------------------"""

books = [{"title": "Ready Player One", "author": "Ernest Cline", "genre": "Science Fiction"},
         {"title": "Rich Dad, Poor Dad", "author": "Robert Kiyosaki", "genre": "Personal Finance"},
         {"title": "Cashflow Quadrant", "author": "Robert Kiyosaki", "genre": "Personal Finance"},
         {"title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction"},
         {"title": "The Maze Runner", "author": "James Dashner", "genre": "Science Fiction"},
         {"title": "48 Laws of Power", "author": "Robert Greene", "genre": "Politics"},
         ]

"""
To print just books exmaple:

for book in books:
    [print(key, ': ', book[key]) for key in book]
    print('------')
"""

# Genre prompt

print("From what we have on file, please select input of the following Genre-Types:\n ")
menu = {'A': 'Science Fiction',
        'B': 'Personal Finance',
        'C': 'Politics'}
options = menu.keys()
for entry in options:
    print(entry, menu[entry])
print(" ")

selection = input('Input selection here: \n').lower()
matches = []
for book in books:
    if book['genre'].lower() == selection.lower():
        matches.append(book['title'])
if matches == []:
    print('no books in that genre available. please check back later')
else:
    print(f'I have the following titles in the selected genre: \n')
    [print(match) for match in matches]
