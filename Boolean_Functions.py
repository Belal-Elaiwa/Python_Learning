# Values:

print(True)
print(False)
print(type(True))

# Functions: 
"""
bool (value)

built-in function output: boolean
True  → if the value is non-empty or non-zero
False → if the value is empty or zero
"""
print(bool(123))  # True
print(bool("HI")) # True

print(bool())     # False => Empty
print(bool(0))    # False => Zero " In boolean functions 0 considered as Nothing not a value"
print(bool(None)) # False => Nothing
"""
None Isn't Empty - It's Missing!
None means no value. ''' Empty means the value exists, but empty string 
"""
#ex:
email = ""
phone = "0176-123456"
username = ""

# Allow registeration 
# If any field is filled
print(any([email, phone, username])) # True

# Allow registeration 
# Only if all field are filled
print(all([email, phone, username])) # False
#------------------------------------------------
"""
isinstance (value, type)
built-in function output: bool

checks if a value belongs to a certain data type
"""
print(isinstance(1234, int))

"""
endswith (substring) str method
output: bool

checks if the string ends with a specific word
"""
print("Hello".endswith("o"))
print("Hello".startswith("f"))