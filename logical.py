# LOGICAL OPERATORS
# Used to perform operations on values and variables. They are used on conditional statements.
# Logical AND operator. Returns True if both the operands are True else it returns False.
# a = 10
# b = 10
# c = -10
# if a > 0 and b > 0:
#     print("The numbers are greater than 0")
# if a > 0 and b > 0 and c > 0:
#     print("The numbers are greater than 0")
# else:
#     print("Atleast one number is not greater than 0")
#
#
# # Logical OR Operator
# # returns True if either of the operands is True.
# x = 10
# y = -10
# z = 0
# if x > 0 or y > 0:
#     print("Either of the number is greater than 0")
# else:
#     print("No number is greater than 0")
# if y > 0 or z > 0:
#     print("Either of the number is greater than 0")
# else:
#     print("No number is greater than 0")


# Logical NOT operator
# Works with a singleboolean value. If the boolean value is True it returns False and vice-versa
j = 100
if not j:
    print("Boolean value of j is True")
elif not (j%3 == 0 or j%5 == 0):
    print("100 is not divisible by either 3 or 5")
else:
    print("100 is divisible by either 3 or 5")


# Order of precedence of logical operators
def order(x):
    print("Method calles for value: ", x)
    return True if x > 0 else False
a = order
b = order
c = order
if a(-1) or b(5) or c(10):
    print("Atleast one of the number is positive")
