# Parameters VS Global Variables VS Local Variables
# How long does it live?
# Where is it accessible?

"""
Global Variable
    - It is created outside the function
    - Can be accessed anywhere

Local Variable
    - It is created inside the function
    - Can be accessed only inside the function   
Parameters
    - It is created inside the function    
    - Can be accessed only inside the function   
"""
#---------------------------------------------
# How long does it live?
"""
Global Variable
    - Program Start
    - Function Start
    - Function End
    - Program End
Parameters
    - Function Start
    - Function End
Local Variable
    - Function Start
    - Function End
"""

f = 2                     # --> Global Variable f
def multiple_factor(x):   # --> Parameter x
    y = f * x             # --> Local Variable y
    print(y)
multiple_factor(10)       # --> Argument 10
"""
How does this work?
[1]- Python assigning the global variable f=2 
[2]- then create a parameter x --> empty 
[3]- Python know nothing about the body of the function or local variable until execution
[4]- While calling the function
     Python fills the Parameter with the Argument value and the f from the Global Variable
     then create the local variable y 
[5]- print(y)
[6]- Parameter emptied again waiting for the new value from the Argument!  
[7]- Python destroys the whole local variable y 
"""
"""
Raw vs Processed Data?
Parameter: keeps the raw value to be reused 
Local variable: holds the processed version

Global Variable: Controls behavior without changing the function
"""

def clean_name(name):                # Parameter  
    cleaned = name.strip().lower()   # Local Variable
    print("Raw:", name)              
    print("Cleaned:", cleaned)
clean_name(" MarIA  ")

""" 
Output:
Raw:  MarIA  
Cleaned: maria
 """
# Scope: Parameters and local variables only accessed inside the function
# XXX print("Raw:", name)         # Output: NameError: name 'name' is not defined      
# XXX print("Cleaned:", cleaned)  # Output: NameError: name 'cleaned' is not defined

# Logic creation Using a Global Variable
# Global Variable --> Global Access across the entire script

case_rule = "lower"               # Global Variable
def clean_name(name):
    cleaned = name.strip()        # Local Variable
    if case_rule == "lower":
        cleaned = cleaned.lower()
    print("Cleaned:", cleaned)
clean_name("  MaRiA ")            # Output: Cleaned: maria