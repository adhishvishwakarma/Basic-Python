def add(a, b):
   """This program adds two
   numbers and return the result"""
   result = a + b
   return result



def hello():
    print "i am from module.py"


if __name__ == "__main__":
    print "Executing as main program"
    print "Value of __name__ is: ", __name__
    hello()
