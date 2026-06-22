"""
Each data structure behaves differently
  - Lists --> Everything allowed
  - Tuple --> Frozen
  - Set   --> Unique
  - Dict  --> Mapping

Categories:
  - Ordered
    Python cna remember the exact position of every value 
    Nothing changed until changed by you!
  - Allow duplicates
    You can store the same value more than once
    Repetition!
  - Indexed
    You can access the value directly using their position number 
  - Mutable  
    After creation you can change add, replace, remove, ...etc

Data structure     Ordered     Allow duplicates     Indexed     Mutable  
List []            yes         yes                  yes         yes
Tuple ()           yes         yes                  yes         No                                             
"""
my_list = [10, 20, 30, 10]
print(my_list)      # Output: [10, 20, 30, 10] --> Ordered, Allow duplicates 
print(my_list[2])   # Output: 30               --> Indexed
my_list[3] = 40
print(my_list)      # Output: [10, 20, 30, 40] --> Mutable
#---------------------------------------------------------------------------
# Data structure: Tuple
"""
- Tuple is an ordered collection that cannot be changed after creation
- Locked or frozen for safety reasons
- Syntax:
  tuple_name = ( ,  ,  ,)
"""
my_tuple = (10, 30, 20, 10)

print(my_tuple)          # Output: (10, 30, 20, 10)                                           --> Ordered, Allow duplicates 
print(my_tuple[2])       # Output: 20                                                         --> Indexed
my_tuple[3] = 40
print(my_tuple)          # Output: TypeError: 'tuple' object does not support item assignment --> Immutable
 
# Try to use functions with a tuple!
print(sorted(my_tuple))  # Output: [10, 10, 20, 30] ==> It is a LIST!
# Use tuples in each time you feel that the data must be protected!