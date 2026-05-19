# input() Function
# Built-in function that stops your program to get user input !
# It is used for example in signing in any application that requires E-Mail, Password..etc
# Ask the users to input thier names:

input("Enter Your Name:")  # It will displayed only in terminal 
                           # Input data will be lost
""" INPUT() and Variables
Using INPUT() alone reads the user's response but immediately discards it.
To keep the value, assign it to a variable! """                           

name = input("Enter your Name:")
print("You Are", name)

# Difference between Hard-Coded values and Dynamic Values
# Dynamic Values:
#           data entered by the user that can vary each time the program runs.

#Hard-Coded (static) Value:
#           fixed piece of data written directly into your code that never changes at runtime.

name = input("Enter your Name:") # Dynamic Value ( Waiting input from user)
country = "Netherlands"          # Hard-Coded Value
print(name, "Comes from", country)