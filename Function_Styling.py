# Function Styling Guide
"""
- Goal
    We have to write functions that are easy to read and understand
- PEP8 - Style Guide
    the official Style Guide  
"""
# Bad Style
def DiscPrint(p, r):
    print("calculating discount")
    p = p - (p * r/100)
    print (p)
DiscPrint(80, 20)    

"""
Review
Function Name:
    - Use snake_case for Function Names
      Write function names in lowercase and separate words with underscores
      "load-data_from_file"
    - Use Clear Descriptive Function Names
        - Describe exactly what the function does
        - Start with a verb
        - Use full words, avoid abbreviations
Parameter Names:
    - Describe Their Values
    - Use full, meaningful words
    - Avoid abbreviations and single letters        
        "price", "country_code", "file_path"
Documentation:
    - Always describe functions using Docstring
        - Help teammates understand your code
        - Help future you remember the logic
    - Docstring
        - A short text in the first line inside a function
          that explains what the function does 
        - Why not use comments instead of docstrings?
          Comment #
          Python ignores comment, they are only notes for us (It is Lost)
          
          Docstring """"""
          Python stores it inside the function and can be reused by tools, editors ..             

          Usage
          Docstring can be used by functions, tools IDEs .. etc
          Ex: help(function_name) --> Returns also the docstring which inside the function !!
Don't Print
    - Replace Prints with Returns to send data back to the program
Don't Modify
    - Don't change parameter values directly,
      create local variable for any processing!!
Return One-Line Expressions Directly
    - Put simple calculations directly inside the return statement instead of storing them 
      in extra variables.

Use Data Type Hints
    - Always add type hints to parameters and return to make the function easier to understand
      def add(a: str) -> string:   
      NOTE "float" is only a type hint. It does not convert              
Explain Args & Return in Docstring
    - Always describe what goes in and what comes out of the function in the docstring                 
"""
# Smarter:

def calculate_discount(price: float, rate: float) -> float:
    """
    Calculate the final price after applying a discount.
    Args:
    price (float): Original Product Price.
    rate (float): Discount Rate as numbers (e.g 20 for 20%).
    Returns:
    final_price (float): Final Price after applying discount.
    """
    final_price = price - (price * rate/100)
    return final_price