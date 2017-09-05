##### Data Structures in python ###########

# Types of Objects:
# Scalar and Non Scalar
# Scalar: Which do not have accessible internal structure
# Non Scalar: strings, tuple, lists, dictionaries

####### More about Strings #######

# A string is a sequence of characters.
# A character is simply a symbol to represent the smallest possible break on the text.
# For example, the English language has 26 characters.
# In Python, string is a sequence of Unicode character
# Computers do not deal with characters, they deal with numbers (binary).
# Even though you may see characters on your screen,
# internally it is stored and manipulated as a combination of 0's and 1's.
# This conversion of character to a number is called encoding, and the reverse process is decoding.
# ASCII and Unicode are some of the popular encoding used.

# Example of how to create string in python
# my_string = 'Hello'
# print(my_string)
#
# my_string = "Hello"
# print(my_string)
#
# my_string = '''Hello'''
# print(my_string)
#
# # triple quotes string can extend multiple lines
# my_string = """Hello, welcome to
#            the world of Python"""
# print(my_string)

## How to access characters inside a string

# "Indexing"

#  P  y  t  h  o  n
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1

# string = "Python"
# print string[2]

# str = 'Python'
# print 'str = ', str
#
# # first character
# print 'First Character in str is ', str[0]
#
# # last character
# print'last character in str is ', str[-1]
#
# # 3rd character
# print'Third character in str ', str[2]

# # Error if out of index
# print str[10]
#
# # index must be an integer
# print str[1.5]


### Slicing ###

# str = 'Python'
# #slicing 2nd to 5th character
# print 'str[1:5] = ', str[1:5]
#
# print str[1:]
#
# print str[:]
# print str

# print str[:-3]
#
# print str[-3:]

# some_str = "Hello world!"
# print some_str[3:7:2]

# reversing a string
# str = 'Python'
# print 'reversed = ', str[::-1]
#
# str1 = 'Hello World!'
#
# print "Updated String : ", str1[:6] + 'Python'


### "String Operations"

# str = "Hello world!"
#print str.index("a")
#print str.find("a")
# print "single quotes are ' '"
#
# print len(str)

# # # How to find the index of some character in string
# print str.index("o")
#
# print str.find("y")
#
# print str.count("l")

# print str.upper()
#
# print str.lower()
#
# print str.startswith("Hello")
#
# print str.endswith("d!")
#
# print str
# print str.split("o")

### String Formatting

# # % operator
# text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')
# print text

# number1 = int(raw_input("Enter a number: "))
# number2 = int(raw_input("Enter another number: "))
# add = number1 + number2
#
# print "The sum of %s and %s is %s" % (number1, number2, add)

# add parenthesis to make the long-line work:
# text2 = ("%d little pigs come out or I'll %s and %s and %s" %
# (3, 'huff', 'puff', 'blow down'))
# print text2


######### Tuples #######
# Like strings, tuples are immutable ordered sequences of elements. The difference is that the elements
# of a tuple need not be characters. The individual elements can be of any type, and need not be of the
# same type as each other.

# A tuple is created by placing all the items (elements) inside a parentheses (), separated by comma.

# # empty tuple
# # Output: ()
# my_tuple = ()
# print my_tuple
#
# # tuple having integers
# # Output: (1, 2, 3)
# my_tuple = (1, 2, 3)
# print my_tuple
#
# tuple with mixed datatypes
# Output: (1, "Hello", 3.4)
# my_tuple = (1, "Hello", 3.4)
# print my_tuple
# #
# # nested tuple
# # Output: ("apple", (5, 9, 6), (1, 2, 3))
# my_tuple = ("apple", (5, 9, 6), (1, 2, 3))
# #print my_tuple

#
# tuple can be created without parentheses
# also called tuple packing
# Output: 3, 4.6, "dog"

## Tuple Unpacking
# a, b = 1, 2
#
# my_tuple = 3, 4.6, "dog"
# print my_tuple
# print type(my_tuple)
# #
# # # tuple unpacking is also possible
# # # Output:
# # # 3
# # # 4.6
# # # dog
# a, b, c = my_tuple
# print a
# print b
# print c

# # only parentheses is not enough
# # Output: <class 'str'>
# my_tuple = ("hello")
# print type(my_tuple)
#
# # need a comma at the end
# # Output: <class 'tuple'>
# my_tuple = ("hello",)
# print type(my_tuple)
# #
# # parentheses is optional
# # Output: <class 'tuple'>
# my_tuple = "hello",
# print type(my_tuple)

### Indexing in tuple
#
# my_tuple = ("apple", (5, 9, 6), (1, 2, 3))
#
# print my_tuple[0]
# print my_tuple[1]
# print my_tuple[2]
# ## nested value
# # Output: 6
# print my_tuple[1][2]

## Slicing tuple, same as string

# tup = (1, 2, 3, 4, 5, 6, 7 )
# print "tup[1:5]: ", tup[1:5]
# # reverse
# print tup[::-1]

## Updating Tuples
# Tuples are immutable which means you cannot update or change the values of tuple elements.
# You are able to take portions of existing tuples to create new tuples

# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
# print id(tup1)
# print id(tup2)
# # Following action is not valid for tuples
# # tup1[0] = 100;
# #
# # # So let's create a new tuple as follows
# tup3 = tup1 + tup2
# print tup3
# print id(tup3)


##Concatenation, same as string using + operator
# print (1, 2, 3) + (4, 5, 6)

## Deleting tuple

# my_tuple = (1, 2, 3)
# del my_tuple
# print my_tuple

## Tuple Functions

# my_tuple = ('a','p','p','l','e',)
#
# # Count
# # Output: 2
# print my_tuple.count('p')
#
# # Index
# # Output: 3
# print my_tuple.index('l')
#
# # Few More functions : len(), max(), min(), sorted(), sum(), tuple()


## Membership checking

# my_tuple = ('a','p','p','l','e',)
# # In operation
# # Output: True
# print('a' in my_tuple)
#
# # Output: False
# print('b' in my_tuple)
#
# # Not in operation
# # Output: True
# print('g' not in my_tuple)

## Iteration on Tuple
# tup = (1, 2, 3, 4, 5, 6, 7)
# for element in tup:
#      print element



######### LISTS ########
"""
Like a tuple, a list is an ordered sequence of values, where each value is
identified by an index. The syntax for expressing literals of type list is
similar to that used for tuples; the difference is that we use square
brackets rather than parentheses. The empty list is written as [], and
singleton lists are written without that (oh so easy to forget) comma
before the closing bracket. The list is a most versatile datatype available
in Python.
"""

# # empty list
# my_list = []
# print my_list
# #
# # list of integers
# my_list = [1, 2, 3]
# print my_list
# #
# # # list with mixed datatypes
# my_list = [1, "Hello", 3.4]
# print my_list


## Accessing values inside list and slicing

# list1 = ['physics', 'chemistry', 1997, 2000];
# list2 = [1, 2, 3, 4, 5, 6, 7 ];
#
# print "list1[0]: ", list1[0]
# print "list2[1:5]: ", list2[1:5]

# nested list
# my_list = ["Happy", [2,0,1,5]]
#
# #print my_list[0][1]
# # print my_list[0][1]
# #
# print my_list[1][2]


## Updating Elements inside list
## Since the list is mutable, we can update or add elements inside lists

# list = ['a', 'b', 1, 2];
#
# print list
# print id(list)
#
# list[1] = ('x', 'y');
# print list
# print id(list)
#
# del list[1]
# print list
# print id(list)


### LIST functions
# l.append(e) # adds the object e to the end of l
# l.count(e)  # returns the number of times that e occurs in l
# l.insert(i, e) # inserts the object e into l at index i
# l.extend(l1) # adds the items in the list l1 to the end of l
# l.remove(e) # deletes the first occurrence of e from l
# l.index(e) # returns the index of first occurrence of e in l
# l.pop(i) # removes and returns the item at index i in l, if i is omitted it defaults to -1
# l.sort() # sorts the elements in ascending order
# l.reverse() # reverses the order of the elements in l


## Adding to list

# lst = [1, 3, 5]
#
# lst.append(7)
#
# # Output: [1, 3, 5, 7]
# print lst
# #
# lst.extend([9, 11, 13])
#
# # Output: [1, 3, 5, 7, 9, 11, 13]
# print lst
# 

# # Output: [1, 3, 5, 9, 7, 5]
# print lst + [9, 7, 5]
# 
# #Output: ["re", "re", "re"]
# print ["re"] * 3 # ['re'] + ['re'] + ['re']


# lst = [1, 9]
# lst.insert(1, 'Some_string')
# lst.append('another_string')
#
# # Output: [1, 3, 9]
# print lst
#
# lst[2:2] = [5, 7]
#
# # Output: [1, 3, 5, 7, 9]
# print lst


## Removing from list

# my_list = ['p','r','o','b','l','e','m']
# my_list.remove('p')
#
# # Output: ['r', 'o', 'b', 'l', 'e', 'm']
# print my_list
# #
# # Output: 'o'
# print my_list.pop(1)
# #
# print my_list
# # # Output: ['r', 'b', 'l', 'e', 'm']
# # print my_list
# #
# # # Output: 'm'
# print my_list.pop() ## default index = -1
# #
# # Output: ['r', 'b', 'l', 'e']
# print my_list
# #
'''
my_list.clear()

# Output: []
print my_list
'''


## Other functions

# my_list = [3, 8, 1, 6, 0, 8, 4]
#
# # Output: 1
# print my_list.index(8)
#
# # Output: 2
# print my_list.count(8)
#
# my_list.sort()
#
# # Output: [0, 1, 3, 4, 6, 8, 8]
# print my_list
#
# my_list.reverse()
#
# # Output: [8, 8, 6, 4, 3, 1, 0]
# print my_list


#### List Comprehension ####

# sqr = [2 ** x for x in range(10)]
#
# # Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
# print(sqr)

# sqr = []
# for x in range(10):
#     sqr.append(2**x)
# print sqr

# odd = [x for x in range(20) if x % 2 == 1]
# print odd
#
# odd = []
# for x in range(20):
#     if x%2 == 1:
#         odd.append(x)
# print odd
#
# program = [x+y for x in ['Python ','C '] for y in ['Language','Programming'] if y == 'Language']
# print program
#
# program = []
# for x in ['Python ','C ']:
#     for y in ['Language', 'Programming']:
#         if y == 'Language':
#             program.append(x+y)
# print program

# x = 'Python'
# y = 'Language'
# x + y = 'Python Language'
#
# x = 'Python'
# y = 'Programming'
# x + y = 'Python Programming'
#
# x = 'C'
# y = 'Language'
# x + y = 'C Language'
#
# x = 'C'
# y = 'Programming'
# x+ y = 'C Programming'


#### Iterating through list

# for fruit in ['apple','banana','mango']:
#     print("I like",fruit)


#### Advance Lists ####
"""Assignment with an = on lists does not make a copy. 
Instead, assignment makes the two variables point to the one list in memory."""

# colors = ['red', 'blue', 'green']
#
# b = colors # ['red', 'blue', 'green']
#
# print b # ['red', 'blue', 'green']
#
# b.append('add') # ['red', 'blue', 'green', 'add']
#
# print colors # ['red', 'blue', 'green']
# print id(b)
# print id(colors)

### Create a new list from the existing list

# oldList = ['red', 'blue', 'green']
# # newList = oldList[:]   ## slicing and creating new list
# # newList = list(oldList) ## by list methid
# newList = copy.deepcopy(oldList) # deepcopy method
# print oldList
# print newList
#
# newList.append('yellow')
#
# print oldList
# print newList
# print id(oldList)
# print id(newList)

#### Convert list to string ###

# listOfStrings = ['One', 'Two', 'Three']
# strOfStrings = ''.join(listOfStrings)
# print type(listOfStrings)
# print strOfStrings
# print type(strOfStrings)

# List Of Integers to a String
# listOfNumbers = [1, 2, 3]
# strOfNumbers = ''.join(str(n) for n in listOfNumbers)
# print strOfNumbers
# print type(strOfNumbers)



##### Dictionaries ############
""" A Dictionary (or "dict") is a way to store data 
just like a list, but instead of using only numbers to get the data, 
you can use almost anything. This lets you treat a dict like 
it's a database for storing and organizing data."""

# An empty dictionary without any items is written with just two curly braces,
# like this: {}

# Ordering: Undefined

# Contains key value pair
# Keys are unique within a dictionary while values may not be.
# The values of a dictionary can be of any type, but the keys must be of an
# immutable data type such as strings, numbers, or tuples.

## Why Dictionary: we can determine if a specific key is present in the dictionary
# without needing to examine every element (which gets slower as the dictionary gets bigger).
# The Python interpreter can just go to the location key "should be"
# at (if it's in the dictionary) and see if key is actually there.

## When to Use It: If you use a word match, chances are you need dictionary


### Creating a dictionary

#{'key': [1,2,3,4], 'key2': (1,2,3,4)}

# my_dict = {1: 'apple', 2: 'ball'}
# print my_dict
#
# my_dict = {'name': 'John', 1: [2, 4, 3]}
# print my_dict
# #
#
# my_dict = dict(one=2, three=4)
# # {'one': 2, 'three': 4}
# print my_dict
#
# another_dict = dict([(1, 2), (3, 4)])
# print  another_dict


####### Accessing values in dictionary

# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#
# print "dict['Name']: ", dict['Name']
# print "dict['Age']: ", dict['Age']


# dict['Age'] = 8; # update existing entry
# dict['new_key'] = 'new_value'
# dict['School'] = "DPS School"; # Add new entry
#
# print dict


## Deleting Dictionaries
#
# dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# #
# # del dict1['Name']; # remove entry with key 'Name'
# # print dict1
# # dict1.clear();     # remove all entries in dict
# # print dict1
# # del dict1;        # delete entire dictionary
# # print dict1
#
# print "dict['Age']: ", dict1['Age']
# print "dict['School']: ", dict1['School']

## Updating

# first = {'a': 1}
# second = {'b': 2}
# first.update(second)
# print first
# # {'a': 1, 'b': 2}
# print second
# # {'b': 2}

# d = {1: 'a', 2: 'b', 3: 'c'}
# copied_dict = d.copy()
# print copied_dict # {1: 'a', 2: 'b', 3: 'c'}
# print id(d)
# print id(copied_dict)

# print {1: 'a', 2: 'b', 3: 'c'}.get(3)

### Removing

# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}

# # remove a particular item
# # Output: 16
# print(squares.pop(4))
#
# # Output: {1: 1, 2: 4, 3: 9, 5: 25}
# print(squares)

# # remove an arbitrary item
# # Output: (1, 1)
# print(squares.popitem())
#
# # Output: {2: 4, 3: 9, 5: 25}
# print(squares)
#
# delete a particular item
# del squares[5]
#
# # Output: {2: 4, 3: 9}
# print(squares)

# # remove all items
# squares.clear()
#
# # Output: {}
# print(squares)

# # delete the dictionary itself
# del squares
#
# #Throws Error
# print(squares)


### Iterating on dictionary

## By default, iterating over a dict iterates over its keys.
## Note that the keys are in a random order.


dict = {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

# for key in dict:
#     print dict[key]
# # prints a g o
#
# ## Exactly the same as above
# for key in dict.keys():
#     print key
#
#
# ## Get the .keys() list:
# print dict.keys()  ## ['a', 'o', 'g']
#
# ## Likewise, there's a .values() list of values
# print dict.values()  ## ['alpha', 'omega', 'gamma']

# ## Common case -- loop over the keys in sorted order,
# ## accessing each key/value


# for key in sorted(dict.keys()): # ['a', 'g', 'o']
#     print key, dict[key]

# ## .items() is the dict expressed as (key, value) tuples
# print dict.items()  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]
# #
# ## This loop syntax accesses the whole dict by looping
# ## over the .items() tuple list, accessing one (key, value)
# ## pair on each iteration.
# for key, value in dict.items():
#     print key, '>', value
# ## a > alpha    o > omega     g > gamma



### Dictionary Comprehension

# squares = {x: x*x for x in range(6)}
#
# squares = {}
# for x in range(6):
#     squares[x] = x*x
#
# print squares
#
# # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# print(squares)

# squares = {}
# for x in range(6):
#    squares[x] = x*x






 #########  Data Structures Questions ########


""" 1. Print index and value of the list """

my_list = [ 'a', 'b', 'c', 'd' ]

### expected output

# 0 a
# 1 b
# 2 c
# 3 d

# Hint: range(len(z))

# index = 0
# while index < len(my_list):
#     print index, my_list[index]
#     index += 1  # index = index + 1
#
# for index in range(len(my_list)):
#     print index, my_list[index]
#
# ## enumerate
#
# for index, value in enumerate(my_list):  # [(0, 'a'), (1, 'b'), ...]
#     print index, value


""" 2. key value pair interchange in dictionary """

my_dict = {'a': 1, 'b': 2}
#print my_dict['a']

### expected output { 1: 'a', 2: 'b' }

# inv_dict = {}
# for key in my_dict:
#     inv_dict[my_dict[key]] = key  # appending to the new dict
# print inv_dict
#new_dict[key] =value
#
# print {value: key for key, value in my_dict.items()}
#
# print {value: key for key, value in my_dict.iteritems()}


""" 3. Remove all whitespaces """

string = 'a   b c   d e'

### expected output : abcde

# Hint: Join and Split functions

# lst = string.split()
# print ''.join(lst)
#
# ''.join(string.split())

""" 4. number triangle printing """

## Expected Output:

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6


# n = int(raw_input("Please enter a number: "))
#
# for i in range(n + 1):
#     print (str(i) + ' ') * i



""" 5. Great Pyramid of #, max line should be 2n - 1 """

## Expected Output:

    #
   ###
  #####
 #######
#########

# n = int(raw_input("Please enter a number: "))
# n = 5
#
# for i in range(n+1):
#     row = ' ' * (n-i)
#     row += '#' * (2*i -1)
#     print row


""" 6. print only vowels from a given word using list comprehension """

# word = 'MATHEMATICS'

## Expected Output: ['A', 'E', 'A', 'I']

# print [ x for x in word if x in 'AEIOUaeiou']
#
# print [x for x in word if x in ['A', 'E', 'I', 'O', 'U']]




#### Solutions ####

# i = 0
# while i < len(z):
#    print i, z[i]
#    i += 1
#
#
# for i in range(0, len(z)):
#    print i, z[i]
#
#
# for i, item in enumerate(z):
#    print i, item
#
#
# # 2
#
# inv_dict = {};
# for i in my_dict:
#     inv_dict[my_dict[i]]=i
# print inv_dict
#
# inv_dict = {value: key for key, value in my_dict.items()}
# print inv_dict
#
# inv_dict = {value: key for key, value in my_dict.iteritems()}
# print inv_dict
#
#
# # 3
#
# print "".join(string.split())
#
# # 4
#
#
# for i in range(7):
#     print (str(i) + " ")*i
#
#
# # 5
#
# n = int(raw_input("Please enter a number: "))
# for i in range(0,n+1):
#     s = ' ' * (n-i)
#     s += '#'*(i*2-1)
#     print s
#
# # 6
#
# print [x for x in word if x in ['A','E','I','O','U']]