# You Must Master Functions1
"""
- What is function?
  A small reusable block of code
  that does one specific job 
"""

# Why functions ?
"""
- Easy to change
- Fast changes
- Safer (Low Risk)
- Smaller & Clean
- Easy to Read &  Understand
- Modular
- Collaboration
"""
# Sources of Functions
"""
- Built-in Functions
  Come with Python
  - Use
    print(), len(), str(), type(), ..etc

- Standard Library
  Written by Python team
  Specific & advanced
  Not expected to be used all time in our code 
  - Import first
  - Use
    math, datetime, random, ..etc

- External Library
  Written by the community, Other developers or companies
  - Install
  - Import
  - Use
    Pandas, Matplotlip, NumPy 

- User Defined Functions
  Written by you 
  Very specified
  - Define
  - Use   
"""
# How to choose between sources?
"""
Golden Role
  - Before writing a new code
    always check if it already exists
    Don't reinvent the wheel!
    - Check the built-in functions --> Easy & Safe
    - Check the libraries 
    - Check with your team --> User Defined Functions
    - Write your User Defined Functions
"""
# How function work?
"""
User Defined Functions
   - Function Definition
     Description or declaration of the function
     Syntax:
       def function_name():
          <line of code>
          <line of code>    --> The function body
          <line of code>
   - Function Call
     function_name()        --> Execution
     Only defining a function does not execute it, we have to call it
Easy to fix bugs since changes are done in one place!     
"""
print("Start")
def greet():
    print("Hello")
greet()    
print("End")    

"""
Output:
Start
Hello
End
"""
print ("Wake up")
print("Start Machine")
print ("Make Coffee")
print("Add Milk")
print("Enjoy it")
print ("Working for a while")
print ("Start Machine")
print ("Make Coffee")
print("Add Milk")
print("Enjoy it")

# Instead of repeating lines, define a function!

def make_coffee():
    print("Start Machine")
    print ("Make Coffee")
    print("Add Milk")
    print("Enjoy it")

print ("Wake up")
make_coffee()
print ("Working for a while")
make_coffee()

import math

#Built-in Function (Just Calling)
print(len("Python" ))

# Function From Libraries (Import then Call)
number = 4.2
print(math.ceil(number))

#User Defined Function (Define Then Call)
def greet():
    print("Hello")
greet()