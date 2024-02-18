# Python basics
x = 2
y = 5
# Addition
z = x + y
print(z)

# Augments Assignment operator
# Addition and assignment
x =+ y     # Equivalent to:  x = x + y

# subtraction and Assignment
x -= y      # Equivalent to: x = x - y

# multiplication and assignment
x *= y      # Equivalent to: x = x * y

# Division and assignment
x /= y      # Equivalent to: x = x/y

# greeting = 'Hello'
# greeting += ' World!'
# print(greeting)
#
# number = 1
# number += 1
# print(number)
#
# my_list = ["Item"]
# my_list *= 3
# print(my_list)
#
#
# # Concatenation and Replication
# # String Concatenation
# gname = 'Alice'
# bname = 'Bob'
# couple_name = gname +" "+ bname
# print(couple_name)
#
# # String Replication
# rep = gname * 5
#
# print(rep)

# Python Basics
# the input() function
print('what is your name?')   # asking user input
my_name = input()
print('Hi,  {}'.format(my_name))

# Input can also set a default message without using the print()
my_names = input('What is your name? ') # default message
print('Hi, {}'.format(my_names))

# its is also possible to use formatted strings to avoid using.format
my_namee = input('What is your name? ')  # defaul message
print(f'Hi, {my_namee}')


# Built-In Function
# abs() - return the absolute value of a number
# abs(-2)
#
# # Comparison operator
# 42 == 42  # Equal to
# 40 != 32 # Not equal to
# 20 < 23 # Less than
# 45 > 12 # Greater than
# 20 <= 24 # Less or equal to
# 23 >= 20 # Greater or equal to

# Boolean operators

# if statements

jina = 'Debora'

if jina == 'Debora':
    print('Hi, {}'.format(jina))

if jina != 'George':
    print('You are not George')

# the else statement executes only if the evaluation of the if and all the elif expressions are false

name = 'debora'

if name == 'george':
    print('Hi, {}'.format(name))
else:
    print('You are not George')

# only after the if statement expression is false the elif statement is evaluated and executed

name = 'George'

if name == 'Debora':
    print('Hi, Debora')
elif name == 'George':
    print('Hi, {}'.format(name))

# The elif and else part are optional

name = 'Antony'

if name == 'Debora':
    print('Hi, Debora!')
elif name == 'George':
    print('Hi, George')
else:
    print('Hi, Antony')


# Ternary Conditional Operator
age = 15

# this if statement
if age < 18:
    print('kid')
else:
    print('adult')

# is equivalent to this ternary statement
# A ternary statement offers one line code to evaluate the first expression if the condition is true,
# otherwise it evaluates the second expression.
print('kid' if age < 18 else 'adult')

age = 15

# ternary operators can be chained

print('kid' if age < 13 else 'teen' if age < 18 else 'adult')

# It is equivalent to this if statement
if age < 18:
    if age < 13:
        print('kid')
    else:
        print('teen')
else:
    print('adult')

# While loop statements
spam = 0
while spam < 5:
    print('Hello, world!')
    spam += 1

    





