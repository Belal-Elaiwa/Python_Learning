# How Data Flows Through Functions?
"""
Function shapes:
Functions work differently
Different shapes means different data flow
  - No Input and No Output
  - Only Input
  - Input and Output
  - Multiple-Input and Multiple-Output
The inputted data called Parameter & Argument
The outputted data called Return
"""

# Parameters VS Arguments
"""
Parameters
    - Names used in function definition 
      that describes what data the function expects 
    - Placeholder
    - Define what function expects
Arguments
    - Actual values passed in function call
      that are assigned to parameters
    - Value that fills placeholder!
    - Provides function with values

Syntax:
       def function_name(Parameter):
          <line of code>
          <line of code>    --> The function body
          <line of code>
   - Function Call
     function_name(Argument)        --> Execution

When the function is defined the parameter will be empty 
acting as a placeholder, until you fill it with a value through the argument!           
"""
#  Task: Define a function that multiplies any value by 2

def multiple_two(x):   # --> Our parameter is X --> Empty, Placeholder!
    print(x*2)
multiple_two(3)        # --> Our argument is a VALUE to fill the Parameter!
# Output: 6
# After Execution --> The parameter will be empty again

# Rule: Normalize Strings
# Remove extra spaces and make text lowercase
name = "  MariA "
print(name.strip().lower())   # Output: maria

# Instead of repeating this, define a function!
def clean_name():
    name = "  MariA "
    print(name.strip().lower())
clean_name()          # Output: maria
clean_name()          # Output: maria
clean_name()          # Output: maria

"""
HardCoded value issue!
It is not reusable it always cleans the same value
Pass Data in
Pass the values as a parameter to handle any input
"""
def clean_name(name):
    print(name.strip().lower())
clean_name(" MarIA  ")           # Output: maria
clean_name(" BELAL   ")          # Output: belal
clean_name("JoHn     ")          # Output: john
clean_name()                     # Output: TypeError: clean_name() missing 1 required positional argument: 'name'
# Works with any Value
# Values change but logic stays the same
# At least one Argument even empty one !! --> clean_name("")  