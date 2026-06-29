# Day 3: Variables and Data Types

# Variables
name = "Alice"
age = 30
height = 5.8
is_student = True

# Data Types
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student)) # <class 'bool'>

# multiple assignment
a,b,c = 10,20,30
print(a,b,c)  # 10 20 30

# naming rules for variables
# - Variables must start with a letter or underscore
# - Variables cannot start with a number
# - Variables can only contain alphanumeric characters and underscores
# - Variables are case-sensitive

# swap without temp variable
a,b = 10 , 20
a,b =b,a
print(a)
print(b)