"""
While Loops
   - Used to repeat a block of code over and over
     as long as condition is True
   - Difference between for and while loops ?
     For Loops:
         - Predefined Sequence "Known Times"   --> for i in [1, 2, 3]
         - Predefined Condition from Python 
           It is always about whether we are at the end of the sequence or not ?  
     While Loops:
         - Defined condition   
           We define our own loop  "Unknown Times"
           When it is true --> Do something and go back to the top
           as long as it is true --> we will keep looping and iterating
           when it becomes False --> Exit the Loop
         - It is Risky 
           As we might End_Up easily in an infinite Loop
While Loops Designs:
   [1] - While Condition 
         We define a condition and the Loop keep going until the condition becomes False
         Classical Type
   [2] - While True:
         This loop will runs forever
         So, we add to it a break statement 
         in order to force the loop to stop  

[1]- While Condition 
     i = 1         --> Initialization 
     while i < 4:  --> Condition
         print(i)  --> Action when True

    In this case Python prints i again & again .. infinite loop 
    That is why we have to add a new line inside our while loop
    to give a chance for the i to change !         

      i = 1         --> Initialization 
     while i < 4:  --> Condition
         print(i)  --> Action when True
         i += 1    --> Allowing i to change (Update Mechanism) 
"""
# Task: Build a counter from 1 to 5

count = 1
while count <= 5:
    print(count)
    count += 1     # Here it is Hard_Coded, How to make it a dynamic one ?

# Task: Write a program that keeps asking "Do You Agree?" until the user types yes

answer = "" 
while answer != "yes":
    answer = input("Do you agree? (yes/no): ")
print("Thank You")
#--------------------------------------------------------------------------------    
"""
[2]- While True
     The most powerful and the most risky
     while True:
         Do something
     if x == 'stop'
         break
             
"""
while True:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        break
print("Thank You")

# Challenge 
"""
For the previous Loop 
Re-Design it with these requirements
  - Allow up to 3 attempts
  - If the user types "yes", print "Glad we are on the same page"
  - Otherwise, print "3 Strikes, You are Out!"
"""
# Answer:
# If you know how many times to loop, use while condition - not while True!
# How can a loop do onje thing when it finds something, and another when it doesn't?
# Use else + break for either-or logic in loops

attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we are on the same page")
        break
    attempts += 1
else:
    print("3 Strikes, You are Out!")   
# -----------------------------------------------------------------------------------
# While Condition VS True
"""
While Condition:
    - When know when the loop should stop
    - Exists Normally - Condition = False
    - Safer & More readable
    - Best use cases: counter, limited retries or validating the output from the user
While True:
    - It gonna run forever
    - Must have extra if + break
    - Risk of infinite loop + More flexible
    - Best use cases: Open-ended scenario waiting for a trigger from something external
      like Database, Stream, API
"""

# Loops For VS While
"""
For Loops:
   - Loop over a fixed sequence
   - Predefined condition
   - Use if Nr. of iterations is known "Processing data"
   - Simple, Clear and Safe but limited
While Loops:
   - Loop while a condition is True
   - You can add your own condition for the iterations   
   - Use if we don't know how many times we want to iterate "Waiting for external event"
   - Advanced, Flexible but complex and risky
"""