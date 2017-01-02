# Various Python Topics

# *args and **kwargs
# arguments and key word arguments
def my_method(arg1, arg2):
    return arg1 + arg2

# *args passes in as a list
def my_method(*args):
    return sum(args)

def what_are_kwargs(*args, **kwargs):
    print args
    print kwargs

what_are_kwargs(21, 41, name="John", last="Smith")

# Passing functions as parameters
def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

# Lambda functions
print methodception(lambda: 35 + 77)

my_list = [13, 56, 77, 484]

print list(filter(lambda x: x != 13, my_list))

def not_thirteen(x):
    return x != 13

print list(filter(not_thirteen, my_list))

# Using list comprehensions
print ([x for x in my_list if x != 13])

# decorators - a function that gets called before another functions
import functools

# way decorators are built
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print "In the decorator"
        func()
        print("After the decorator")
    return function_that_runs_func

@my_decorator
def my_function():
    print "I'm the function"

my_function()

###### More advanced decorators #######

# Decorators without parameters
def decorator_with_arguments_no_params(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func():
            print "In the decorator"
            if number == 56:
                print "Not running the function"
            else:
                func()
            print "After the decorator"
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments_no_params(56)
def my_function_too():
    print "Hello"

my_function_too()

# Decorators with parameters
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print "In the decorator"
            if number == 56:
                print "Not running the function"
            else:
                func(*args, **kwargs)
            print "After the decorator"
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(56)
def my_function_too():
    print "Hello"

my_function_too()
