"""
Sets
- Unordered collection of unique values
- Very fast
- Syntax:
  set_name = { ,  ,  ,}

Data structure     Ordered     Allow duplicates     Indexed     Mutable  
Set {}             No          No (Auto-Removed)    No          yes
  
"""
my_set = {10, 30, 20, 10}
print(my_set)      # Output: {10, 20, 30}  diff order than the defined    --> Un-Ordered, No Duplicates allowed
# print(my_set[1])   # Output: TypeError: 'set' object is not subscriptable --> Not Indexed
my_set.remove(20)    
print(my_set)        # Output: {10, 30}                                     --> Mutable
#-------------------------------------------------------------------------------------------------------------
# Special Methods & Operators for the Sets
# Set Methods
"""
- Index-Based methods do not work with Sets
  like .append()
"""
# Add Item?

# .add() --> Insert the item somewhere in the set, bu\t only if it is new
a = {10, 20, 30, 40}
a.add(50)
print(a)                # Output: {40, 10, 50, 20, 30}
a.add(20)
print(a)                # Output: {40, 10, 50, 20, 30} --> No Change        

# .update() --> Merges another group of values (Iterable) into the set
a.update("Hi")         
print(a)                # Output: {'H', 40, 10, 'i', 50, 20, 30}
a.update([1, 2, 3])    
print(a)                # Output: {1, 2, 3, 'H', 40, 10, 'i', 50, 20, 30}

# Using math operators as quick shortcuts: |&-^
b = {10, 20, 30, 40}
# |= Works like update for the sets
b |= {1, 2, 3}
print(b)                # Output: {1, 2, 3, 20, 40, 10, 30}

# Remove values from a set
b.remove(10)
print(b)                # Output: {1, 2, 3, 20, 40, 30}

# b.remove(100)
print(b)                # Output: KeyError: 100  --> Will stop the whole block --> not safe
# .pop()     --> removes and returns a random item from a set

# .discard() --> Removes the item if it exists and does nothing if it doesn't
b = {10, 20, 30, 40}
b.discard(10)
print(b)                # Output: {40, 20, 30}
b.discard(10)
print(b)                # Output: {40, 20, 30} --> Nothing happened, No Error
#-------------------------------------------------------------------------------------------------------------
# Set Math Methods
"""
Tools or methods used to differentiate between sets: --> For Comparison
  - .union()
  - .intersection()
  - .difference()
  - .symmetric_difference()
Math Operators return a new set and leave the original untouched!!
"""
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

# .union() --> Combines ALL unique items from both sets
print(a.union(b))         # Output: {40, 10, 50, 20, 60, 30} --> Removed duplicates (Unique Only) 
print(a | b)              # Output: {40, 10, 50, 20, 60, 30} --> Equal to .union()

# .intersection() --> Returns only the shared items
print(a.intersection(b))  # Output: {40, 30}
print(a & b)              # Output: {40, 30} --> Equal to .intersection()

# .difference() --> Items that belongs only to the first group
# Items only appear in the first list but doesn't overlap with the second list
print(a.difference(b))   # Output: {10, 20}  --> 10, 20 are in a but not in b
print(a - b)             # Output: {10, 20}  --> Equal to .difference()
print(b - a)             # Output: {50, 60}

# .symmetric_difference --> Returns only the Non-shared items  
print(a.symmetric_difference(b))    # Output: {10, 50, 20, 60}
print(a ^ b)                        # Output: {10, 50, 20, 60} --> Equal to .symmetric_difference()
#-------------------------------------------------------------------------------------------------------------
# Set Relationship Methods
"""
- Relationship question?  - True  - False

.issubset()   --> Returns True if ALL items in this set exists in the other
.issuperset() --> Returns True when it includes ALL items of the other set
.isdisjoint() --> Returns True if both sets share no items (No Overlapping)
"""

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
print(a.issubset(b))      # Output: False --> Not all items of A exist in B

a = {10, 20, 30, 40}
b = {30, 40, 50, 60, 10, 20}
print(b.issuperset(a))    # Output: True  --> B includes all items of A
print(a.isdisjoint(b))    # Output: False --> There is Overlapping between the 2 sets