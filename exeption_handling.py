#### Exception Handling #####

""" An exception is an error that happens during execution of a program. When that
error occurs, Python generate an exception that can be handled, which avoids your
program to crash."""

## Few Examples

# if a < 3

# 1/0

# def func():
# print 'abcd'


## Few kinds of exception ##
"SyntaxError"
"IndentationError"
"ValueError"
"ZeroDivisionError"
"TypeError"
"NameError"
"IndexError"
"KeyError"
"ImportError"
"RuntimeError"

# try:
#     a =10
#     print a
# except NameError:
#     print "NameError"
#
# print "This should be executed"


### Catching specific exception ###

try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass

#
# try:
#     #a = 10/0
#     print a
# except ZeroDivisionError:
#         print "This statement is raising an exception"
# except:
#     print "Not a zero division error"
#
#
# print "I am executed due to except statement"



# randomList = ['a', 0, 2, 4]
#
# for entry in randomList:
#     try:
#         print "The entry is", entry
#         r = 1/int(entry)
#         break
#     except Exception as e:
#         print "Oops!", e
#         print "Next entry."
#         print "##" * 10
# print "The reciprocal of", entry, "is", r



# import math
# number = int(raw_input("Please enter a number: "))
#
# try:
#     print math.sqrt(number)
# except:
#     print "Bad Value for square root"
#     print "Using absolute value instead"
#     print math.sqrt(abs(number))



### Try Except Else ####

# try:
#     #a = 10/0
#     print a
# except:
#     print "everything"
# else:
#     print "Successfully Done"



#### Raising Exceptions ###

# raise KeyboardInterrupt
#
# raise MemoryError("This is an argument")


# try:
#     a = int(input("Enter a positive integer: "))
#     if a <= 0:
#         raise ValueError("That is not a positive number!")
# except ValueError as ve:
#     print ve



### Finally Block ###
""" A finally clause is always executed before leaving the try statement, whether an
exception has occurred or not. """
# try:
#     a = 10/0
#     print "Exception occurred"
# finally:
#     print "I Will be executed everytime."


#### Combining everything ###

# try:
#     x = float(raw_input("Your number: "))
#     inverse = 1.0 / x
# except ValueError:
#     print "You should have given either an int or a float"
# except ZeroDivisionError:
#     print "Infinity"
# else:
#     print "No error occured"
# finally:
#     print "There may or may not have been an exception."


# Exception
#     Except <particular exception>
#     Finally
#
# No Exception
#     try
#     else
#     finally


#### USer defined Exception ###

# # define Python user-defined exceptions
# class Error(Exception):
#    """Base class for other exceptions"""
#    pass
#
# class ValueTooSmallError(Error):
#    """Raised when the input value is too small"""
#    pass
#
# class ValueTooLargeError(Error):
#    """Raised when the input value is too large"""
#    pass
#
#
# number = 10
#
# while True:
#    try:
#        i_num = int(input("Enter a number: "))
#        if i_num < number:
#            raise ValueTooSmallError
#        elif i_num > number:
#            raise ValueTooLargeError
#        break
#    except ValueTooSmallError:
#        print "This value is too small, try again!"
#        print "##" * 10
#    except ValueTooLargeError:
#        print "This value is too large, try again!"
#        print "##" * 10
#
# print "Congratulations! You guessed it correctly."
#
