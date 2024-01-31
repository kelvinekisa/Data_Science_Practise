import pandas as pd

# Creating a pandas dataframe
# 1. list
lst = ['James', 'Mwangi', 'Pombe', 'maina', 'Clement', 'Jair', 'joshua', 'Ambani']

# Calling dataframe constructor on list
# df = pd.DataFrame(lst)
# print(df)

# creating dataframe from dict of ndarray/list:

# initialize data of lists.
data = {'Name': ['Tom', 'Nick', 'Krish', 'Jack'],
        "Age": [20, 21, 19, 18]}

# Create dataFrame
df = pd.DataFrame(data)

print(df)

# Dealing with rows and columns
# Define a dictionary containing employee data
data = {'name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert The dictionary into a dataframe
df = pd.DataFrame(data)

# Select two columns
print(df[['name', 'Qualification', 'Age']])

# using nba.csv file (Downloaded)
# making data frame from a csv file
dataa = pd.read_csv("/home/kelvinnr/Downloads/nba.csv", index_col='Name')

# Retrieving row by loc method
first = dataa.loc['Avery Bradley']
second = dataa.loc["R.J. Hunter"]

print(first, "\n\n\n", second)
print(dataa)

# working o rows and columns using pandas
# To select a column in Pandas dataframe we can either acces te columns by calling
# them by their ccolumn name.
# Select two columns
print(df[['name', 'Qualification', 'Age']])

# Adding a column in an existing dataframe.
# define a dictionary containg students data
students = {'Name': ['jai', 'Princi', 'Guarav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Mcs', 'MA', 'Msc', 'Msc']}

# convert the dictionary into a dataframe
df = pd.DataFrame(students)

# declare a list that is to be converted into a column
address = ['Delhi', 'Bangalore', 'Channai', 'Patna']

# using "Address" as the column name and equating it to the list
df['Address'] = address

print(df)


