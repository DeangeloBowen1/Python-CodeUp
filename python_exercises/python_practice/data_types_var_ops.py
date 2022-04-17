"""
bool: boolean values, either True or False; an answer to a yes/no question
str (string) a sequence of characters "strung" together
int: whole, or counting numbers
float: decimal numbers
list: an ordered sequence of objects
dict: a collection of values that have names
NoneType: a special value that indicates absence of a value
"""

# Examples
type(123)
# returns int

type('hello')
# returns str

type(True)
# returns bool

## Variables

favorite_number = 42
n = favorite_number + 7

x = 1
print(x)
x = x + 1
print(x)
x = x * 3 + x
print(x)

"""
Booleans:

True == True=
True

True == False =
False

True != True =
False

True != False =
True
"""

"""
String formatting operators:

name = 'World' # variable 

'Hello, %s!' % name =
'Hello, World!'

'Hello, {}!'.format(name) =
'Hello, World!'

f'Hello {name}!' =
'Hello World!'
"""


"""
String methods
"""

""""
s = 'Hello, Codeup!' # variable

s.lower()

# returns : hello, codeup!

s.strip()

# 'Hello, Codeup!'

s.isdigit()

# False

'123'.isdigit()

# True

s.strip().split(', ')

# ['Hello', 'Codeup!']

', '.join(['one', 'two', 'three'])

# 'one, two, three'"""

"""

LISTS : 

numbers = [1, 2, 3]

numbers.append(4)
numbers

[1, 2, 3, 4]

numbers.pop()
numbers

[1, 2, 3]
"""

"""
DICTIONARIES:

Dictionaries can be created by writing a dictionary literal, which is delimeted with curly braces, and the keys are separated from the values with a colon, and key-value pairs are separated by commas.


{'name': 'Codeup', 'age': 4}
=
{'name': 'Codeup', 'age': 4
}
Dictionaries can also be created with the built-in dict function:

dict(name='Codeup', age=4) = {'name': 'Codeup', 'age': 4}


You can access values in a dictionary by their name, using a similar syntax to the way that list elements are accessed.

school = dict(name='Codeup', age=4)

school['name'] ='Codeup'


'school['age'] += 1　

school '

=

{'name': 'Codeup', 'age': 5}
"""
