
####### Functions #######
"""A function is a block of organized, reusable code
that is used to perform a single, related action.
Functions provide better modularity for your application
and a high degree of code reusing."""

"""Functions are a convenient way to divide your code 
into useful blocks, allowing us to order our code, 
make it more readable, reuse it and save some time. 
"""

## Syntax

# def function_name(parameters/arguments):
# 	"""docstring"""
# 	statement(s)
#     return expression


## Actual function

# def my_function():
#     print("Hello From My Function!")


## Calling a function

# my_function()


## Fuction with arguments

# def greet_user(name):  ## name = 'Adhish'
#     """This function greets to
#     the person passed in as
#     parameter"""
#     print("Hello, " + name + ". Good morning!")
#
# greet_user(raw_input("Enter your name: "))



# def add_two_numbers(number1, number2): ## number1 = 1, number2 = 2
#     print number1 + number2  # print 1 + 2
#
#
# add_two_numbers(1, 2)


## How function works

# Explain on pythontutor


## Pass by reference

# def append_list(my_list):  # my_list = some_list
#     "This changes a passed list into this function"
#     my_list.append(40)
#     print "Values inside the function: ", my_list
#
# # Now you can call append_list function
# some_list = [10, 20, 30]
# append_list(some_list)
# print "Values outside the function: ", some_list


## Function with return statement

# def absolute_value(num):
#     """This function returns the absolute
#     value of the entered number"""
#
#     if num >= 0:
#         return num
#     else:
#         return -num
#
# # Output: 2
# print absolute_value(2)
# # print "I am the value from return: ", x
#
# # Output: 4
# print absolute_value(-4)


## Scope of Variables


# def my_func():
#     x = 10
#     print "Value inside function:", x
#
#
# x = 20
# my_func()
# print "Value outside function:", x


##### Function Arguments ####

## Required

# def greet(name, msg="Good Morning"):
#    """This function greets to
#    the person with the provided message"""
#    print "Hello",name + ', ' + msg
#
# greet("Monica")


## Default

# def greet(name, msg="Good morning!"):
#    """
#    This function greets to
#    the person with the
#    provided message.
#
#    If message is not provided,
#    it defaults to "Good
#    morning!"
#    """
#
#    print "Hello", name + ', ' + msg
#
# greet("Kate")
# greet("Bruce", "How do you do?")


## Keyword

# def print_me( str ):
#    "This prints a passed string into this function"
#    print str
#
# # Now you can call printme function
# print_me(str="My string")


## Arbitrary Arguments

# def test_var_args(f_arg, *args):
#     print "first normal arg:", f_arg
#     for arg in args:
#         print "another arg through *args :", arg
#
# test_var_args('Ice Cream', 'python', 'eggs', 'test')


# def greet_me(**kwargs):
#     if kwargs is not None:
#         for key, value in kwargs.iteritems():  ## list of tuples
#             print "%s == %s" % (key, value)
#
# greet_me(name="Admin", session="Python")

# def some_func(required_arg, *args, **kwargs):
#     print required_arg
#     if args:
#         print args
#     if kwargs:
#         print kwargs
#
# some_func("required argument", 1, 2, '3', keyword1=4, keyword2="foo")


##### Recursion #####
"""In Python, a function can call other functions. 
It is even possible for the function to call itself."""

"""a function is recursive if it calls itself and has a termination condition."""


# def add_everthing_inside_list(list):
#     sum = 0
#
#     # Add every number in the list.
#     for i in range(0, len(list)):  ## loop through index
#         sum += list[i]
#
#     # Return the sum.
#     return sum
#
# print add_everthing_inside_list([1, 2, 3, 4])

#
# def add_everthing_inside_list(list):
#     if len(list) == 1:
#         return list[0]
#     else:
#         return list[0] + add_everthing_inside_list(list[1:])
#
#
# # 1st call..
# # list = [10, 20, 30, 40]
# #
# # 10 + 20 + 30 + 40
# #
# # 2nd call
# #
# # list = [20,30,40]
# #
# # 20 + 30 + 40
# #
# # 3rd call.
# # list = [30, 40]
# #
# # 30 + 40
# #
# # 4th call..
# # list = [40]
# # 40
#
# print add_everthing_inside_list([10, 20, 30, 40])


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         res = n * factorial(n-1)
#         return res
#
# print factorial(5)


#### Anonymous function ####
"""In Python, anonymous function is a function that is defined without a name."""


## Syntax:

# lambda arguments: expression

# sum = lambda arg1, arg2: arg1 + arg2;
#
# print sum(10, 20)
#
# def sum(arg1, arg2):
#     return arg1 + arg2
#
# print sum(10, 20)

# print (lambda x, y: x + y)(5, 3)









##### Modules #####
"""Modules refer to a file containing Python statements and definitions"""

"""A file containing Python code, for e.g.: example.py, is called a module and its module name would be example."""


### example

## Python Module example

# import example_moduke
#
# print example_moduke.add(10, 20)


## How to import modules

# import example_moduke
#
# print example_moduke.add(10, 20)


## few more modules

# import math
# print "The value of pi is", math.pi

#
# import math as m
# print "The value of pi is", m.pi


## From keyword

# from example_moduke import add
#
# print add(10, 20)

# from math import pi
# print "The value of pi is", pi

# from math import *  ## Not a good practice
# print "The value of pi is", pi


### Python module search path
"""
While importing a module, Python looks at several places. 
Interpreter first looks for a built-in module then (if not found)
into a list of directories defined in sys.path. The search is in this order.

1. The current directory.
2. PYTHONPATH (an environment variable with a list of directory).
3. The installation-dependent default directory.
"""

# import sys
#
# print sys.path


#### Built in Modules

""" datetime, math, random, os etc"""

# import os
# print os.getcwd()

# import random
# print random.randint(0, 100)


## Install a new module

# import numpy


#### Dir function
""" The dir() built-in function returns a sorted list of strings 
containing the names defined by a module. The list contains the names of 
all the modules, variables and functions that are defined in a module."""

# import random
# print dir(random)
#
# import example_moduke
# print dir(example_moduke)


### if __name__ == "__main__":

""" Every module in python has a special attribute called __name__ . 
The value of __name__  attribute is set to '__main__'  when module run as main program. 
Otherwise the value of __name__  is set to contain the name of the module."""

## Datetime Module

#
# create_date = datetime.datetime(2017, 8, 4, 12, 30, 45)
# #
# print create_date
# #
# print type(create_date)
# #
# print create_date.year, create_date.month, create_date.day
# print create_date.hour, create_date.minute, create_date.second
# print create_date.microsecond


# print datetime.datetime.today()
# now = datetime.datetime.now()
# print now
# # print now.strftime("%Y-%m-%d %H:%M:%S")
# #
# # print now.strftime("%H:%M:%S")
# #
# # print now.date()
# # print now.time()
# #
# print datetime.datetime.utcnow()


## Python Packages

"""Packages are namespaces which contain multiple packages and modules themselves. 
They are simply directories, but with a twist.

Each package in Python is a directory which MUST contain a special file called __init__.py. 
This file can be empty, and it indicates that the directory it contains is a Python package, 
so it can be imported the same way a module can be imported."""

# from iampackage import example_moduke
#
# print example_moduke.add(10, 30)


### Zen of python
#
# import this