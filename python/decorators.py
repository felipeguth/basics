#A decorator is a design pattern in Python that allows a user to add new functionality to an
# existing object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate.

#Decorators dynamically alter the functionality of a function, method, or class without having to directly use
# subclasses or change the source code of the function being decorated.
def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'


print(say_hi())


def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

print(cities("Nairobi", "Accra"))


#Defining General Purpose Decorators
#To define a general purpose decorator that can be applied to any function we use
# args and **kwargs. args and **kwargs collect all positional and keyword arguments and stores them in
# the args and kwargs variables. args and kwargs allow us to pass as many arguments as we would like during function calls.
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1,2,3)

#Keyword arguments are passed using keywords
@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")


#Passing Arguments to the Decorator
#Now let's see how we'd pass arguments to the decorator itself. In order to achieve this, we define a
#decorator maker that accepts arguments then define a decorator inside it.
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")



#Debugging Decorators
print('\n')
print(decorated_function_with_arguments.__name__)
print(decorated_function_with_arguments.__doc__)


import functools

def uppercase_decorator(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper


@uppercase_decorator
def say_hi():
    "This will say hi"
    return 'hello there'

print(say_hi())
print(say_hi.__doc__)