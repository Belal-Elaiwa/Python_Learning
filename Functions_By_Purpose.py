# Function types By Purpose -- Use Cases
"""
Action Functions:
Designed to perform an operation in the system
instead of returning values.
Like print, connect, send, call
"""
"""
- Task:
    Stores apllication log messages in a file whenever an event occurs
- with open()
    Opens the file safely and closes it automatically when done
- Append Mode "a"
    it appends data at the end of the file    
"""
def write_log(message):
    with open(r"D:\Belal Data\Python Handling\Testing\app.log", "a") as file:
        file.write(message + "\n")
write_log("App Started")    
write_log("User Logged-In") 
write_log("App Stopped") 
#----------------------------------------------------------------------------
"""
Transformation Functions
- Raw data goes in, gets transformed, and returns processed data
- Data Manipulation "Business Logic"
- Most Important Shape of Functions
"""
"""
Task:
Clean E-mail addresses and split them into structured data
(username and domain)
"""

def clean_split_email(email):
    clnd_email = email.strip().lower()
    username, domain = clnd_email.split("@")
    return {"username": username, 
            "domain": domain}
test = clean_split_email(" SARA@gMaiL.cOm   ")
print(test)   # Output: {'username': 'sara', 'domain': 'gmail.com'}
#----------------------------------------------------------------------------
"""
Validation Functions
- Validates a condition and returns 
  a boolean result (True or False) 
"""
"""
Task:
Check whether the password meets the minimum requirement of 8 characters?
"""

def is_valid_password(password):
    return len(password) >= 8
print(is_valid_password("123456"))    # Output: False
print(is_valid_password("12345678"))  # Output: True

"""
Task:
Check whether an email has a basic valid format?
"""

def is_valid_email(email):
    return "@" in email and "." in email
print(is_valid_email("SaraGmail.com"))   # Output: False
print(is_valid_email("Sara@Gmail.com"))  # Output: True
#----------------------------------------------------------------------------
"""
Orchestrator Functions
- Controls program flow by calling many other functions
  in the correct order
- Connect everything together and decide what is the next step to be executed  
"""
"""
Task: Project
    1 Receive an email from the user
    2 Validate the email
    3 If it is invalid, Log an error in a file.
    4 If it is valid, Clean and structure the email.
    5 Log each step of the program.
"""
write_log("Application Started")
# We receive an email from a user
email = input("Please enter Your E-Mail: ")
# We must check if it is valid
# If it is not valid, we log the problem
# If it is valid, we clean it and store structured information
# And we log what happened
if not is_valid_email(email):
    write_log(f"Invalid E-Mail: {email}")
else:
    clean_email = clean_split_email(email)
    write_log(f"Processed E-Mail: {clean_email}")    
write_log("Application Ended")    
"""
Testing

- Inputted: SArA@Gmail.com  
  Outputted in the file:
  Application Started
  Processed E-Mail: {'username': 'sara', 'domain': 'gmail.com'}
  Application Ended

- Inputted: Eman.com
  Outputted in the file:  
  Application Started
  Invalid E-Mail: Eman.com
  Application Ended
"""
# Where is the Orchestration Function ?
# Here To Go:

# Orchestrator Function 
def proccessed_email(email):
    write_log("Application Started")
    if not is_valid_email(email):
        write_log(f"Invalid E-Mail: {email}")
    else:
        clean_email = clean_split_email(email)
        write_log(f"Processed E-Mail: {clean_email}")    
    write_log("Application Ended")    

email = input("Please enter Your E-Mail: ")
proccessed_email(email)

"""
Testing

- Inputted: SArA@Gmail.com  
  Outputted in the file: BElAl@GMAIL.COM
  Application Started
  Processed E-Mail: {'username': 'belal', 'domain': 'gmail.com'}
  Application Ended 

- Inputted: EMANGMAIL.com
  Outputted in the file:  
  Application Started
  Invalid E-Mail: EMANGMAIL.com
  Application Ended
"""