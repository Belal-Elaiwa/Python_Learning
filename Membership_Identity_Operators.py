# Membership (in), (not in) Operators
# Checks if a value inside another value
# Like string, list, tuple, or other sequences
# Returns Boolean True or False 

print("e" in "Belal")     # Returns True
print("b" in "Belal")     # Returns False 
print("f" in "Belal")     # Returns False
print("f" not in "Belal") # Returns True
print(3 in [1, 2, 3, 4])  # Returns True
print(4 in {1, 2, 3, 4})  # Returns True

# Task 
# Validate that the domain is not in the banned list
# Security check: Ensure the domain is not banned

domain = "gmail.com"
banned_domains = ["spam.com", "fake.net", "bot.org"]
print(domain not in banned_domains)  # Returns True
#---------------------------------------------------
# Identity (is) (is not) Operators
# checks if two variables are refering to the same object in the memory

x = ["a", "b", "c"]
y = ["a", "b", "c"]

print(x == y) # Returns True  ( '==' Compares the values )
print(x is y) # Returns False ( 'is' Compares the identity (IDs) of each object)

x = 10
y = 10
print(x == y) # Returns True
print(x is y) # Returns True  (simple value no need for python to assign different IDs)

print("=" *100)
# Task 
# Validate the email address it must be filled in and not empty
# Make sure the email exists, and it's not empty

email = None
print(email != None and email != "")

# Use is instead of == or != when checking for None
print(email is None and email != "")
print(email is not None and email != "")