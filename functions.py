# Python functions

# function arguments
def say_hello(name):
    print('Hello {}'.format(name))


say_hello('James')
say_hello('Mercy')
say_hello('Paul')


# Keyword Arguments - Improving code readability
def say_hi(name, greeting):
    print('{}'.format(greeting), '{}'.format(name))


# Without keyword argumenst
say_hi('John', 'Hello')


# With keyword arguments
say_hi(name='Anna', greeting='Hi')


# return values
def sum_two_numbers(num1, num2):
    return num1 + num2


result = sum_two_numbers(7,8)
print(result)


# local and global scope
global_variable = 'I am available everywhere'

def some_function():
    print(global_variable)  # because is global
    local_variable = 'only available within this function'
    print(local_variable)

# the following code will throw error because
# local_variable only exists inside some function

# the following code will throw error because
# local_variable' only exists inside 'some_function'

# print(local_variable)

# The global statement

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

# Functions continuation
def my_address():
    print("kelvin Ekisa")
    print("123 main Street")
    print('Nairobi, Kenya')
    print('Klm jeshi')


my_address()          # calling the function


# Passing argumenst to a function
def personal_data(name):
    print(name)
    print('Nairobi')


personal_data('Kelvin Ekisa')

# Many arguments


def students(name, grade):
    print(name)
    print(grade)
    print('Nairobi')
    print('Kisumu')


students('mercy Chemtai', '5Th grade')


# Functions that return a value
def calculate_tax(price, tax_rate): # function calculates tax and returns total
    tax_total = price + (price * tax_rate)
    return tax_total    # sends results back to the main program


totalprice = calculate_tax(200, 0.045)

print(totalprice)

# Exasperating local and global scope
def test1():
    a = 'local test' # local variabl
    # test2: test2
    test2()
def test2():
    b = 'local test2' # local variable
    print(b)
    test3()
def test3():
    c = 'local test3' # Local variable
    print(c)


x = 'global' # global variable
test1()
print(x)

# Local variable cannot be accessed in a global scope
# code in the global scope cannot use any local variables
# a local scope can access a global variable
# code in a function's local scope cannot use variables in any other local scope
# You can use the same name for different variables if they are in different scopes

print('Exasperating local and global variables')

def test_1():
    a = 'local variable'

def test_2():
    test_1()
    print()

    
test_1()

