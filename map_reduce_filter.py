##### Map, Filter and Reduce ####


# items = [1, 2, 3, 4, 5]
# squared = []
# for x in items:
#     squared.append(x ** 2)
#
# print squared


#### Map #####
""" Map is a built in function which applies passed function to sequences and other iterables. """

## Syntax

"""r =  map(function, sequence)"""

# items = [1, 2, 3, 4, 5]
#
# def sqr(x):
#     return x ** 2
#
# print list(map(sqr, items))
#
#
# print list(map((lambda x: x **2), items))

#
# m = [1, 2, 3]
# n = [1, 4, 9]
# new_tuple = map(None, m, n)   ### [(1, 1), (2, 4), (3, 9)]
# print new_tuple


# def sum(x, y):
#     return x + y
#
# r = map(sum, [1, 2, 3, 4], [5, 6, 7, 8])  ## [(1, 5), (2, 6) ...]
# print r


""" The map call is similar to the list comprehension expression. 
But map applies a function call to each item instead of an arbitrary expression."""


#### Filter ####
""" As the name suggests filter extracts each element in the sequence for which the function returns True """

## Syntax
""" r =  filter(function, sequence) """

# def even(x):
# 	return x%2 == 0  ## Boolean
#
# r = filter(even, [1,2,3,4])
# print r
#
# a = [1,2,3,5,7,9]
# b = [2,3,5,6,7,8]
# print filter(lambda x: x in a, b)


#### Reduce ####

"""The 'reduce' function will transform a given list into a single value 
by applying a given function continuously to all the elements. 
It basically keeps operating on pairs of elements until there are no more elements left. """

## Syntax
""" r =  reduce(function, sequence) """

# product = 1
# list = [1, 2, 3, 4]
# for num in list:
#     product = product * num
# print product

# print reduce((lambda x, y: x * y), [1, 2, 3, 4])


### Example using all three

# people = [{'name': 'Mary', 'height': 160},
#           {'name': 'Isla', 'height': 80},
#           {'name': 'Sam'}]
#
# # print filter(lambda x: 'height' in x, people)
#
# heights = map(lambda x: x['height'], filter(lambda x: 'height' in x, people))
#
# print heights
# # from operator import add
# # print reduce(add, heights)
# ## map (function, sequence)
#
# if len(heights) > 0:
#     from operator import add
#     average_height = reduce(add, heights) / len(heights)
#
# print average_height
# print heights
