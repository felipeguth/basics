#documentation
def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area


#lamda expresions

# You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name.
    # They are helpful for creating quick functions that aren’t needed later in your code

def multiply(x, y):
    return x * y

#can be reduced to
multiply = lambda x, y: x * y

multiply(4, 7)


#Generators are a simple way to create iterators using functions. You can also define iterators using classes

def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

# This allows the function to return values one at a time, and start where it left off each time it’s called.
# This yield keyword is what differentiates a generator from a typical function.

# https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/



#Scripting

#raw input
name = input("Enter your name: ")
print("Hello there, {}!".format(name.title()))

#error handling
try:
    # some code
    print(0)
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))





#the statndar library


























