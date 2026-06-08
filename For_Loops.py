"""
= What i Loop in Python ?
  - Control the flow of code 
  - Repeat a block of code over and over until a condition is met
  - Two types of Loops:
         - For Loops
         - While Loops
[1] = For Loops          
      Basics :
      - Go through a group of items one by one 
        to do something for each item 
      - You have always to specify a sequence 
        Group of items that has a start and an end 
      - You can mix between numbers and strings inside
        the sequence  
      Python Iterator:   
      - An object that lets you go through items 
        one by one in a sequence 
        ' remember what's done. know what's next
"""
# Instead of repeating code over and over
# We can write our code once and put it in a loop

print("Round :1")
print("Round :2")
print("Round :3")
print("Round :4")
print("Round :5") 

for i in (1,2,3,4,5):
    print("Round: 1")    # This will print Round: 1" 5 times as we have 5 items in the list

for i in (1,2,3,4,5):
    print(i)             # This will print 1 2 3 4 5

for i in (1,2,3,4,5):
    print(f"Round: {i}") # This will print Round: 1 Round: 2 .. etc   

"""
You can assign the sequence into a variable 
But use the same word
Variable --> Singular
Sequence --> Plural
"""
items = (1,2,3,4,5)
for item in items:
    print(f"Order: {item}")
#-------------------------------------------------------------------
"""
For loops
Sequences you can loop
  - tuple
  - list 
  - string !
      string appears like a single value 
      but for Python it is a sequence of letters
      each letter considered a value 
      even the space will considered as a character
  - built in function called range
      a built in function that generates a sequence of numbers 
      range(stop) if you wrote range(5) => 0,1,2,3,4  '5' Not included  
      range(start, stop)       => to control the output !
      range(start, stop, step) => to control the increments 
                                  By default is 1.
  - You can use any object that is iteratable                                
  """

items = "Python"
for item in items:
    print(f"Round: {item}")  # This will print P  y  t  h  o  n

for item in range(5):
    print(f"Round: {item}")  # stops at 4  

for item in range(1, 5):
    print(f"Round: {item}")  # stops at 4 ! - end is always NOT INCLUDED  

for item in range(1, 6):
    print(f"Round: {item}")  # stops at 5

# To display the even numbers 0: 10 use step
for item in range(0, 10, 2):
    print(f"Round: {item}")  # 0,2,4,6,8

# To display the even numbers 1: 10 
for item in range(1, 10, 2):
    print(f"Round: {item}")  # 1,3,5,7,9
#------------------------------------------------------------------------
"""
For Loops
Real-world Applications 

- If you have hundreds of files in your source data 
  you can write the code once instead of hundreds times 
  and iterate it through all your data sources

- Dtat Preparation 
  In Data cleaning up 
  if you are using the same action for the whole files

- Not only files and tables
  can be used with columns 
  For example if you have lead and trail spaces in the columns values 
  instead of muillion codes, use for loop  
"""

"""
[1]- Using For Loops to go through values 
     and aggregate data
     like summing, counting, or averaging 
"""
# Find the total of this list
scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total = total + score    # Instead total += score   # Use the loop variable not the sequence
    print("Current total:", total)

print("Final Total:", total)

"""
[2]- Using For Loops to transform data 
     like cleaning data before processing
"""

files = [' Report.csv', 'DATA.csv ', ' final.TXT']

# for file in files:
#     print(file.strip())    # My Try 

# Ideal
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')  # Write it in small case 
    print(f"Processing {file}")                          # as it comes after lower() function!!
# Clean first, Transform second --> Always in that order  "Very Important"
#------------------------------------------------------------------------------------------------
# Challenges 
"""
[1] - Print the 7-times table 
      from 1 to 10
      using a for loop
      to look exactly like:
      7 x 1 = 7
      7 x 2 = 14
      7 x 3 = 21
      7 x 4 = 28
                ..  etc
"""
# Answer

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(f"7 * {number} = {7 * number}")

#OR
for number in range(1,11):
    print(f"7 * {number} = {7 * number}")

#OR
for number in range(1,11):
    result = 7 * number
    print(f"7 * {number} = {result}")

"""
[2] - Print a left-aligned 
      pyramid of stars with 6 rows 
      using a for loop 
"""
# Answer

for number in range(1,7):
    print("*" * number)