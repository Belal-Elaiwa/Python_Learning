# Data Types
#------------------------------------------------------
# Python needs to understand how to treat your values!
# Python automatically detects the type of Data
# Dynamic : Data type can change at anytime

# Why Data Types ?
# To prevent doing something wrong
# To know how to operate Data

# Data Categories and Types:
#---------------------------------------------------

""" 
No value
      - None      = None
                    - means "no value", "nothing" or "unknown"
                    - it's used to show the absence of any data
      """

""" 
Single Value
      - Integer   = int integer: whole numbers without decimals
      - Float     = float numbers with decimal points 
      - String    = str
                     - string: represent text or a sequence of characters
                     - written inside single or double quotes                          
      - Boolean   = bool
                     - boolean: can be either True or False
                     - used to handle logic and decision-making                                 
      """

""" 
Multiple Values:
      - List
      - Set
      - Tuple
      - Dict 
      """


a = 10      # int
b = 3.15    # float
c = "Hello" # str
d = 'Hi'    # str
e = "1234"  # str
f = True    # bool Must start with upper case no Quotes
g = False   # bool Must start with upper case no Quotes
h = None    # Nothing
i = ""      # Blank "" is a string value with no characters inside, it is not same as None!
j = " "     # White Space " " is a string value with 1 or more spaces, it is not same as None!
#---------------------------------------------------------------------------------------------

""" Data Types, Functions, Methods
-There are specific tools for specific data types
-Inorder to do something to data we needfunctions
- Functions :
     = Standard Library      (Built-in)
     = Third-Party Libraries (Pandas, Numpy, ..etc)
     = User Defined
-----------------------------------------------------------------------------------------------     
-Standard Library :
     = Built-in Module:
        - Standalone functions       : print(), type(), ...etc
        - Methods of Class           : a Class for each data type 
                                       upper(), replace() --> class str
                                       to-byte()          --> class int
        - Operations (Magic Methods) : + / > < == in or
     
     = Math Module ( import):
        - Functions: abs(), round(), floor, .. etc   
"""
#-----------------------------------------------------------------------------------------------

text = "Hi"
number = 10

print(text)
print(number)

# type() => Built-in Function that returns the data type of a value, so you know what kind of object it is.
print(type(text)) 
print(type(number))

# len () => Built-in Function that gives the total count of items inside a value, helping you measure its length.
print(len(text))
# print(len(number)) => TypeError: object of type 'int' has no len()
 
# Methods
print(text.upper())
# print(number.upper()) => AttributeError: 'int' object has no attribute 'upper'

# bit length () => Method of ‹class int> returns the length of a number in binary.
print(number.bit_length()) #--> returns 4 which means wen need 4 bits inorder to store this value
# print(text.bit_length()) => AttributeError: 'str' object has no attribute 'bit_length'
#-----------------------------------------------------------------------------------------------

"""
Challenge:
Create 5 variables - each with a different data type:
1. Your age
2. Your height (with decimals)
3. Your name
4. Are you a student?
5. Something with no value yet
Then print the values, data types, lengths of all vairables 
"""

# Answer:

age = 35
height = 176.5
name = "Belal"
q = input("Are you a student ?")
x = None

# print the values
print(age)
print(height)
print(name)
print("Are you a student?", q)
print(x)

# data types
print(type(age))
print(type(height))
print(type(name))
print(type(q))
print(type(x))

# lengths
print(age.bit_length())
print(len(name))      
