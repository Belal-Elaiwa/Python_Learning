"""
Dictionaries:
- Instead of assigning multiple variables
- Dict allows storing different types of data in one place
- Data stored in Key-Value pairs
   - Key describes what the data means
     Keys must be unique, duplicates are not allowed
   - Value holds actual data, duplicates are allowed  
- Syntax:
  {key:value, key:value, key:value, ..etc}   

Data structure     Ordered     Allow duplicates           Indexed           Mutable  
Dict { : ,  : }    Yes         Yes in vals / No in keys   No(It is Keyed)   Yes by key
"""
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 30
}
print(my_dict)       # Output: {'a': 10, 'b': 20, 'c': 30, 'd': 30} --> Ordered, Allows duplicates but in keys or vals ?

my_dict2 = {
    'a': 10,
    'b': 20,
    'c': 30,
    'a': 30
}
print(my_dict2)  
# Output: {'a': 30, 'b': 20, 'c': 30}                                  --> Removed duplicates!
# So, Allows duplicates in values but not allowed in keys!1
#print(my_dict[1])    # Output: KeyError: 1                            --> Not indexed  
print(my_dict['b'])   # Output: 20                                     --> Dict is keyed 
my_dict['a'] = 50
print(my_dict)        # Output: {'a': 50, 'b': 20, 'c': 30, 'd': 30}   --> Mutable
#---------------------------------------------------------------------------------------------
# Dict Methods (Special Methods & Operators for Dict)

user = {"id": 1, "age": 30, "city": "Berlin"}

# Access
print(user["city"])                  # Output: Berlin

"""
If the key is missing?
If the key is not found Python through a key error --> Not Safe
-- > print(user["name"])             # Output: KeyError: 'name' XXX
get() -->  Method Returns the value safely, gives None if missing
"""
print(user.get("name"))              # Output: None

# Missing Key returns None or your default value
print(user.get("name", "Unknown"))   # Output: Unknown As a default value

# Checks
# in operator --> Tests if the key is inside the dictionary
print("age" in user)                # Output: True
print("name" not in user)           # Output: True

# Special Methods for Dict
"""
View Objects --> Give you a live view of the Dict's keys, values, or key-value pairs
 - .keys()
   Returns all the KEYS in your dictionary
 - .values()
   Returns all the VALUES in your dictionary
 - .items()
   Returns BOTH the KEYS & VALUES in your dictionary  
   Perfect when you need key and value together
   for looping, transforming data, building new Dicts, comparing and more
"""
print(user.keys())                 # Output: dict_keys(['id', 'age', 'city']) --> Keys without values!
print(user.values())               # Output: dict_values([1, 30, 'Berlin'])   --> Values without keys!
print(user.items())                # Output: dict_items([('id', 1), ('age', 30), ('city', 'Berlin')])   --> Both!

# Looping

user = {"id": 1, "age": 30, "city": "Berlin"}
for u in user:
    print(u)
# Output:
"""
id
age
city
"""    
user = {"id": 1, "age": 30, "city": "Berlin"}
for u in user:
    print(u, user[u])
# Output:
"""
id 1
age 30
city Berlin
"""     

# Modern Way
user = {"id": 1, "age": 30, "city": "Berlin"}
for key, value in user.items():
    print(key, value)
# Output:
"""
id 1
age 30
city Berlin
"""
# Add, Remove, Update
# Assignment for addition or updating
user["name"] = "John"    
print(user)                     # Output: {'id': 1, 'age': 30, 'city': 'Berlin', 'name': 'John'} --> Add

user['age'] = 35
print(user)                     # Output: {'id': 1, 'age': 35, 'city': 'Berlin', 'name': 'John'} --> Update
 
# .update() --> adds new keys and updates existing ones using another dictionary
user.update({"age": 40, "city": "paris"})
print(user)                     # Output: {'id': 1, 'age': 40, 'city': 'paris', 'name': 'John'}

# .pop() --> Removes a key from the dictionary and returns its value Or returns your default value if the key is missing
age = user.pop("age")
print(user)                     # Output: {'id': 1, 'city': 'paris', 'name': 'John'}
print("Removed Item:", age)     # Output: Removed Item: 40

user.update({"age": 40, "city": "paris"})
#salary = user.pop("salary")
#print(user)                       # Output: KeyError: 'salary' XXX
#print("Removed Item:", salary)
#To avoid the key error which will break the entire code
salary = user.pop("salary", "Not Found")
print(user)                        # Output: {'id': 1, 'city': 'paris', 'name': 'John', 'age': 40}
print("Removed Item:", salary)     # Output: Removed Item: Not Found
 
# .pop() --> at least 1 argument 
# user.pop()
# print(user)   # Output: TypeError: pop expected at least 1 argument, got 0 XXX

# .popitem() --> Returns and deletes the most recent key value pair from the dict
user = {"id": 1, "age": 30, "city": "Berlin"}
removed = user.popitem()
print(user)                       # Output: {'id': 1, 'age': 30}
print ("Removed Item:", removed)  # Output: Removed Item: ('city', 'Berlin')

# Creation of new Dict
"""
.fromkeys() --> Method Builds anew dictionary where all keys get the same default value
- .fromkeys([list of the keys], the value)
"""

user = dict.fromkeys(["id", "name", "age", "city"], None)
print(user)                     # Output: {'id': None, 'name': None, 'age': None, 'city': None}
user["age"] = 50
print(user)                     # Output: {'id': None, 'name': None, 'age': 50, 'city': None}
#----------------------------------------------------------------------------------------------
# Challenge
"""
user = {"id": 1, "name": "John", "age": 30, "city": "Berlin" }

1 Create New Dict
2 Keep Only Pairs with String Values
3 Convert Values to Uppercase
4 Elegant f Short Solution!
# """
# print("=" * 150)

# My Try XXX  XXX
# user = {"id": 1, "name": "John", "age": 30, "city": "Berlin" }
# new_dict = {}
# for Key, value in user.items():
#     if type(value) == str:
#         new_dict[key, value] = key, value
# print(new_dict)        

# user = {"id": 1, "name": "John", "age": 30, "city": "Berlin" }
# new_dict = {}

# for u in user:
#     if type(user[u]) == str:
#         new_dict = u, user[u]
# print(new_dict)        

# Answer
# Dict comprehension
# components: Key value expression, a loop, and an optional condition

user = {"id": 1, "name": "John", "age": 30, "city": "Berlin" }
user_str = {
    k: v.upper()             # Expression --> you can manipulate each item!
    for k, v in user.items() # Loop
    if isinstance(v, str)    # filter
}
print(user_str) # Output: {'name': 'JOHN', 'city': 'BERLIN'}
#---------------------------------------------------------------------------
# Dict Real World Applications
#---------------------------------------------------------------------------
"""
- Use Case: Database or API Records
  Returned records are stored as dictionaries where column names are keys
  and the row values are the dictionary values
"""

# Representing a single row from a Database or API
row = {
    "id": 101,
    "name": "John",
    "country": "DE",
    "age": 29,
    "status": "active"
}

"""
- Use Case: Mapping To Friendly Values 
  Great for converting technical codes into friendly labels.
"""
# Mapping Translations to Friendly Values
status_map = {
    "01": "Open",
    "02": "In Progress",
    "03": "Done"
}

"""
- Use Case: Mapping Abbreviations
  Turning short abbreviations into full readable names
"""
country_map = {
    "DE": "Germany",
    "FR": "France",
    "IN": "India"
}

"""
- Use Case: Config and Environment Data
  Store system settings like host, port, and usernames in one clean place.
"""
# Storing Environment Variables & Configuration
system_conn = {
    "DB_HOST": "prod-db.company.com",
    "DB_PORT": 5432,
    "DB_USER": "admin_user",
    "DB_NAME": "analytics_warehouse"
}

"""
- Use Case: ETL and Pipeline Settings
  Great for storing run parameters and controlling how your ETL pipeline loads data
"""
etl_config = {
    "DEBUG_MODE": False,                          # Turn verbose logging on/off
    "BATCH_SIZE": 500,                            # How many rows to process per batch
    "LOG_LEVEL": "INFO",                           # Logging verbosity
    "SOURCE_PATH": "/data/bronze/",                # Where raw files live
    "TARGET_PATH": "/data/silver/",               # Where cleaned files go
    "RETRY_COUNT": 3,                             # How many times to retry a failed extr
    "FAIL_ON_ERROR": False,                       # Keep going or stop the job
    "VALIDATE_SCHEMA": True,                      # Enforce schema che
    "SUPPORTED_FORMATS": ["CsV", "parquet"],      # Allowed file
    "RUN_ENV": "production"                       # dev / test / prod
}

"""
- Use Case: Metadata
  Data About Your Data
"""
# Metadata
table_metadata = {
    "table_name": "customers",
    "columns": {
        "id": {"type": "integer", "nullable": False},
        "name": {"type": "string", "nullable": True},
        "age": {"type": "integer", "nullable": True},
        "country": {"type": "string", "nullable": True}
    },
    "row_count": 105320,
    "file_format": "parquet",
    "last_updated": "2024-10-01T12:45:00Z",
    "partition_by": ["country"],
    "tags": ["pii", "customer-data"],
}