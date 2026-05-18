# Types of Functions:
# [1] - Built-in functions (print(), input(), len(), ...etc)
# [2] - Third-Party libraries (Pandas, Numby, Pyspark, ....etc )
# [3] - User Defined functions

# print function (Built-in function)

# Using single or double quotes
print("Hello Python")
print('Hello Python') 

# Styling the Output
print("-------------------")
print("   Helllo Python   ")
print("-------------------")

#---------------------------------------------------------------
# Escape Sequence 
# Using Back-slash \ to escape from the default sequence !

print("Hello \"Python\"") # \" => To skip " & include it as a part of the string
print('Hello "Python"')   # Different quotes will be included as a part of the string

# print("Path: C:\Users\Belal")  --> Error 
print("Path: C:\\Users\\Belal") #--> Using \\ to include the real \ in the message 

# How to put a blank between 2 lines?
print("Message1")
print()
print("Message2")

print("Message3\n") # Using \n to add an empty line
print("Message4")

print("Message5\n\n\n") # 3 empty lines
print("Message6")

# Putting all together
print("Message7\nMessage8")    # New line without blank
print("Message9\n\nMessage10") # New line and blank

print("Message1\tMessage2")    # Putting horizontal tab between messages (Space)
#-------------------------------------------------------------------------------
# Challenge
"""  Use PRINT() to recreate this exact output
     You are allowed to use only one PRINT()
  Your Learning Path:
    - Python Basics
    - Data Engineering
    - AI
"""
# Answer:
print("Your Learning Path:\n\t- Python Basics\n\t- Data Engineering\n\t- AI ")

# Using triple quotes for multiple lines (No need for \n!)
print("""Your Learning Path:
\t- Python Basics
\t- Data Engineering
\t- AI """)
#-----------------------------------------------------------------------------