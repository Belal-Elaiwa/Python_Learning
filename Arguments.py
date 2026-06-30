# Positional VS Keyword Arguments
# Multiple Parameters - Multiple Arguments
def clean_name(name):                # Parameter  
    cleaned = name.strip().lower()   # Local Variable             
    print(cleaned)
clean_name(" MarIA  ")

# Lets extend that!
# Send first & last name to be cleaned 
# Merge them into Fullname

def normalize(first_name, last_name):
    first = first_name.strip().lower()
    last  = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name)
normalize("Belal  ", "  ElAIWa")     # Output: belal elaiwa

# Two different ways on how to send the values to the function
"""
Keyword Arguments
    - Values pass to the function
      based on their NAMES
    - Rule
      The order of the Arguments must match the order of the Parameters 
Positional Arguments
    - Values pass to the function
      based on their ORDER

Readability: Keyword Arguments are easier to read and understand than positional    
Safety: Keyword Arguments are safer since they reduce mistakes with clear names  
Overhead: Keyword Arguments take more time to write and maintain
"""
def normalize(first_name, last_name, country):
    first = first_name.strip().lower()
    last  = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "From", country)
# Positional Argument    
normalize("Belal  ", "  ElAIWa", "Egypt") # Output: belal elaiwa From Egypt                         

# Keyword Argument
normalize(first_name = "Belal  ",last_name = "  ElAIWa", country = "Egypt") # Output: belal elaiwa From Egypt  
# -----------------------------------------------------------------------------------------------------------
"""
Positional VS Keyword 
How to choose between them?
Depending on the number of Parameters
    = 2 - 3 --> Positional Arguments
    = > 3   --> Keyword Arguments
"""
# Mixed Arguments
"""
- Rule: 
    You must start with Positional Args then Keyword
- Used for styling purpose
    to understand what is primary & secondary
- Not Recommended   

"""
normalize( "  MariA ", last_name = "SMITH  ", country = "DE")  # Output: maria smith From DE
# XXX normalize( last_name = "  MariA ", "SMITH  ", country = "DE")  
# Output: SyntaxError: positional argument follows keyword argument XXX
#-------------------------------------------------------------------------------------------
# Default Parameter
"""
- Parameter that has already a value, 
    So if you don't pass anything in 
    Python uses that value Automatically
- To be added in the definition 
- Rule ?? 

"""
def normalize(first_name, last_name, country = "N/A"): # Addition of a default value
    first = first_name.strip().lower()
    last  = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "From", country)
normalize(" BELAL   ", "eLAIWa  ")    # Output: belal elaiwa From N/A