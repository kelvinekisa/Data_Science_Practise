# COLLECTION DATA TYPES

#  Python Lists
names = ['John', 'peter', 'Debora', 'Charles']

print(names)

# Getting values with indexes
print(names[0])
print(names[2])
print(names[2])

# Negative indexes
print(names[-2])
print(names[1])

# Getting sublists with slices
print(names[0:2])

# Slicing the complete list will perform a copy

names_1 = names[:]
print('The copied list is: ', names_1)

# Adding values using append
names_1.append('Moses')

# Changing values with indexes
names[2] = 'Paul'
names[-1] = 'Ken'
print('The added names are: ', names)

# concatenation and replication
num = [1, 2, 1, 5]
num1 = [5, 6, 8, 9]
num3 = num + num1
print(num3)
print(num * 3)


# using loops with lists

furniture = ['Table', 'Chair', 'Rack', 'Shelf']

for item in furniture:
    print(item)

# Getting the indexes in a loop with enumerate()
for index, item in enumerate(furniture):
    print(f'index: {index} - item: {item}')


# Loop in multiple lists with zip()
utensils = ["Plate", 'Cups', 'Spoons', 'Dishes']
price = [100, 250, 50, 12]

for item, amount in zip(furniture, price):
    print(f'The {item} costs ${amount}')


# The multiple assignment trick

# print("The multiple assignment trick")
# schools = ['TUK', 'Musingu', 'Nairobi', 'Meru']
# Tuk = schools[0]
# Musingu = schools[1]
# Nairobi = schools[2]
# Meru = schools[3]
#
# print(schools)

# adding values
# "Append" adds an element  to the end of a list 'list':
furniture.append('bed')
print(furniture)

# insert() - 'insert' adds an element to a list ata given position;
furniture.insert(1, 'bed')
print(furniture)

# Removing values


