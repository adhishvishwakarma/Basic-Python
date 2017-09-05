####### Conditional Statements ########

# If the number is positive, we print an appropriate message

# num = 3
# if num > 4:
#     print num, "is a positive number."
# print("This is always printed.")
#
# num = -1
# if num > 0:
#     print(num, "is a positive number.")
# print("This is also always printed.")

## If Else

# num = 0
# if num >= 0:
#     if num == 0:
#         print "Zero"
#     else:
#         print "Positive"
#     #print("Positive or Zero")
# else:
#     print("Negative number")

## IF Elif Else

# num = 0
# if num > 0:
#     print("Positive number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative number")

## Nested IF with input

# raw_input >> String

# num = int(raw_input("Enter a number: "))
# if num >= 0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")

## One More Example

# num = int(raw_input("Enter a number: "))
# if (num % 2) == 0:
#    print num, "is Even"
# else:
#    print num, "is Odd"


### Leap Year ####

# Should be divisible by 4 but not by 100
# but if its divisible by 100 and also 400 then its a leap year

# year = int(raw_input("Enter a year: "))
# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print year, "is a leap year"
#        else:
#            print year, "is not a leap year"
#    else:
#        print year, "is a leap year"
# else:
#     print year, "is not a leap year"


########## For Loop #######

# # Range(begin,end, step)
# # Prints out the numbers 0,1,2,3,4

#range(0,6, 2) = 0,2,4
# for x in range(5):
#     print(x)

# for <varibale> in <sequence/iterable>:
#     <condition>
# # Prints out 3,4,5
# for x in range(3, 6):
#     print(x)

# # Prints out 3,5,7
# for x in range(3, 8, 2):
#     print(x)


########### While loop ######


# # Prints out 0,1,2,3,4
# count = 0
# while count < 5:
#     print(count)
#     count += 1  # This is the same as count = count + 1

#### Break and Continue ######

# Prints out 0,1,2,3,4
# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 3:
#         break
#
# # Prints out only odd numbers - 1,3,5,7,9
# for x in range(10): # range = (0,1,2,3,4,5,6,7,8,9)
#     # Check if x is even
#     if x % 2 == 0:
#         continue
#     print(x) # XXXXXX

# Break: Which will break the loop and you are forced to come out of the loop
# Continue: Which will skip that particular loop and move to the next value
# pass: Doesn't do anything, just let the program move forward'

###### Else in loops ####

# count=0
# while(count<5):
#     print(count)
#     count +=1
# else:
#     print "count value reached", count
#
# # Prints out 1,2,3,4
# for i in range(1, 10):
#     if(i%5==0):
#         break
#     print i
# else:
#     print "this is not printed because for loop is terminated because of break but not due to fail in condition"

#####Loop with if else
# Algorithm used is varint of guess and check called exhaustive enumeration
# We enumerate all possibilities until we get to the right answer or exhaust the space of possibilities

# x = int(raw_input('Enter a integer: '))
# ans = 0
# while ans**3 < abs(x):
#
#     ans = ans + 1
#     print ans
#
# if ans**3 != abs(x):
#     print x, 'is not a perfect cube'
# else:
#     if x < 0:
#         ans = -ans
#     print 'Cube root of', x, 'is', ans
