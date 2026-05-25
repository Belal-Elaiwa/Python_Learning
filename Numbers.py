# Numeric data types in Python
# Int  float  complex (2 + 3j)

# Number functions
# Types

x = 5
y = 5.7
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

g = "24"
print(type(g)) # Str
print(g * 3)   # 242424 => Python dealed as a str  

"""
int (value)
built-in function output: int
converts compatible value into int value
"""

g = int(g)
print(type(g))  # int
print(g*3)      # 72
 
f = 3.14
print(int(f))   #=> Returns only 3

"""
float (value)
built-in function output: float
converts compatible value into float value
"""
x = 3
print(float(x)) #=> Returns 3.0

"""
complex (real, imag) built-in function
output: complex
creates a complex number using real and imaginary parts
"""

x = 3                 # Ral part
y = 14                # Imaginary part

print(complex(x, y))  # => Returns (3.14j)
#------------------------------------------------------------
# Math Operators
print(2 + 3)
print(5 - 3)
print(4 * 2)
print(7 / 2)

# // Floor Division output: int, It divides two numbers and rounds down
print(7 // 2)

"""
% remainder output: 0 or 1
The leftover part after division - used to check if a number is even(0) or odd(1)
"""
print(7 % 2)  # 1 (2+2+2+1)
print(10 % 2) # 0 (5+5)

"""
** exponentiation
It raises a number to the power of another number
"""
print(3 ** 2) # (3*3) = 9

"""
<operator>= Shorthand Assignment
Apply an operator and reassign the result in one step 
"""
x = 2
x = x + 3 # 5
# Or
x += 3    # 5
x -= 1
x *= 4
print(x)
#------------------------------------------------------------
# Rounding
# Measure the distance

print(2 - 10) # Outputs -8

"""
abs (value)
built-in function output: int
returns the absolute (non-negative) value of a number

useful for measuring distance or size, regardless of direction
"""
print(abs(2 - 10)) # abs for absolute => outputs 8
# ------------------------------------------------------------
# Rounding 
# Sometimes numbers are messy we round them to make the result easier to read and work with
price = 35.5498721621541
print(round(price)) #=> 36 (rounding to the nearest even number) 

# floor() is not a built-in function, floor() belongs to the math module - import it before using
# print(floor(price)) # NameError: name 'floor' is not defined. Did you mean: 'float'?

import math               # Importing module first (each time)
print(math.floor(price))  # 35 
print(math.ceil(price))   # 36

"""
round(number, ndigits)

Rounds the number to the specified number of decimal places
Handy in data analysis to clean up numbers for reports or save spaces
"""
print(round(price, 2))   # 35.55 (float)

# math.trunc(x) - cuts off the decimal part and keeps the whole number (no rounding)
print(math.trunc(price)) # 35 (No Rounding)
print(int(price))        # 35 (Converting a float to int to get rid of decimals)

# int()  VS  trunc()
"""
If you're not using math already, just use int() it's simple and built-in
If you've already imported math, use trunc() it makes your intent clearer
"""
# ceil()
# Perfect for data engineering like splitting data into pages or batches
#-------------------------------------------------------------------------------------
# Advanced Math --> Search for examples !!
#-------------------------------------------------------------------------------------
# Random Functions
"""
random ()
random function output: float
returns a random float between 0.0 and 1.0
"""

import random
print(random.random()) # Random output each time

"""
randint (start, end) random function
output: int
gets a random whole number from start to end (both included)

use it to generate test data (dummy) for like age, ID, or prices
"""
print(random.randint(1, 6))
#------------------------------------------------------------------
# Validation
"""
is integer ()
float class method output: bool
checks if a float has no decimal part (is a whole number)

Check if numbers are truly whole
floats with .O might just be from file exports
"""
x = 7.0
y = 8.6

print(x.is_integer()) # True
print(y.is_integer()) # False
#---------------------------
"""
isinstance (value, type)
built-in function output: bool
checks if a value belongs to a certain data type

Used to build a logic and conditions !!
"""
x = 50
print(isinstance(x, int))  # True
print(isinstance(x, str))  # False

# Challenge
# Generate a random integer between 1 and 100, and check if the result is an even number

# Answer
import random

x = random.randint(1, 100)
print(x)

if x % 2 == 0: 
    print("Even Number")
else: 
    print("Odd Number")