# Logical Operators : and | or | not
# Used to connect multiple boolean expressions to build a logic or rules
# and => Both of them must be True
# or  => At least one condition must be True

print(3 > 1 and 5 < 1) # Returns False
print(3 > 1 and 5 > 1) # Returns True

print(3 > 1 or 5 < 1)  # Returns True
print(3 > 1 or 5 > 1)  # Returns True
print(3 < 1 or 5 < 1)  # Returns False

# Checking if the system is under pressure?
CPU_usage    = 70
memory_usage = 95

print(memory_usage > 90 or CPU_usage > 90)  # Returns True

# checking user credentials before login?
email = True
password = True
print(email and password)

email = True
password = False
print(email and password)

email = False
password = False
print(email and password)
#---------------------------------------------------------------------------

# Operator (not)
# It reverses the truth it turns True into False and vice versa

print(not 3 > 2) # Returns False
print(not True)  # Returns False 
print(not False) # Returns True

name = ""
print(not name)  # Returns True as Boolean of empty is False
#---------------------------------------------------------------------------

# Control Multiple Conditions
# "and" has higher priority than "or"
# To control Execution Order ==> Parentheses () First

print(5 == 5 or 8 > 5 and 6 < 4)    # Returns True
print((5 == 5 or 8 > 5) and 6 < 4)  # Returns False

# Why? 

5 == 5 or 8 > 5 and 6 < 4
"""
Python will execute "and" before "or"
[1] 8 > 5 and 6 < 4       
     True      False   => Returns False 
[2] 5 == 5 or False
     True      False   => Returns True   
"""

(5 == 5 or 8 > 5) and 6 < 4
"""
Python will execute "()" before "and"
[1] 5 == 5 or 8 > 5      
     True      True  => Returns True
[2] True and 6 < 4   
     True     False   => Returns False   
"""

# Task
"""
Allow access only if user logged in 
or they are guest
but they must not banned
"""
# Answer

is_logged_in = True
is_guest = False 
is_banned = True

print((is_logged_in or is_guest) and not is_banned)  
# not here is referes to the condition itself not the meaning !!

# challenge 
"""
[1] Check if the user name is not empty and the age is greater than or equal to 18
[2] Check if the password is at least 8 characters long and does not contain spaces 
[3] Check if a user's email is not empty, contains '@', and ends with '.com'
[4] Check if a username is a string, is not None, and is longer tahn 5 characters
[5] Check if the user is either an admin or a moderator, 
    and either they are not banned or they have verified their email
"""
print("=" * 100)
# Answer
# [1]
user_name = "Belal"
age = 35
print(user_name != "" and age >= 18 )

# [2]
password = "mypass12345"
print(len(password) >= 8 and len(password) == len(password.strip()))
print(len(password) >= 8 and " " not in password)

# [3]
email = "myEmail@gmail.com"
print(email != "" and "@" in email and email.endswith(".com"))

# [4]
print(type(user_name) == str and user_name != None and len(user_name) > 5)

# [5]

user_name = "Belal"
email     = "verifiedemail@gmail.com"
title    = "moderator"
is_Verified = True
is_banned   = False

print((title == "moderator" or title == "admin" ) and (is_Verified or not is_banned))
print((title in ["moderator","admin" ]) and (is_Verified or not is_banned))