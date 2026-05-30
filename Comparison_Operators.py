# It compares two values and return True or False based on the result
"""
== Equal To
!= Not Equal
<  Less Than
<= Less Than or Equal
>  Greater Than
>= Greater Than or Equal
"""
# Value 1 Comparison Operator Value 2
# It acts like a question and the output is True or False (Condition)

print(3 < 2)          # False

# Variable
x = 5
print(x == 5)         # True

# Expression
print(2-1 != 1)       # False

# Function
print(len("Hi") == 3) # False

print(10 == 10)
print(10 != 10)
print(7 > 3)
print(3 > 7)
print(7 <= 7)
#---------------------------------------------------------
# Chained Comparison
"""
Check multiple conditions in one line, just like in math
it evaluates it from left to right, checking each condition one by one

Chained comparisons work like SQL's BETWEEN
They check if a value is between two bounds
"""
print(1 < 4 < 6)

# ex : is age is between 18 and 30?

age = 20
print(18 <= age <= 30)

#---------------------------------------------------------

# strings can be compared too !!
# You can compare Alphabetically not just numbers 
# Python is case sensitive so, "A" & "a" are treated as different values
# Don't Mix = assigns, == compares 

# Chained Comparison
# Check multiple conditions in one line, just like in math
