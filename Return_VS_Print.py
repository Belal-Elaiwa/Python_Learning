# Transformation Function
"""
- Raw Data 
- Input 
- Data Transformation
- Processed Data 
- Output
- Return 
"""
"""
== Print
    - We are just printing the output of the function !
      Printing is something for Us (Human!), To display it on the screen

== Return  
    - Programs don't work with the printed Outputs!
      They need the function to return the values back to it internally  
    - If you want the result of your function to be
      reused later in the program
"""

"""
Syntax:
def function_name(Parameter):
    <Line of Code>
    <Line of Code>
    return <expression>   --> Could be value, local variable, parameter, calc, function, ...etc

    # Function call
function_name(Argument)    
    """

f = 2
def multi_factor(x):
    y = x * f
    print(y)
multi_factor(3)    # Output: 6

"""
z= y + f
print(z)           # Output: NameError: name 'y' is not defined XXX """

# Using Return!!
f = 2
def multi_factor(x):
    y = x * f
    return(y)
z = multi_factor(10)
print(z)          # Output: 20

# Returned from the function and assigned as a global variable to be used anywhere
# Inside & Outside the function !!
print(f + z)      # Output: 22

"""
- What will happen if you didn't assign a return ?!!!
    - If a function has no return statement, Python returns None
- Assign the function call to a variable to store the result
- A function can have multiple return statements
- You can return multiple values separated by commas
"""

def clean_name(name):                # Parameter  
    cleaned = name.strip().lower()   # Local Variable             
    return cleaned
clnd_name = clean_name(" MarIA  ")
print(clnd_name)                     # Global Variable 

# Without return
def clean_name(name):
    cleaned = name.strip().lower()
clnd_name = clean_name(" MarIA  ")
print(clnd_name)                     # Output: None

# Multiple return
# Extend the logic: If the value is empty, convert it to None, Otherwiose, Clean It

def clean_name(name): 
    if not name:
        return None
    else:          
        cleaned = name.strip().lower()            
        return cleaned
clnd_name = clean_name("")
print(clnd_name)                     # Output: None    

def clean_name(name): 
    if not name:
        return None
    else:          
        cleaned = name.strip().lower()            
        return cleaned
clnd_name = clean_name("  mArIA ")
print(clnd_name)                     # Output: maria 

# Return Multiple Values!
# Extend Logic: Return the value in both upper & lower case

def clean_name(name):
    lo_cleaned = name.strip().lower()  
    up_cleaned = lo_cleaned.upper()   
    return lo_cleaned, up_cleaned
clnd_name = clean_name(" MarIA  ")
print(clnd_name)                     # Output: ('maria', 'MARIA') --> Tuple

# To get rid of tuple !
def clean_name(name):
    lo_cleaned = name.strip().lower()  
    up_cleaned = lo_cleaned.upper()   
    return lo_cleaned, up_cleaned
lo_clnd, up_clnd = clean_name(" MarIA  ")
print(lo_clnd) 
print(up_clnd)

"""
Output:
maria
MARIA
"""