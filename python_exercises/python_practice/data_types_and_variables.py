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



