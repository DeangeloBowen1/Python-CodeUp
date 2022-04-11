"""
DeAngelo Bowen
CodeUp
Python Data Types and Variables Exercises
"""
"""
1. You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear 
(for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). 
If price for a movie per day is 3 dollars, how much will you have to pay?
"""

movie_tickets = 0
print("Movie tickets cost ", movie_tickets)

# after the little mermaid movie for 3 days
little_mermaid = 3 * 3
print("After the little mermaid, movie tickets cost: ", movie_tickets + little_mermaid)
movie_tickets += little_mermaid

# after brother bear
brother_bear = 5 * 3
print("After brother bear, tickets cost: ",  movie_tickets + brother_bear)
movie_tickets += brother_bear

# after hercules
hercules = 1 * 3
print("After hercules, tickets cost: ", movie_tickets + hercules)

"""
Suppose you're working as a contractor for 3 companies:
Google, Amazon and Facebook, they pay you a different rate per hour.
Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
How much will you receive in payment for this week?
You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
"""

google = 400
amazon = 380
facebook = 350

my_pay = ((google*6)+(facebook*10)+(amazon*4))
print("My pay for the week is $", my_pay)

"""
A student can be enrolled to a class only if the class is not full
and the class schedule does not conflict with her current schedule.
"""


class_not_full = True
schedule_not_full = False
student_can_enroll = class_not_full and schedule_not_full
print(f'Can the student enroll? \n {student_can_enroll}')

"""
A product offer can be applied only if people buys more than 2 items, and the offer has not expired.
 Premium members do not need to buy a specific amount of products.
"""

is_premium_member = True
more_than_two_items = False

offer_not_expired = True
discount_valid = offer_not_expired and (is_premium_member or more_than_two_items)
print(discount_valid)

"""
Create a variable that holds a boolean value for each of the following conditions:

the password must be at least 5 characters
the username must be no more than 20 characters
the password must not be the same as the username
bonus neither the username or password can start or end with whitespace
"""

username = 'codeup'
password = 'notastrongpassword'

password_is_long_enough = len(password) >= 5
username_is_short_enough = len(username) <= 20
username_and_password_are_different = username != password
username_has_spaces = username != username.strip()
password_has_spaces = password != password.strip()

username_good = username_is_short_enough and username_and_password_are_different and (not username_has_spaces)
password_good = password_is_long_enough and username_and_password_are_different and (not password_has_spaces)

valid_credentials = username_good and password_good

print('Username good?')
print(username_good)
print('Password good?')
print(password_good)
print('credentials valid?')
print(valid_credentials)

