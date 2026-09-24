# This file will cover basic data types in python

# Integers (int):
'''
- can be negative or positive
- there is a finite number but it has a large range

'''

x, y, z = 1, 2, 3
x = 10
y = 3
z = -4

print(x)
print(y)
print(z)

# Float (float):
'''
- floats are real numbers
- can be decimals and/or be negative/positive

'''

x = 3.4
y = 9.99

print(x)
print(y)

# String (str): a sequence of characters
name = 'Bob'
name1 = "Bob"

print(name)
print(name1)
print('This is a string')
print("This is a string")

# Labels
# Equals (=) indicates an assignment

this_variable = this_expression = 3


# In python, no explicit data type, data type is determined by expression format
# To check data type

print(type("Hello"))

# Typecasting
# Changing the type of expression

float(2)
int(2.4) #changing from float to int will lose data by dropping the .4
int('1') #can convert str to int if str is a number, non-numbers will cause an error
str(1) # = '1'
str(2.4) # = '2.4'

type(float(2))

# Boolean
# (Yay boolean math and truth tables!)

isRunning = True
isRunning = False
# type = bool
int(True) #= 1 bool(1)
int(False) #= 0 bool(0)

# Check python.org for other types

# This will give you info like max value for each data type
import sys
print(sys.float_info)
print(sys.int_info)
print(sys.str)