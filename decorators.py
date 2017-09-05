
#### Before starting Decorators ####

""" Everything in python is an Object."""

## Assign functions to variables

# def greet(name):
#     return "hello "+name
#
# greet_someone = greet
# print greet_someone("Python")

## Define functions inside other functions

# def greet(name):
#     def get_message():
#         return "Hello "
#
#     result = get_message() + name  ## "Hello " + "Python"
#     return result
#
# print greet("Python")

## Functions can be passed as parameters to other functions

# def greet(name):
#    return "Hello " + name
#
# def call_func(func):
#     other_name = "Python"
#     return func(other_name)  ## greet("Python")
#
# print call_func(greet)

## Functions can return other functions
#
# def compose_greet_func():
#     def get_message():
#         return "Hello there!"
#
#     return get_message
#
# greet = compose_greet_func()
# print greet()


## Closure: Inner functions have access to the enclosing scope

# def compose_greet_func(name):
#
#     def get_message():
#         return "Hello there "+name+"!"
#
#     return get_message
#
# greet = compose_greet_func("Python")
# print greet()

#
# def outer():
#     x = 1
#     def inner():
#         print x  # 1
#     return inner
#
# foo = outer()
# print foo()

#
# print foo.func_closure


#### Decorators #####
"""Decorators provide a simple syntax for calling higher-order functions. 
By definition, a decorator is a function that takes another function and 
extends the behavior of the latter function without explicitly modifying it."""

"""This is also called metaprogramming as a part of the program tries to modify 
another part of the program at compile time."""
#
#
# def make_pretty(func):
#     def inner():
#         print "I got decorated"
#         func()
#     return inner
#
# def ordinary():
#     print "I am ordinary"
#
# print ordinary()
#
# pretty = make_pretty(ordinary)
# print pretty()
#
#
# ordinary = make_pretty(ordinary)
#
# print ordinary()
#
#
# @make_pretty      ### ordinary = make_pretty(ordinary)
# def ordinary():
#     print "I am ordinary"
#
# print ordinary()

### Decorators with parameters


# def divide(a, b):
#     return a/b

# print divide(8, 5.0)
# print divide(2, 0)


# def smart_divide(func):
#     def inner(a, b):
#         print "I am going to divide", a, "and", b
#         if b == 0:
#             print "Whoops! cannot divide"
#             return
#
#         return func(a, b)
#     return inner
#
# @smart_divide
# def divide(a, b):
#     return a/b
#
# print divide(8, 5)
# print divide(2, 0)


### Common Decorator ##

# def works_for_all(func):
#     def inner(*args, **kwargs):
#         print("I can decorate any function")
#         return func(*args, **kwargs)
#     return inner
# #
# def logger(func):
#     def inner(*args, **kwargs):  # 1
#         print "Arguments were: %s, %s" % (args, kwargs)
#         return func(*args, **kwargs)  # 2
#     return inner
#
# @logger
# def foo1(x, y=1):
#     return x * y
#
# @logger
# def foo2():
#     return 2
#
# print foo1(2, 4)
#
# print foo1(5, y=3)
#
# print foo2()


### Chaining Decorators

# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#     return inner
#
# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 30)
#         func(*args, **kwargs)
#         print("%" * 30)
#     return inner
#
# @star
# @percent
# def printer(msg):
#     print(msg)
# printer("Hello")


#### Iterators ####

""" Iterators are objects that can be iterated upon. """

"""
For loops are used to loop over a iterables

if we use it with a list, it loops over its elements
if we use it with a string, it loops over its characters
If we use it with a dictionary, it loops over its keys.
If we use it with a file, it loops over lines of the file.
"""

"""There are many functions which consume these iterables."""

# print "".join(["a", "b", "c"])
#
# print ",".join({"x": 1, "y": 2})
#
# print list("python")  ### [], [].append
#
# print list({"x": 1, "y": 2})


## The Iteration Protocol

"""Python iterator object must implement two special methods, 
__iter__() and i.__next__(), collectively called the iterator protocol."""



# variable_name = iter(sequence)

# my_iterator = iter([1, 2, 3])
#
# print my_iterator.next()
#
# print my_iterator.next()
#
# print my_iterator.next()
#
# print my_iterator.next()


# ## For Loops Behind the Scenes
#
# for element in iterable:
#     # do something with element
#
#
# # create an iterator object from that iterable
# iter_obj = iter(iterable)
#
# # infinite loop
# while True:
#     try:
#         # get the next item
#         element = next(iter_obj)
#         # do something with element
#     except StopIteration:
#         # if StopIteration is raised, break from loop
#         break


# for i in range(5):
#     print i

#
# iter_obj = iter(range(5))
#
# while True:
#     try:
#         i = iter_obj.next()
#         print i
#     except StopIteration:
#         break



### Custom Iterator ###

# class PowerTwo:
#     """Class to implement an iterator
#     of powers of two"""
#
#     def __init__(self, max = 0):  #### max=0 or whatever is passed to the class, in our case max =5
#         self.max = max
#
#     def __iter__(self):
#         self.n = 0                ### n = 0
#         return self
#
#     def __next__(self):
#         if self.n <= self.max:     ### if n <= max
#             result = 2 ** self.n   #### result = 2 ** n
#             self.n += 1            ### n = n + 1
#             return result
#         else:
#             raise StopIteration
#
# a = PowerTwo(5)
#
# i = iter(a)
#
# print i.__next__()
#
# print i.__next__()
#
# print i.__next__()
#
# print i.__next__()
#
# print i.__next__()
#
# print i.__next__()
#
# print i.__next__()



####### Generators #######

""" a generator is a function that returns a generator object (iterator) which we can iterate over (one value at a time)."""


# # Build and return a list
# def firstn(n):
#     num, nums = 0, []
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums
#
# sum_of_first_n = sum(firstn(1000000))


# a generator that yields items instead of returning a list
# def firstn(n):
#     num = 0
#     while num < n:
#         yield num     ### Stopssss
#         num += 1
#
# sum_of_first_n = sum(firstn(1000000))


#### Yield Keyword ###
""" When a function that is executing encounters the yield keyword, 
it suspends execution at that point, saves its context and returns 
to the caller along with any value in the expression_list; 
when the caller invokes next on the object, execution of the function 
continues till another yield or return is encountered or end of function is reached. """


#
# def my_gen():
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n   ### n = 1
#
#     n += 1
#     print('This is printed second')
#     yield n   #### n = 2
#
#     n += 1
#     print('This is printed at last')
#     yield n    ### n =3
#
#
# print my_gen()
# print type(my_gen())
# a = my_gen()
#
# print next(a)
#
# print next(a)
#
# print next(a)
#
# ### For loop directly on generators
#
# for i in my_gen():
#     print i


### Types of Generators

# Generator Function
# Generator Expression


# numbers = [1, 2, 3, 4, 5, 6]
#
# # print [x * x for x in numbers]
#
# lazy_squares = (x * x for x in numbers)
#
# print lazy_squares
# print type(lazy_squares)
# print next(lazy_squares)
#
# print next(lazy_squares)
#
# print list(lazy_squares)


### Advantages ###


# 1. Easy to implement
"""
we earlier today saw the implementation of iterator for calculating power of two
and here is the example using generator function.
"""
# def PowTwoGen(max = 0):
#     n = 0
#     while n < max:
#         yield 2 ** n
#         n += 1



# 2. Memory Efficient
"""
A normal function to return a sequence will create the entire sequence 
in memory before returning the result. This is an overkill if the number 
of items in the sequence is very large.

Generator implementation of such sequence is memory friendly and is 
preferred since it only produces one item at a time.
"""

# 3. Infinite stream of data
""" Infinite streams cannot be stored in memory and since generators produce only one item at a time, 
it can represent infinite stream of data."""


### Tip to get started with generators: find places in your code where you do the following:

# def something():
#     result = []
#     for x in ...:
#         result.append(x)
#     return result
#
#
# def iter_something():
#     for x in ...:
#         yield x
