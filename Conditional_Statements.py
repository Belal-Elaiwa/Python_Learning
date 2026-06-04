"""
Conditional Statements (IF, ELSE, ELIF)
  Checkpoint that checks a condition like traffic lights
          - True ? Runs the code
          - False ? Skip it
""" 
#------------------------------------------------------------ 
"""
if Statement
Defines the first condition 
"if this is true do this -
otherwise, do nothing "
   - Only One if in each chain
   - Starts with if
   - Always required
   - Can standalone 
Syntax Ex
if condition :
  print()       => : after the condition & 2 spaces before action (print)    'Indentation'
"""
score = 100
if score >= 90:
    print("Grade: A")
    print("Great job")

#----------------------------------------------------------------------------------------
# Python Indentation
"""
- Means adding spaces at the beginning of a line to show that this line belongs to a code block
- Indentation in Python is part of the syntax
- To add 4 spaces automatically:
   - ctrl+shift+P => Type preferences user settings json
   - add this part of code
       "[python]": {
       "editor. tabsize": 4,
       "editor.insertSpaces": true
       }  
   - Then save and restart VSC
"""
#-----------------------------------------------------------------------------------------
# Two-Way Decision if-else
"""
Else statement runs only if the answer of the previous condition is False
"if nothing was true, do this instead"
Only one path runs !, either if or else
   - come at the end
   - No conditions
   - Optional
   - Can't standalone, Can't used alone (needs an if at the start)
   - Only one else
"""
score = 50
if score >= 90:
    print("Grade: A")
else:
    print("Grade: F")
#-----------------------------------------------------------------
# Multiple Conditions (if, elif, else)
"""
elif statement
Short of Else If
Asks a follow-up question
Only runs if previous conditions were false
"If the first wasn't true, try this one".

Condition 1: 
    do A
elif condition 2: 
    do C
else:
    do B

  - Comes always after the if statement
  - Multiple elif
  - Needs Condition
  - Optional
  - Can't standalone  
"""
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: F")
#---------------------------------------------------------
# Branching if-elif-elif-else

score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")    
else:
    print("Grade: F")


score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")        
else:
    print("Grade: F")
#--------------------------------------------------------------
# Nesting if-else
"""
Nested if 
if statement inside another if 
"if the first is true, then check the second"
Each if statement can be followed by else
"""

score = 75
submitted_project = True

if score >= 90:
    if submitted_project:  # Python evaluates Boolean conditions directly Avoid explicit comparisons == True or == False
        print("Grade: A+")
    else:
        print("Grade: A")        
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")        
else:
    print("Grade: F")
#-----------------------------------------------------------------------------------------------------------------------
# Connecting conditions - Logical Operators

if score >= 90 and submitted_project:  # Both of them should be True
     print("Grade: A+")
elif score >= 90:
    print("Grade: A")  
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60 or submitted_project:
    print("Grade: D")        
else:
    print("Grade: F")
#---------------------------------------------------------------------------------------------------------------
# Independent if - else
"""
- Ifs
  Each is checked separately
  All conditions are tested even if one is already True !!
  No dependency between them
"""
grade = 50
submitted_project = True

if grade >= 90:
    print("High score")
else:
    print("Low Score")
if submitted_project:
    print("Project is Submitted")
else:
    print("Project is Not Submitted") 
#--------------------------------------------------------------------------------------------
# Challenge [1]
"""
Validate the Quality and Correctness of Email Values
- Must not be empty
- Must contain '.' and '@'
- Must contain exactly one '@' symbol
- Must end with 'com', org', or 'net'
- Must not be longer than 254 characters
- Must start and end with a letter or digit
"""

# Answer

email = "Belal.12345@Gmail.com"

# firstly clean the Data
email = email.strip()

#[1] - Email Must not be empty
if email == "":
    print("Email is Empty")
#[2] - Email Must contain '.' and '@'
elif "." not in email:
    print("Abscence of '.'")
elif "@" not in email:
    print("Abscence of '@'")    
#[3] - Email Must contain exactly one '@' symbol
elif email.count("@") != 1:
    print("More than one '@'")
#[4] - Email Must end with 'com', org', or 'net'
elif not (email.endswith('.com') or email.endswith('.net') or email.endswith('.org')):
    print("Error in Email End")
#[5] - Email  Must not be longer than 254 characters
elif len(email) > 254:
    print("Email is longer than 254 characters") 

# #[6] - Email Must start and end with a letter or digit         # XXX - I didn't know how to solve this - XXX 
# elif type(email.startswith()) != str and type(email.startswith()) != int:
#     print("Email has a typo in the start")
# elif type(email.endswith()) != str and type(email.endswith()) != int:
#     print("Email has a typo in the end")

else:
    print("Email is valid")
#==============================================================================================
# The Ideal Answer For Challlenge [1]

# Clean the String
email = email.strip()
# Email must not be empty
if email == "":
    print ("Email cannot be empty.")
# Email must contain a '.' and '@'
elif not('.' in email and '@' in email):
    print ("Email must contain . and @")
# Email must contain exactly one '@' symbol
elif email. count ('@') != 1:
    print ("Email must contain exactly one @.")
# Email must end with '.com', '.org', or '.net"
elif not email.endswith(('.com', '.org','.net')):
    print("Email must end with .com, .org, or net")
# Email must not be longer than 254 characters
elif len(email) > 254:
    print ("Email must not be longer than 254 characters")
# Email must start and end with a letter or digit
elif not(email[0].isalnum() and email[-1].isalnum()) : #isalnum() - Checks if the string contains only letters and digits
    print ("Email must start and end with a letter or digit")
else:
    print ("Email is valid.")

"""
You want to stop at the first condition that returns True ??!!
     - This will happen when using if-elif-else
Or you want all conditions to be evaluated ??
     - So, use independant if statements
 ==> But notice that the last else belongs for the last condition only !!
     you have options for else :
              - Add an else in every if statement
              - remove else
              - assign a new variable     
"""

# Email must not be empty
if email == "":
    print ("Email cannot be empty.")

if not('.' in email and '@' in email):
    print ("Email must contain . and @")

if email. count ('@') != 1:
    print ("Email must contain exactly one @.")

if not email.endswith(('.com', '.org','.net')):
    print("Email must end with .com, .org, or net")

if len(email) > 254:
    print ("Email must not be longer than 254 characters")

if not(email[0].isalnum() and email[-1].isalnum()) :
    print ("Email must start and end with a letter or digit")
else:
    print ("Email is valid.")
#-----------------------------------------------------------------------------------------------
# Challenge [2]
"""
Validate the Quality and Correctness of Passwords
- Must not be empty
- Must be at least 8 characters
- Must include at least 1 uppercase
- Must include at least 1 lowercase
- Must not be same as the email
- Must not contain any spaces
- Must start and end with a letter or digit
"""
# Answer 

password = "As12345689"
email = "Belal.123456@Gmail.com"

#[1] - Must not be empty
if password == "":
    print("Password Can't Be Empty")
else:
    print("Password Is Valid")    
#[2] - Must be at least 8 characters  
if len(password) < 8:
    print("Password Must Be AT Least 8 Characters")
    print("Password Is Valid")  
#[3] - Must include at least 1 uppercase  # XXX IDK How to solve this
#[4] - Must include at least 1 lowercase  # XXX IDK How to solve this
#[5] - Must not be same as the email
if password == email:
    print("Password Can't Be As Same As The Email")
    print("Password Is Valid")
#[6] - Must not contain any spaces      
if " " in password:
    print("The Password Can't Contain Any Spaces")
#[7] - Must start and end with a letter or digit  
if not(password[0].isalnum() and password[-1].isalnum()) :
    print ("Password must start and end with a letter or digit")
else:
    print ("Password is valid.")




































