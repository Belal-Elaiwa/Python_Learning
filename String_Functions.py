# String Functions
"""
:Types 
  type (value)
  built-in function output: type
  returns the data type of a value, so you know what kind of object it is
"""
name = "Belal"
print(type(name))           # <class 'str'>

age = 35
print(type(age))            # <class 'int'>
# print("Your age is" + age)  # Can't combine a string with an integer using + operator

"""
str (value)
built-in function output: string
conversts any value into string value
"""
print("Your age is " + str(age)) 

"""
Python is flexible with data types - but watch out!
You can change a value's type, but Python will treat it differently
"""
#--------------------------------------------------------------------
# Math
"""
len (value)
built-in function output: int
returns the number of items in a value returns the number of characters in a string
it counts everything even spaces

Use Case - Check Password Quality
make sure the password meets minimum length requirements

Use Case - Validate Input Length
Prevent values that are too short or too long
"""
password ="123a"
print(len(password))
#-----------------------------------------------
"""
count (substring)
str method output: int  
syntax:
Value.count("value that need to be counted")

Python is case-sensitive,
means uppercase and lowercase letters are treated as different
returns how often a word appears in the string
"""

text = """
Python is easy to learn.
Python is powerful.
Many people love python.
"""
"""
Use Case - Word Frequency Check
Counts how many times a specific word appear

Use Case - detect quality issues
count how many unwanted characters in my data
"""
print(text.count("Python")) 
#-----------------------------------------------------------------
# Data Transformations
"""
[1]- replace()
replace (old, new) str method
Syntax:
print(Value.replace("old character", "new character"))
print(Value.replace("old character", "new character").replace("2nd old character", "2nd new character"))
output: string
swaps part of the text with something new

Use Case - Clean Numeric Formats
replace commas with dots in European-style decimal numbers
"""

price = "1234,56"
print(price.replace(",","."))

"""
Use Case - Change Phone Number Format replace special characters with something else
"""
phone = "176-1234-56"
print(phone.replace("-","/"))

"""
replace() is not just for changing values you can also remove unwanted parts by replacing them with an empty string ("")
could be used for removing a character

Use Case - Clean Phone Numbers remove special characters from phone numbers
"""
print(phone.replace("-", ""))

# How to relplace multiple characters at once ?
# Chained methods are executed in order from left to right.
# Each replace()) runs on the result of the one before it.

price = "$1,266.59"
print(price.replace("$", "").replace(",",""))

"""
Challenge :
Convert the messy phone number into a clean number format with only digits
"+49 (176) 123-4567"
"""

#Answer:

phone = "+49 (176) 123-4567"
print(phone.replace("+", "00") .replace(" ", "") .replace("(","") .replace(")","") .replace("-",""))
#---------------------------------------------------------------------------------------------------
"""
[2]- Join Strings
joins (concatinates) two strings into one, using + Operator

'string' + 'string" 
output: string
joins (concatinates) two strings into one.
"""

Fname = "Belal"
Lname = "Elaiwa"
Full_name = Fname +" "+ Lname 

print(Full_name)

"""
Use Case - Build File Paths
build dynamic paths using folder and file variables
"""
folder = "C:/Users/Baraa/"
file   = "report.csv"
full_file_path = folder + file

print(full_file_path)
#---------------------------------------------------------------------------------------------------
"""
[3]- f-string
Modern, super-easy way to format and build strings
"f" stands for "formatted"

lets you easily put variables and expressions directly inside string value
EX:
print(f"My name is {name} and I am {age} years old.")
"""
name       = "Sam"
age        = "35"
is_student = False

print("My name is "+ name + ", I am " + str(age) + " years old, and student status is " + str(is_student) + "." )
# Hard to read - There are lots of plus signs and you have to worry about spaces and types
# Instead of that use f-string :

print(f"My name is {name}, I am {age} years old, and student status is {is_student}.") # Cleaner, shorter and readable

print(f"2 + 3 = {2 + 3}")

# to include {} in our output 

print("{This is me}")
print(f"{{This is me}}")
#---------------------------------------------------------------------------------------------------
"""
[4]- split()
split (separator)
str method
output: list of strings
breaks a string into smaller parts
"""
stamp = "2026-09-20 14:30"
print(stamp.split(" ")) # Outputs a list ['2026-09-20', '14:30']

stamp = "2026-09-20"
# Break a date into year, month, and day parts
print(stamp.split("-"))  # Outputs a list ['2026', '09', '20']

# Break comma-separated values into individual items
csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))  # ['1234', 'Max', 'USA', '1970-10-05', 'M']
#---------------------------------------------------------------------------------------------------
"""
[5]- String repetition
"string" * number
Operator output: string
repeats the string multiple times

Use Case - Style Your Logs
use repeated characters to create clear sections in output
"""
print("Ha" * 5)
print("=" * 100)
#===================================================================================================
# Data Extraction
# Indexing & Slicing
"""
'string'[ index ]
Operator output: string
Indexing: extracts one character by position
"""
target = "Python"

# Extract the first charact
print(target[0])
print(target[-6])

# Extract the last charact 
print(target[5])
print(target[-1])

# Extract h
print(target[3])
print(target[-3])
#------------------------------------------------------------------------------
"""
Slicing: extracts a part of the string

'string' [start: end: step]

Open-ended slicing
If you leave the start index empty, Python starts from index O

end is not included
step = 1 by default
Operator output: string
"""

date = "2026-05-23"

# Extract the year 
print(date[0:4])
print(date[:4])

# Extract the Month
print(date[5:7])
print(date[-5:-3])

# Extract the day
print(date[8:])
print(date[-2:])

# When do we youse positive and negative indexes ?
"""
Use Positive Indexes
If you want to extract part from the left side (start) of a string "When start counting from the left-side"

Use Negative Indexes 
If you want to extract part from the right side (end) of a string  "When start counting from the right-side"
"""
#===================================================================================================
# Data Cleansing
# WhiteSpace CleanUp
# It removes tabs and multiple spaces
# Only removes spaces at the start or end not in the middle
"""
Istrip()
     str method output: string
     removes spaces from the left side of a string   
strip ()
     str method output: string
     removes spaces from both ends
rstrip()
     str method output: string
     removes spaces from the right side of a string
"""
text = " Engineering "
print(text.lstrip())
# Or
text = " Engineering ".lstrip()  # add strip() while assigning the variable !!
print(text)

text = " Engineering ".strip()
print(text)

# Best Practice - Trim Spaces from User Input
# You never know where users might add spaces use .strip() to remove all extra spaces from both ends

# It removes any characters you want from the start and end - not just spaces
# By specicifying the charact to be removed !

text = "###ABC###".strip("#")
print(text)

# Use Case - Detect Extra Spaces
# Check the length before and after strip to find unwanted spaces

text = " Engineering "
print(len(text))                      # 13
print(len(text.strip()))              # 11
print(len(text) - len(text.strip()))  # 2
print(len(text) == len(text.strip())) # False

test = "   No Risk No Fun   "
nr_of_spaces = len(test) - len(test.strip())
is_clean = len(test) == len(test.strip())

print("Number of spaces:", nr_of_spaces)
print("Is my data clean", is_clean)

test = "No Risk No Fun"
nr_of_spaces = len(test) - len(test.strip())
is_clean = len(test) == len(test.strip())

print("Number of spaces:", nr_of_spaces)
print("Is my data clean", is_clean)
#-------------------------------------------------------------------------
# Case Conversion
"""
Use Case - Standardize Text Case
make sure text is always in lowercase

lower ()
str method output: string
makes all letters lowercase

upper ()
str method output: string
makes all letters uppercase
"""

text = "python PROGRAMMING"
print(text.lower())
print(text.upper())

"""
Use Case - Clean Data for Matching
Lowercase all text to prevent case-based mismatches during search or comparison
"""
search = "Email"
data   = "email"
print(search == data)

search = "Email".lower()
data   = "email".lower()
print(search == data)

# Best Practice - Clean Before Search
# Always trimm spaces and lowercase your data and search term before matching

search = " Email".lower()
data   = "email".lower()
print(search == data)

search = " Email".lower().strip()
data   = "email".lower().strip()
print(search == data)
#==============================================================================

"""
Challenge:
Turn the messy string into a single clean summary with name, role, and age
"968-Maria, (Data Engineer );; 27y
Clean the string! 
name: maria | role: data engineer | age: 27
"""

# Answer

Adv_test = "968-Maria, (D@t@ Engineer );; 27y   "
print("name:",Adv_test[4:9],"|", "role:",Adv_test[12:25].replace("@","a"),"|", "age:",Adv_test[-6:-3])
#===================================================================================================
# Searching
"""
startswith (substring)
str method output: boolean
checks if the string begins with a specific word

endswith (substring) str method
output: boolean
checks if the string ends with a specific word

'substring'in'string' Operator
output: int
checks if a word exists in the string

find (substring)
str method output: number
returns the starting position of a word in the string

find() is great when combined with other methods to add dynamics
"""
# Is the phone code German? Check the country code (+49) 
phone = "+49-176-12345"
print(phone.startswith("+49"))

email = "Belal@gmail.com"
print(email.endswith("gmail.com"))

# Is the email valid? check for @
print("@" in email)

# Check if the URL is an API endpoint

url = "https://api.company.com/v1/data"
print("/api" in url)

# Phone number without country code
# Hardcoding the start position doesn't work when the country code length changes

phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-987-895462"

print(phone1[4:])
print(phone2[3:])

# Using find()
print(phone1.find("-"))

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])
#===================================================================================================
# Validation
"""
isalpha ()
str method output: boolean
checks if the string has only letters

isnumeric ()
str method output: boolean
checks if the string has only numbers
only numbers no foat or special charcters 

"""
# Check if the country name contains only letters
country = "USA"
print(country.isalpha())

# Check if the phone number contains only numbers
phone = "01752134632"
print(phone.isnumeric())