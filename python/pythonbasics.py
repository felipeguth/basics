
# Practice sites HackerRank and Codewars.
#
# Data Structure	Ordered	Mutable	Constructor	Example
# int	NA	NA	int()	5
# float	NA	NA	float()	6.5
# string	Yes	No	' ' or " " or str()	"this is a string"
# bool	NA	NA	NA	True or False
# list	Yes	Yes	[ ] or list()	[5, 'yes', 5.7]
# tuple	Yes	No	( ) or tuple()	(5, 'yes', 5.7)
# set	No	Yes	{ } or set()	{5, 'yes', 5.7}
# dictionary	No	Keys: No	{ } or dict()	{'Jun':75, 'Jul':89}


set_a = set(1,2,3,3,3,4) //sets do not store repeated values

# compund data structures - dictionary of dict, list of dicts etc

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True


# Conditions
# Here are most of the built-in objects that are considered False in Python:
#
# constants defined to be false: None and False
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '"", (), [], {}, set(), range(0)
is_cold = True

# Bad example
if is_cold == True:
    print("The weather is cold!")

# Good example
if is_cold:
    print("The weather is cold!")


errors = 3
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")


# Loops

#for with range
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()


items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)


cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }


for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))


# For loops are an example of "definite iteration" meaning that the loop's body is run a predefined number of times. This differs from "indefinite iteration" which is when a loop repeats an unknown number of times and ends when some condition is met, which is what happens in a while loop. Here's an example of a while loop.

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  < 17:
    hand.append(card_deck.pop())



# break terminates a loop
# continue skips one iteration of a loop



# zip returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables.
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. You'll often use this when you want the index along with each element of an iterable in a loop

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)




