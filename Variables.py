# Variables
# Name that you create to store data inside to reuse it

print("My name is Belal")
print("Belal is learning Python")
print("Belal wants to become Python expert")

name = "Belal"                                # Variable assigning
print("My name is", name)                     # Using (,) between static part and the variable (dynamic)
print(name, "is learning Python")             # (,) adds automatic space
print(name, "wants to become Python expert")  # Python executes line-by-line (put variable assignment first)


# variables make every thing dynamic
name = "Belal" 
language = "Python"
print("My name is", name)                     
print(name, "is learning", language)             
print(name, "wants to become", language, "expert")
#-----------------------------------------------------------------------------------------------------------
# Challenge
""" 
- Print the following three lines.
- Add at least one variable to make it dynamic.
          info@datawithbaraa.com
          support@datawithbaraa.com
          www.datawithbaraa.com     
"""

# Answer
domain = "datawithbaraa.com"
print("info@"+domain)   # Using (+) instead of (,) To avoid the space added by (,)
print("support@"+domain)
print("www."+domain)