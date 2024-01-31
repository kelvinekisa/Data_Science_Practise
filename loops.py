# Python FOR loop
#I terating over a list
names = ["John", "Joy", "James", "Jero", "Moses"]
for i in names:
    print(i)

#Python For loop in dictionaries
print("Dictionary Iteration")

d = dict()

d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))

# Python for loop in string
# print each character on a new line
print("String Iteration")

s = "Geeks"
for i in s:
    print(i)


# Python For Loop with a step size
# This code uses a for loop in conjunction with the range() function to generate a
# sequence of numbers starting from 0, up to (but not including) 10, and with a step
# size of 2. For each number in the sequence, the loop prints its value using the
# print() function.

for i in range(0, 10, 2):
    print(i)


# Nested for loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

print("underatnding this:")
for i in range(1, 4):
    print(i)

