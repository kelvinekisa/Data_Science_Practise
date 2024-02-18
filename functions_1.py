# understanding python functions

# function arguments

# Global variable
global_variable = 'I am global'


def my_function(local_param):
    # local variable
    local_variable = 'I am local'

    # Accessing global and local variables
    print(global_variable) # Accessing global variable
    print(local_param) # Accessing function parameter
    print(local_variable) # Accessing local variable

# calling the function with values


my_function('I am an argument')

# Example 2


def say_hello(name):
    print('Hello {}'.format(name)) # {} placeholder


say_hello('Kelvin')


# Keyword Arguments
def say_hi(name, greeting):
    print('{}'.format(name), '{}'.format(greeting))


say_hi(name='Anna', greeting='Hi')

# return values

def sum_two_numbers(num1, num2):
    return num1 + num2


result = sum_two_numbers(7, 8)
print('The sum: ', result)
