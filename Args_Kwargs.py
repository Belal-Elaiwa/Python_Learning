"""
- Sometimes you don't know how many arguments
  will be passed to your function!
- There are two tools in Python:
  Both allow function to accept unknown number of arguments
  - *args    --> * Positional Arguments
     Used when you pass similar types values!
       like (1, 2, 3,4) or ("Alex", "Kumar", "Nora")
     Data type --> Tuple
     Works only with Positional arguments --> Only values
     
  - **kwargs --> ** Keyword arguments 
     Used when you pass Different types values!
       Like (Alex, 25, alex@gmail.com, 10.11.2024)
     Data type --> Dict
     Works only with keyword arguments    --> Names & Values 
"""
# Calc the total of values
def total(a, b):
    print( a + b)
total(1, 2)       # Output: 3

def total (a=0, b=0, c=0, d=0):
    print(a + b+ c + d)
total (1, 2)
total (1, 2, 3)
total (1, 2, 3, 4)
# Instead of this, Use *args Or **kwargs

# Python put the values inside a tuple!
def total(*args):
    print(type(args))
total (1, 2, 3, 4)    # Output: <class 'tuple'>

# So, we can use any function or method that works with tuple!
def total(*args):
    print(sum(args))
total (1, 2, 3, 4)             # Output: 10
total(1, 2, 3, 3, 4, 5, 6, 7)  # Output: 31

# Create the user profile
def create_user(**kwargs):
    print(type(kwargs))        
    print(kwargs)
create_user(first_name="Mo", 
            Last_name= "Salah",
            age=33, 
            country="Egypt")
"""
Output:
<class 'dict'>
{'first_name': 'Mo', 'Last_name': 'Salah', 'age': 33, 'country': 'Egypt'}
"""
create_user(name = "Ronaldo", country = "Portugal")
# Output: {'name': 'Ronaldo', 'country': 'Portugal'}