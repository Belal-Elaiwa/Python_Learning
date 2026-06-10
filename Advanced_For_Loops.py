"""
-There are tools in Python that we can add to our loop to have more control
   like when to start, stop , skip or pass ??
  ( Break, Continue, Pass )
"""
#--------------------------------------------------------------------------
"""
[1] - Break Statement:
        - It stops the loop immediately 
        - It jumps out and ends the loop right away
        - No matter where you are currently in the loop !
        - Like Emergency Exit
""" 

names = ['John', 'Maria', '', 'Kumar']
for name in names:
    print(f"Name = {name}")
"""
Output:
Name = John
Name = Maria
Name = 
Name = Kumar
"""   
names = ['John', 'Maria', '', 'Kumar']
for name in names:
    if name == '':
        print("Empty value Detected")
        break
    print(f"Name = {name}")
"""
Output:
Name = John
Name = Maria
Empty value Detected
"""
#--------------------------------------------------------------------------
"""
[2] - Continue Statement:
        - It skips one loop cycle
        - Without stopping the loop
        - It jumps back to the top & starts the next round !
        - Skip this one and go next
        - The value skipped in the output
        - Use continue to skip bad or empty data 
          without stopping the whole loop
"""  

names = ['John', 'Maria', '', 'Kumar']
for name in names:
    if name == '':
        print("Empty value Detected")
        continue
    print(f"Name = {name}")
"""
Output:
Name = John
Name = Maria
Empty value Detected
Name = Kumar
"""
#--------------------------------------------------------------------------
"""
[2] - Pass Statement:
        - It is a placeholder where nothing happens
        - For now, just kep going Do Nothing
        - I Goes Back to our block of code !!!!!
        - No Stopping like break !
          No skipping like continue !
        - So, why do we need it ?
          as a reminder that here we have to do something 
          or kind o specific condition 
          but later ( Placeholder to be changed later ) 
        - Like iteration as we don't have a condition  
"""    
names = ['John', 'Maria', '', 'Kumar']
for name in names:
    if name == '':
        pass # To_Do: Handle Empty Value
    print(f"Name = {name}")
"""
Output:
Name = John
Name = Maria
Name =               --> Value was added in the output
Name = Kumar
"""    
# May after you meet your team and decide to replace this empty Value with Unknown 

names = ['John', 'Maria', '', 'Kumar']
for name in names:
    if name == '':
        name = name.replace('', 'Unknown')
    print(f"Name = {name}")
"""
Output:
Name = John
Name = Maria
Name = Unknown
Name = Kumar
"""        
#-------------------------------------------------------------------
# - Break vs Continue (Real-World Applications ):
"""
[1] - Task
      Loop through a list of days 
      And print only the working days 
      Skipping the weekends
"""
# Skip weekends in calendar loop
days = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
weekends = ['Fri', 'Sat']
for day in days:
    if day in weekends:
        continue
    print(f"Work_Day = {day}")

"""
[1] - Task
      Scan emails to block unsafe data
      From entering your system
"""
emails = [
    'data@gmail.com',
    'baraa@outlook.com',
    'DROP TABLE USERS;',
    'maria@gmail.com'
]

for email in emails:
    if ';' in email:
        print("SQL Injection: Hacker Attack")
        break
    print(f"Processing Email: {email}")
#-------------------------------------------------------------------
"""
Comparison Break vs Continue vs Pass
   Break:
     - Exit immediately
     - Used for critical risk 
       Security
       cost
       Integrity
   Continue: 
     - Skip 1 iteration
     - Used for medium risk
       Bad rows
       Empty fies/data
       Skip special cases
    Pass:
     - Placeholder for now       
   """
#----------------------------------------------------------------------------------
"""
[*] Else in Loops:
      - Rins a block of code if the loop finishes naturally
      - Loop completed without a Break
"""
items = [1, 3, 4, 7]
for i in items:
    print(i)
else:
    print("Loop is Completed")
"""
This else here runs no matter what so why not 
  just write it after the loop ?
"""
items = [1, 3, 4, 7]
for i in items:
    print(i)
print("Loop is Completed")   # Exact same result !!
"""
There is one scenario where else statement make sense
 Use else with loops only when there is a break !!
"""
# Else + Break
# Else will run only if the loop is not interrupted
# Task : find out if there are even numbers
items = [1, 3, 4, 7]
for i in items:
    if i % 2 == 0:
        print(f"Even Nr. Found: {i}")
        break
else:
    print("All numbers are Odd")      # Output Even Nr. Found: 4

items = [1, 3, 5, 7]
for i in items:
    if i % 2 == 0:
        print(f"Even Nr. Found: {i}")
        break
else:
    print("All numbers are Odd")     # Output All numbers are Odd
#----------------------------------------------------------------
"""
Else In Loops 
Real-World Applications:
   [1]- Search & Validate 
"""
# Task: Check for Missing Names in a List
names = ['Kamara', 'Tuba', None, 'Mounika']

for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All Names are Available")

# Task: Check if All Files are CSV Files
# My Try:
files = ['data.csv', 'docs.org', 'users.csv', 'orders.csv']

for file in files:
    if '.csv' not in file:
        print("Found Different Format")
        break
else:
    print('All Files are CSV')

# Lecturer Answer:
files = ['data.csv', 'docs.org', 'users.csv', 'orders.csv']

for file in files:
    if not file.endswith('.csv'):
        print(f"{file} is not a CSV")
        break
else:
    print('All Files are CSV')

"""
Only the first file with the wrong format will appear
if you need to display all the files !
use continue instead of break 
but it make no sense to use else + continue
So, Use only braek 

if not file.endswith('.csv'):
        print("Not all files are CSV")
        break
"""
#------------------------------------------------------------------
# Challenge 
"""
Check whether any filename appears more than once
Print "Duplicate found" if a duplicate exists, otherwise print "All files are unique"
"""
file_list = [
        'report. csv',
        'data. xlsx',
        'summary.docx',
        'report. csv',
        'data. csv'
]
# Answer:
for f in file_list:
    if file_list.count(f) > 1:
        print("Duplicate found")
        break
else:
    print("All files are unique")
#-------------------------------------------------------------
# Nested For Loop
"""
- Loop inside Another Loop
- Outer loop & Inner Loop
- Every each iteration from the outer loop the inner loop will fully run 
- You could have another Loop inside the small loop   (1(2(3))) 
"""
for x in range(4):       # Outer Loop
    for y in range(2):   # Inner Loop
        print(f"({x}, {y})")
# Output 
"""
(0, 1)
(1, 0)
(1, 1)
(2, 0)
(2, 1)
(3, 0)
(3, 1)
"""      
# You can add a Third Loop 
for x in range(4):            # Outer Loop
    for y in range(2):        # Inner Loop
        for z in range(2):    # Third Loop
            print(f"({x}, {y}, {z})")
# Output 
"""
(0, 0, 0)
(0, 0, 1)
(0, 1, 0)
(0, 1, 1)
(1, 0, 0)
(1, 0, 1)
(1, 1, 0)
(1, 1, 1)
(2, 0, 0)
(2, 0, 1)
(2, 1, 0)
(2, 1, 1)
(3, 0, 0)
(3, 0, 1)
(3, 1, 0)
(3, 1, 1)
"""               
#------------------------------------------------------------------------
"""
Nested For Loops 
Real-World Applications:
   [1]- Crossing and Combining Our Data (Data Pairing)
            - If we have 2 Data Lists 
            - Trying to get All Possible Combinations 
            - Each Value from one list with ALL values from the Other List
"""
# Generate a Product Catalogue with all Combinations of colors and sizes
colors = ['red', 'blue', 'yellow']  
sizes = ['L', 'M', 'S']

for color in colors:                    # Doesn't Matter Where You Start
    for size in sizes:
        print(f"({color} - Size {size})")
#------------------------------------------------------------------------
"""
[2]- Navigate Hierachy
           - Using Nested For Loops 
             in order to drill down Hierachy
             Like Tables, Columns & Rows 
             Like Date 
                Level 1   for year in years:
                Level 2        for month in months:
                Level 3            for day in days:
                                       print()
"""  
# Creation of multiple Reports for each day, month, year 
years = [2026, 2027]
months = ['Jan', 'Feb']
days = range(1, 29)    

for year in years:
    for month in months:
        for day in days:
            print(f"Report_{year}-{month}-{day}.csv")
#------------------------------------------------------------------------------
# SELECT count(*) FROM customers where id is NULL;
tables = ['customers', 'orders', 'products', 'prices']
columns = ['id', 'create_date']     

for t in tables:
    for c in columns:
        print(f"SELECT COUNT(*) FROM {t} WHERE {c} is NULL;")