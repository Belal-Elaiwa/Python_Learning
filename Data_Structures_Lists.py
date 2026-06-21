# Data Structure 
"""
Lists[]
   - Ordered collection of items
   - Very flexible, changeable
   - Allows duplicates
   - Very common and widely used

Operations and things that you can do with a list:
   - How to create?
   - How to access and read?
   - How to unpack?
   - How to explore and analyze?
   - How to change the original data?
   - How to reorganize and order data inside a list?
   - How to copy?
   - How to combine?
   - How to iterate?
   - How to transform?
   - How to filter?
   - List Comprehension   
"""
# [1]- How to create?

empty = []
print(empty)        # Output []
print(type(empty))  # Output <class 'list'>
#---------------------------------------------------------------------
# Adding data inside the list
# [1]- Manually
letters = ['a', 'b', 'c']
print(letters)      # Output ['a', 'b', 'c']

# You can mix Diff. data types inside the same list
mixed = [1, 'a', True, None]
print(type(mixed))  # Output <class 'list'>
#---------------------------------------------------------------------
# [2]- By Using the built-in function list()
"""
list (value)
built-in function output: list
converts an iterable (sequence) into a list
"""
empty = list()
print(empty)               # Output []

letters = list('Python')
print(letters)             # Output ['P', 'y', 't', 'h', 'o', 'n']

numbers = 1, 2, 3, 4
print(list(numbers))       # Output [1, 2, 3, 4]

numbers = list(range(5))
print((numbers))           # Output [0, 1, 2, 3, 4]
#---------------------------------------------------------------------
# Create Nested List (Matrix)
# 2Lists inside a List

matrix = [['a', 'b', 'c'], 
          ['d', 'e', 'f']]

mixed_matrix = [['a', 'b'],
                [1, 2, 3, 4],
                [True]]

print(matrix)             # Output [['a', 'b', 'c'], ['d', 'e', 'f']]
print(mixed_matrix)       # Output [['a', 'b'], [1, 2, 3, 4], [True]]
print(type(matrix))       # Output <class 'list'>
#----------------------------------------------------------------------
# How To Access & Read Lists in Python ( Indexing & Slicing)
# Access & Read
lst = ['a', 'b', 'c', 'd']
print(lst)

# Indexing
print(lst[0])   # The first item from the list --> Python is Zero Indexed
print(lst[-1])  # The last item                --> Starts with 0 From the left, -1 From the right
print(lst[-2])

# Nested List (Matrix)
"""
It will be like Rows
Having Row Number and an Index number
Each list is a row 
Indexed from Row zero From the Left
print(list name)                               --> Returns the hole list
print(list name [One Number])                  --> Returns Only one list (Row)   
print(list name[First Number][Second Number])  --> Returns a specific item inside a specific list (Row)   
 """
matrix = [['a', 'b', 'c'],   # Row 0 
          ['d', 'e', 'f'],   # Row 1
          ['g', 'h', 'i']]   # Row 2
print(matrix)                # [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]  
print(matrix[2])             # ['g', 'h', 'i']
print(matrix[-1])            # ['g', 'h', 'i']
print(matrix[-1][-1])        # i 'The last item from the last row'
print(matrix[0][0])          # a 'The first item from the first row'

# Slicing
"""
Retrieving Multiple Items
Syntax:
list_name[Start_Index:End_Index]  --> The End is not included
list_name[:End_Index]             --> You can skip the start index it is ZERO by default 
list_name[Start_Index:]           --> You can skip end index it retrieves the rest by default
"""
lst = ['a', 'b', 'c', 'd']
print(lst[0:2])        # ['a', 'b']  --> First 2 characters 
print(lst[2:])         # ['c', 'd']  --> Last 2 characters 
print(lst[:])          # ['a', 'b', 'c', 'd']

print('=' * 150)
# Matrix Slicing
matrix = [['a', 'b', 'c'],   # Row 0 
          ['d', 'e', 'f'],   # Row 1
          ['g', 'h', 'i']]   # Row 2
print(matrix[:2])            # First 2 Rows [['a', 'b', 'c'], ['d', 'e', 'f']]
print(matrix[1:])            # Last 2 Rows  [['d', 'e', 'f'], ['g', 'h', 'i']]
print(matrix[2][:2])         # First 2 Characters in the Second Row ['g', 'h']
#-----------------------------------------------------------------------------
# Unpacking
"""
- Unpacking the list for example to use the information inside as a different variables !!
  To be easier to do different operations
- Unpacking:
  List of variables, separated by commas 
"""
person = ['Maria', 29, 'Data Engineer', 'Berlin']
name = person[0]
age = person[1]
role= person[2]
country = person[3]
# Using only indexes makes code long and hard to extend!!
# Smarter:
name, age, role, country = person 
# Testing
print(name)
print(age)
print(role)
print(country)
# Unpacking is clean, easy, and makes code simple to extend
#----------------------------------------------------------------------
# Rest collector Asterisk *
"""
- If you interested only in the first & last items
- Assigning a * to mark the rest
"""
person = ['Maria', 29, 'Data Engineer', 'Berlin']
name, *details, country = person 
print(name)
print(details) 
print(country)
# Output
"""
Maria
[29, 'Data Engineer']
Berlin
"""
name, *details = person 
print(name)
print(details)
# Output
"""
Maria
[29, 'Data Engineer', 'Berlin']
"""
*details, country = person 
print(details)
print(country)

numbers = [1]
first, *rest = numbers
print(first)
print(rest)
# Output
"""
1
[]
"""
string = 'Hello'
first, *rest = string
print(first)
print(rest)
# Output
"""
H
['e', 'l', 'l', 'o']
"""

# Unpacking Rules:
"""
- Variables order must match the list values order - not less, not more
- Asterisk * collects the leftovers, and it's fine if there are None
- Only one Asterisk is allowed in Unpacking
- Only use asterisk in unpacking not in calling
- You can Unpack any sequence (Lists, Tuples, strings, ..etc)
"""
#---------------------------------------------------------------------------
# Skipping Items
# Unpacking Using Underscore '_'
person = ['Maria', 29, 'Data Engineer', 'Berlin']
name, _, role, _ = person  # "_" Skips, No variable Created, Saves the space
print(name)
print(role)
# Combining asterisk * & UnderScore _

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first, *_, last = test  # To Save Memory, No variable Created, No Multiple "_" added
print(first)
print(last)
#-----------------------------------------------------------------------------------
# Explore & analyze lists
"""
Functions to use:
  Analyze:
    - max()   --> Extreme high
    - min()   --> Extreme low        
    - sum()   --> Total    
    - len()   --> Length

  Completeness of existence check
    - all()   --> Did everything pass?
    - any()   --> Did something pass?

  Search & Count
    - .count('A') --> How often?
    - .index('A') --> Where it appears?   

  Membership & Identity
    - in     --> Check if exist?   
    - is     --> Check if some object?

  Comparison
    - ==
    - >    
"""
# Exs:
numbers = [1, 5, 2, 4, 3]

"""
max ()
Function
output: List Item
Find the highest value
"""
print("Max:", max(numbers))   # Output--> Max: 5

"""
min ()
Function
output: List Item
Find the lowest value
"""
print("Min:", min(numbers))       # Output--> Min: 1

"""
sum ()
Function output: number
Finds the total by summing all values
Works only with numbers
"""
print("Sum:", sum(numbers))      # Output--> Sum: 15

"""
len ()
Function output: number
Finds the length of a list (number of items)
Works for any data type
"""
print("Length:", len(numbers))   # Output--> Length: 5

"""
all ()
Function output: True/False
returns True if all values are True

any ()
Function output: True/False
returns True if at least one value is True
"""
print("All:", all(numbers))          # Output--> All: True
print("All:", all([1, 0, 2]))        # Output--> All: False  It considered 0 as a missing value
print("All:", all(['a', '', 'b']))   # Output--> All: False

print("Any:", any(numbers))          # Output--> Any: True
print("Any:", any([1, 0, 2]))        # Output--> Any: True
print("Any:", any(['a', '', 'b']))   # Output--> Any: True
print("Any:", any([0, 0, 0]))        # Output--> All: False  It considered 0 as a missing value

"""
.count()
Returns how many times a value appears in the list

.index()
returns the position of the first occurrence of a value
only positive numbers
"""
print("Count:", numbers.count(5))    # Output--> Count: 1
print("Index:", numbers.index(5))    # Output--> Index: 1

"""
in & not in 
in
Operator output: True/False
Checks if a value exists in a sequence


"""
numbers = [1, 5, 5, 4, 3]
print(4 in numbers)               # Output--> True
print(8 in numbers)               # Output--> False
print(8 not in numbers)           # Output--> True

"""
Comparison Operators 
==, <, >

Comparison
The first elements are compared,
If they're equal, Python moves to the next element
"""
list1 =[1, 2, 3]
list2 =[1, 2, 3]
print(list1 == list2)             # Output--> True

list1 =[1, 2, 3]
list2 =[5, 2, 3]
print(list1 < list2)             # Output--> True  -- How??

list1 =[1, 2, 3]
list2 =[1, 2, 3]
print(list1 is list2)             # Output--> False
"""
Python checks the identity! 
( Two lists have different addresses and different identities)
Two separate Objects
'is' doesn't care about the values
It only considers the identities
"""
#------------------------------------------------------------------------
# How To Change a list ?
# Adding, Removing, Updating
#------------------------------------------------------------------------
# Add Items
"""
.append()
Append or add the new value
at the end of the list!
"""
# Task: Add 'x' to the end of the list
letters = ['a', 'b', 'c']
letters.append('x')
print(letters)         # Output --> ['a', 'b', 'c', 'x']

# Task: Add 'y' to the end of the list
letters.append('y')
print(letters)         # Output --> ['a', 'b', 'c', 'x', 'y']

"""
.insert(index, value)
Flexible
Controlled
You can add a specific value at a specific position
"""
# Task: Add 'x' to the start of the list
letters = ['a', 'b', 'c']
letters.insert(0, 'x')
print(letters)          # Output --> ['x', 'a', 'b', 'c']

# Task: Add 'y' between 'b' and 'c'!
letters.insert(3, 'y')
print(letters)         # Output --> ['x', 'a', 'b', 'y', 'c']

# For Matrix List !!
# Task: Add new row to the end of matrix
matrix = [['a', 'b', 'c'],   # Row 0 
          ['d', 'e', 'f'],   # Row 1
          ['g', 'h', 'i']]   # Row 2
matrix.append(['j', 'k', 'l'])
print(matrix)          # Output --> [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']]     

# Task: Add new row to the start of matrix
matrix.insert(0, ['x', 'y', 'z'])
print(matrix)          # Output --> [['x', 'y', 'z'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']]

# Task: Add 'x' at the end of the second row!!
matrix = [['a', 'b', 'c'],   # Row 0 
          ['d', 'e', 'f'],   # Row 1
          ['g', 'h', 'i']]   # Row 2
matrix[1].append('x')
print(matrix)          # Output --> [['a', 'b', 'c', 'x'], ['d', 'e', 'f'], ['g', 'h', 'i']]

# Task: Add 'z' at the start of the first row
matrix[0].insert(0, 'z') 
print(matrix)          # Output --> [['z', 'a', 'b', 'c'], ['d', 'e', 'f', 'x'], ['g', 'h', 'i']]
#-----------------------------------------------------------------------------------------------
# Remove Items
"""
.clear()
- Method that clears everything
"""
letters = ['a', 'b', 'c']
letters.clear()
print(letters)      # Output --> []

"""
.remove()
- Method that deletes according to value 
- Removes only the first match
- It will stop after the first match

.pop(index)
- Method that deletes according to position
- Doesn't care about the value
.pop()
- The default --> Will remove the last positioned value
- It remove and can return the removed!
"""
letters = ['a', 'b', 'a']
letters.remove('a')
print(letters)      # Output --> ['b', 'a']   Only removed the first 'a'

letters = ['a', 'b', 'a']
letters.remove('a')
letters.remove('a')
print(letters)      # Output --> ['b']

letters = ['a', 'b', 'a']
letters.pop(0)
print(letters)      # Output --> ['b', 'a']

letters = ['a', 'b', 'c']
removed = letters.pop()
print(letters)                    # Output --> ['a', 'b']
print("Removed Item:", removed)   # Output --> Removed Item: c

# For matrix ??
matrix = [['a', 'b', 'c'],   # Row 0 
          ['d', 'e', 'f'],   # Row 1
          ['g', 'h', 'i']]   # Row 2
matrix.remove(['a', 'b', 'c'])
print(matrix)                    # Output --> [['d', 'e', 'f'], ['g', 'h', 'i']]
matrix.pop()
print(matrix)                    # Output --> [['d', 'e', 'f']

# Task: Remove 'e' from the second row in the matrix
matrix = [['a', 'b', 'c'],   # Row 0 
          ['d', 'e', 'f'],   # Row 1
          ['g', 'h', 'i']]   # Row 2
matrix[1].remove('e')
print(matrix)                    # Output --> [['a', 'b', 'c'], ['d', 'f'], ['g', 'h', 'i']]

# Task: Remove the first item from the last row in the matrix
matrix[-1].pop(0) 
print(matrix)                    # Output --> [['a', 'b', 'c'], ['d', 'f'], ['h', 'i']]
#-----------------------------------------------------------------------------------------------
# Update Items
# list_name[index] = New_Value

letters = ['a', 'b', 'c']
letters[0] = 'x'
print(letters)         # Output --> ['x', 'b', 'c']

letters[1] = 'y'
print(letters)         # Output --> ['x', 'y', 'c']

# Caution
letters = ['a', 'b', 'c']
letters = 'z'          # Without indexing !
print(letters)         # Output --> z
print(type(letters))   # Output --> <class 'str'>

# For Matrix
matrix = [['a', 'b', 'c'],   # Row 0 
          ['d', 'e', 'f'],   # Row 1
          ['g', 'h', 'i']]   # Row 2

# Update the content of the last list
matrix[-1] = ['x', 'y', 'z']
print(matrix)         # Output --> [['a', 'b', 'c'], ['d', 'e', 'f'], ['x', 'y', 'z']]

# Update the first value of the first list
matrix[0][0] = '-'
print(matrix)         # Output --> [['-', 'b', 'c'], ['d', 'e', 'f'], ['x', 'y', 'z']]
#-------------------------------------------------------------------------------------
# How To Sort?
# Changing the order of the items inside the list

# Task: Sort the list in Ascending order
"""
.sort()
- Method that sorts data ASC (From lowest to highest) by default
.sort(reverse=True)
- With this argument it will sort DESC (From highest to lowest)
"""
letters = ['c', 'a', 'b']
letters.sort()
print(letters)         # Output --> ['a', 'b', 'c']

letters = ['c', 'a', 'b']
letters.sort(reverse = True)
print(letters)         # Output --> ['c', 'b', 'a']

numbers = [5, 3, 6, 8, 9, 1, 4, 10]
numbers.sort(reverse = True)
print(numbers)         # Output --> [10, 9, 8, 6, 5, 4, 3, 1]

# For Matrix
"""
- Python sorts by the first item in each inner list!
- If They both started with the same item
  python will go and check the second item
  
  """
matrix = [
          ['g', 'h', 'i'],
          ['d', 'e', 'f'],
          ['a', 'b', 'c']
]
matrix.sort()
print(matrix)         # Output --> [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

# Toi sort specific row
matrix[1].sort(reverse = True)
print(matrix)         # Output --> [['a', 'b', 'c'], ['f', 'e', 'd'], ['g', 'h', 'i']]

"""
.sort()
- It changes the original list 

sorted()
- Function that make a sorted COPY 
  without changing the original list!
"""
# Task: Sort the data without changing the original list
numbers = [5, 3, 6, 8, 9, 1, 4, 10]
new_list = sorted(numbers)
print(numbers)                # Output --> [5, 3, 6, 8, 9, 1, 4, 10]  --> Original list still unchanged
print(new_list)               # Output --> [1, 3, 4, 5, 6, 8, 9, 10]  --> ASC

new_list = sorted(numbers, reverse = True)
print(new_list)               # Output --> [10, 9, 8, 6, 5, 4, 3, 1]  --> DESC
#------------------------------------------------------------------------------------------------------
# Reversing List
"""
If you don't care about the data itself 
Only you want to flip the list around!
.reverse()
 - Method that flips everything around
 - No sorting logic is involved, Just reversing
 - It changes the original list
 
reversed()
 - Function
 - Creates an iterator object, not a list!! --> Will be explained later
"""
letters = ['a', 'b', 'c', 'd']
letters.reverse()
print(letters)                      # Output --> ['d', 'c', 'b', 'a']

numbers = [1, 2, 3, 4, 5, 6, 7]
new_list = reversed(numbers)
print('Original_list:', numbers)    # Output --> Original_list: [1, 2, 3, 4, 5, 6, 7]
print('Reversed list:', new_list)   # Output --> Reversed list: <list_reverseiterator object at 0x000002A963A00130>

new_list = list(reversed(numbers))  # To convert the iterator_object into a list
print('Reversed list:', new_list)   # Output --> Reversed list: [7, 6, 5, 4, 3, 2, 1]
#-----------------------------------------------------------------------------------------------------------------
# How to copy a list?
"""
The Most Important Q is
Are you making a reference to the original data or a new copy?
"""
# Task: Create a copy of the list in a new variable
"""
Assignment = , of the original copy into a new variable
- It is a reference to the original not a new copy!
- If you change an item in the new variable it will be changed in the original
  as they are two variables pointing to the same list
- It is risky 
"""
letters = ['a', 'b', 'c']
letters_copy = letters
letters_copy.append('x')
# Both variables reference the same list in the memory
print('Original:', letters)    # Output --> Original: ['a', 'b', 'c', 'x']
print('Copy:', letters_copy)   # Output --> Copy: ['a', 'b', 'c', 'x']
#-------------------------------------------------------------------------
"""
Shallow Copy
.copy()
- Method that creates a new copy from the original list
- Each variable is pointing to its own list
"""
letters = ['a', 'b', 'c']
letters_copy = letters.copy()

letters_copy.append('x')
letters.pop()
# Each variable is pointing to its own list in the memory
print('Original:', letters)    # Output --> Original: ['a', 'b']
print('Copy:', letters_copy)   # Output --> Copy: ['a', 'b', 'c', 'x']
#-------------------------------------------------------------------------
# Deep Copy
"""
- In leveled data like matrix lists
- .copy()
  creates a shallow copy!
  it will make a copy from the first level (Top Level) of objects only!
  like here the level of object names but still pointing
  to the same data!!
  So, any change in the copied list will also applied to the original 
  as they are pointing to the same list behind the scenes 

- How to Fix This (Make the copy Deeper)  
  We need to get extra help through Copy Module! --> import copy
  Inside Copy Module we have two functions:
      - copy()
        copy.copy()  It is a SHALLOW COPY !! only copy the top level just like the method .copy()
        It is more general than list.copy(), not limited to lists
      - deepcopy()
        copy.deepcopy() creates a true, independent copy for all levels no matter how nested the list
  Syntax:
  Module_name.Function_name(Target list)    
"""

matrix = [
          ['a', 'b'],
          ['c', 'd']
]
matrix_copy = matrix.copy()
matrix.pop()
matrix_copy[0].append('z')                                    
print('Original:', matrix)   # Output --> Original: [['a', 'b', 'z']]
print('Copy:', matrix_copy)  # Output --> Copy: [['a', 'b', 'z'], ['c', 'd']]

# XXX Why both lists Changed ???? XXX

matrix = [
          ['a', 'b'],
          ['c', 'd']
]
import copy
matrix_copy = copy.deepcopy(matrix)
matrix.pop()
matrix_copy[0].append('z') 
print('Original:', matrix)   # Output --> Original: [['a', 'b']]
print('Copy:', matrix_copy)  # Output --> Copy: [['a', 'b', 'z'], ['c', 'd']]

matrix = [
          ['a', 'b'],
          ['c', 'd']
]
matrix_copy = copy.copy(matrix)
matrix.pop()
matrix_copy[0].append('z')                                
print('Original:', matrix)   # Output --> Original: [['a', 'b', 'z']]
print('Copy:', matrix_copy)  # Output --> Copy: [['a', 'b', 'z'], ['c', 'd']]
#-------------------------------------------------------------------------------------------------------------
# Testing - Is Operator
# Is Operator --> Checks if two variables refer to the same object 
# Tip: Use is operator to check if the copies are truly independent
original = [
          ['a', 'b'],
          ['c', 'd']
]
# Assignment
copy1 = original
print('Same Object?', original is copy1)        # Output --> Same Object? True True  (Both of them are referencing the same object)

# Shallow Copy
copy2 = original.copy()
print('Same Object?', original is copy2)        # Output --> Same Object? False
print('Shared list?', original[0] is copy2[0])  # Output --> Shared list? True      (To check the low levels)

# Deep Copy
copy3 = copy.deepcopy(original)
print('Same Object?', original is copy3)        # Output --> Same Object? False
print('Shared list?', original[0] is copy3[0])  # Output --> Shared list? False 

"""
How to Copy?
• Avoid Assignment = (Risky Confusing)
• Use Copy for simple, flat lists
• Use Copy, deepcopyO for Nested lists
• Always make extra Copy for Experiments/ Tests
"""
#------------------------------------------------------------------------------------------------------------
# How to Combine ?
"""
- Using +

- Multiplier Operator
    Makes Multiple copies of the same list

- Create a nested list

- .extend()
  Method that add a list inside another!  
  it doesn't create a new list, it expands the original one!! 

- zip()
  Function that takes 1st item from the 1st list with the 1st item from the 2nd list ...& So On
  Pairing !
  Output: List of tuples --> [(Pair1), (Pair2), ...etc]  
  Python will stop pairing at the shortest list!!
  Actual output of the zip() will be an iterator
  so --> list(zip()) --> To get a listed output
"""
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = letters + numbers
print(comb)             # Output --> ['a', 'b', 'c', 1, 2, 3]
print(letters * 2)      # Output --> ['a', 'b', 'c', 'a', 'b', 'c']  # Multiply

# Combined but Separated!!
comb2 = [letters, numbers]
print(comb2)            # Output --> [['a', 'b', 'c'], [1, 2, 3]] 

# .extend()
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
numbers.extend(letters)
print(letters)          # Output --> ['a', 'b', 'c']
print(numbers)          # Output --> [1, 2, 3, 'a', 'b', 'c']

# zip()
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = zip(letters, numbers)
print(comb)                       # Output --> <zip object at 0x000001468D226040>
print(list(comb))                 # Output --> [('a', 1), ('b', 2), ('c', 3)]

letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4,5 ,6 ,7 ,8]
comb2 = list(zip(letters, numbers))
print(comb2)                      # Output --> [('a', 1), ('b', 2), ('c', 3)] --> Stopped at the shortest list

# You can combine them with a string !
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb3 = list(zip(letters, numbers, "Hi"))
print(comb3)                      # Output --> [('a', 1, 'H'), ('b', 2, 'i')] --> Stopped at the shortest list 

# Task: Pair customers with their IDs (Rebuild the relationship)
ids = [101, 102, 103]
names = ['Ali', 'Sara', 'John']
print(ids + names)                # Output --> [101, 102, 103, 'Ali', 'Sara', 'John'] XXX --> No Sense
print(list(zip(names, ids)))      # Output --> [('Ali', 101), ('Sara', 102), ('John', 103)]
#-------------------------------------------------------------------------------------------------------------
# How to Iterate?
# Python Iterator VS Iterable
"""
Why do we even need Iterators?
  - In order to build a loop!
  - To save memory
    As it produce values one by one upon requesting
    Golden for big data streams 
  - Speed 7 Flexibility
    you can build a real pipelines that 
    can transform the data on the fly!
    without need them to be stored somewhere

Diff between Iterator and Iterable:
  Iterator:
  - An object that help us to do the Iteration
  - It is the engine or the machine


  Iterable:
  - The thing that we can loop over 
    Ex: list --> Has items and we can loop through it
    So as string
    But Boolean?, Integer 565324? XXX
  - Sequence of items 
"""

letters = ['a', 'b', 'c']
for l in letters:
    print(l)
"""
Output:
a
b
c
"""
# letters = 21540452
# for l in letters:
#     print(l)      XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX 
"""
Output: TypeError: 'int' object is not iterable XXX
"""
# We use iteration to transform data
# Make the list items --> in Uppercase
letters = ['a', 'b', 'c']
for l in letters:
    print(l.upper())
"""
Output:
A
B
C
"""    
# Task: Store the transformed results in a new list
letters = ['a', 'b', 'c']
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)
"""
Output:
['A']
['A', 'B']
['A', 'B', 'C']
""" 
#------------------------------------------------------------------------
# enumerate()  reversed()  zip()
"""
enumerate()
  - Iterable
  - Built-in function
  - Returns Position Nr + Value
  - Syntax
    enumerate(Iterable value, start = Index) --> Zero indexed --> Start = 0 By default
"""
letters = ['a', 'b', 'c']
print(enumerate(letters))
# Output: <enumerate object at 0x0000022E4321CF40>
#           Iterator type        Memory address
print(list(enumerate(letters)))
# Output: [(0, 'a'), (1, 'b'), (2, 'c')]
print(list(enumerate(letters, start = 1)))
# Output: [(0, 'a'), (1, 'b'), (2, 'c')]

# Used in Looping
letters = ['a', 'b', 'c']
for index, value in enumerate(letters):
    print(index, value)
"""
Output:
0 a
1 b
2 c
""" 
# Enumerate Use Case:
#    Find the exact position of the bad data in your list
letters = ['a', '', 'c']
for index, value in enumerate(letters):
    print(index, value)
"""
Output:
0 a
1 
2 c
""" 
#----------------------------------------------------------------------------
# reversed()
"""
- Function 
- Returns an object Iterator
- Returns an iterator that flips the data order
- Syntax:
  reversed(iterable value)
"""
letters = ['a', 'b', 'c']
print(list(reversed(letters)))   # Output: ['c', 'b', 'a']

for l in reversed(letters):
    print(l)
"""
Output:
c
b
a
"""
#-------------------------------------------------------------------------------
# zip()
"""
- Function 
- Combine two or more sequences into pairs (tuples)
- Returns an object Iterator
- Syntax:
  zip(Seq1, Seq2)
"""
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
print(list(zip(letters, numbers))) # Output: [('a', 1), ('b', 2), ('c', 3)]
for pair in zip(letters, numbers):
    print(pair)
"""
Output:
('a', 1)
('b', 2)
('c', 3)
"""
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
for l, n in zip(letters, numbers):
    print(l, n)
"""
Output:
a 1
b 2
c 3
"""
#-----------------------------------------------------------------------------------
# Iterator Map()
"""
- Function
- Returns an object Iterator
- Syntax:
  map(Function, Iterable)
- map() is fast, clean way to do data transformations  
"""
# Task: Make every letter uppercase
letters = ['a', 'b', 'c']
for l in letters:
    print(l.upper())
"""
Output:
A
B
C
"""
# List ?
letters = ['a', 'b', 'c']
up_list = []
for l in letters:
    up_list.append(l.upper())
    print(up_list)
"""
Output:
['A']
['A', 'B']
['A', 'B', 'C']
"""
# Smarter map() ?
letters = ['a', 'b', 'c']
print(list(map(str.upper, letters))) # Output: ['A', 'B', 'C']

# Task: Convert list items to integers
numbers = ['1', '2', '3']
print(list(map(int, numbers)))       # Output: [1, 2, 3]

# Task: Clean up the list by removing all unwanted spaces
names = ['  Maria  ', 'John   ', '  Peter']
print(list(map(str.strip, names)))   # Output: ['Maria', 'John', 'Peter']

# in a for loop?
names = ['  Maria  ', 'John   ', '  Peter']
for name in map(str.strip, names):
    print(name) 
"""
Output:
Maria
John
Peter
""" 
#-----------------------------------------------------------------------------------
# Iterator filter()
"""
- Function
- Returns an object operator
- Syntax:
  filter(Function , Iterable)
- filter(None, Iterable)
  it will remove all falsy values like 0, '', or False 
- filter(None, Iterable) 
  it will also remove all falsy values like 0, '', or False 
- It is perfect for cleaning up data in our structures  
"""
# Task: Clean up the list by removing un-valid data
letters = ['a', '', 'b', None, 'c', 0, False]
print(list(filter(None, letters)))       # Output: ['a', 'b', 'c']

letters = ['a', '', 'b', None, 'c', 0, False]
print(list(filter(bool, letters)))       # Output: ['a', 'b', 'c']

# Task: Keep only letters (alphabetic) items
items = ['sql', '123', 'python', '42']
print(list(filter(str.isalpha, items)))  # Output: ['sql', 'python']

for i in filter(str.isalpha, items):
    print(i)
"""
Output:
sql
python
"""
#----------------------------------------------------------------------------------------
# Lambda Functions
"""
- Used to create quick & custom logic
- Is also called Anonymous Function
- You can define a whole function within one line
- Syntax
  lambda(Input Value or variable): Expression
"""

# Ex: Variable multiple store a lambda function which doubles a number
multiple = lambda x: x * 2  # --> Defining the function!
print(multiple(5))          # --> We treat the variable as a function!
                            # Output: 10

# Ex: When a lambda has two parameters, you must pass two values when calling it!
add = lambda x, y: x + y
print(add(10, 2))           # Output: 12

# Lambda can contain any expression, including conditions
check = lambda i: i in "Python"
print(check("n"))           # Output: True
print(check("x"))           # Output: False
#--------------------------------------------------------------------------------
# Lambda + Map
# map(lambda variable: Expression, iterator)
# Task: Prices are stored as messy strings and need cleaning to floats
prices =['$12.50', '$9.99', '$100.00']
# Think about it step by step
# First we need to remove the $ before converting into float!
p = '$100'
print(p.replace('$', ''))                                         # Output: 100    --> str
# Convert to float
print(float(p.replace('$', '')))                                  # Output: 100.0  --> float
# Apply to the list
print(map(lambda p: float(p.replace('$', '')), prices))           # Output: <map object at 0x00000174ABB23400>  --> Object Iterator
# To show a list
print(list(map(lambda p: float(p.replace('$', '')), prices)))     # Output: [12.5, 9.99, 100.0]

"""
[1]- Data Transformation
[2]- Put in lambda
[3]- Map the function to iterator to manipulate my data
"""
#--------------------------------------------------------------------------------
# Lambda + Filter
# filter(lambda variable: Expression, iterator)
# Task: Remove all prices lower than 100
prices = [120, 30, 300, 80]

# Which logic?
# price >= 100
lambda p: filter(p >= 100)
print(list(filter(lambda p: p >= 100, prices)))        # Output: [120, 300]

# Ex:
# Task: Keep only students with scores higher than 70
# Note: Matrix iteration happens one row at a time
students = [['Maria', 85],
            ['Peter', 90],
            ['Max', 60]]
# Build the Logic !
print(students[0][1] > 70)                              # Output: True
# Put the function into lambda
lambda row: row[1] > 70
# Apply to the list using filter()
print(list(filter(lambda row: row[1] > 70, students)))           # Output: [['Maria', 85], ['Peter', 90]]

# Challenge:
"""
Keep only students with names starting with'M'
students = [['Maria', 85],
            ['Peter', 90],
            ['Max', 60]]
"""
# Answer:
students = [['Maria', 85],
            ['Peter', 90],
            ['Max', 60]]
# print(students[0][0].startswith('M')) --> Output: True
print(list(filter(lambda row: row[0].startswith('M'), students))) # Output: [['Maria', 85], ['Max', 60]]
#-------------------------------------------------------------------------------------------------------
# Lambda + sorted() ??
# sorted(Iterable)
# sorted(Iterable, reversed = True)
# sorted(Iterable, Key = lambda) ?????!!!!
"""
Lambda Function
  - Creates quick &  Custom Logic
  - One-lined Function
  - Assist Others:
      map(lambda, iterable)
      filter((lambda, iterable))
      sorted(Iterable, Key = lambda)
  - Add dynamic & Flexibility    
"""
#--------------------------------------------------------------------------------------------------------
# List Comprehension
"""
- Advanced concept
- To Put all in one line (Loops, Transformation, Filtering)
- There is no function or Method for comprehension 
- Instead --> Build three blocks:
              [1]- Data Transformation (Expression)
              [2]- Loop
              [3]- Filter (Using If condition), (Filtering is Optional)
"""
# Ex:
# Task: Normalize the domains into standard format

domains = ['www.google.com',
           'openai.com',
           'localhost',
           'WWW.DATAWITHBARAA.COM']

"""
Concept:
cleaned = [
    - Data Transformation
    - For Loop
    - Data filtering
]
"""
cleaned = [
    d.lower().replace('www.', '')
    for d in domains
    if '.' in d
]
print(cleaned)      # Output: ['google.com', 'openai.com', 'datawithbaraa.com']

"""
- Only filtering: Using only the variable name means no transformation !!
cleaned = [
    d
    for d in domains
    if '.' in d
] 
print(cleaned)      # Output: ['www.google.com', 'openai.com', 'WWW.DATAWITHBARAA.COM']

You can:
   - Data Transformation + Filtering
   - Only Data Transformation
   - Only filtering
"""