import pandas as pd

# Set the dataframe df
df = pd.DataFrame({
        'Fruit': ['Apple', 'Banana', 'Strawberry', 'Blueberry', 'Mango', 'Pear', 'Cherry'],
        'Aisle': [1, 1, 2, 2, 3, 3, 2],
        'Shelf': ['A', 'B', 'C', 'D', 'E', 'A', 'D'],
        'n': [50, 25, 15, 12, 45, 5, 8]
})

print('Data')
print(df.head())
print()

# select columns by name
sel = df.filter(items=['Fruit', 'n'])
print(sel)
print()

# Select column by index
sel_index = df.iloc[:, [0, 3]]
print('Select column by index')
print(sel_index)
print()

# select
print('select fruits that start with the letter b')
sel_b = df[df.Fruit.str.startswith('B')]
print(sel_b)
print()

# Select fruits that contain 'berry'
sel_berry = df[df.Fruit.str.contains('berry')]
print('Select fruits that contain "berry"')
print(sel_berry)
print()

# Select fruits that not starts with the letter 'B'
print('Select fruits that not starts with the letter "B"')
sel_not_b = df[~df.Fruit.str.startswith('B')]
print(sel_not_b)
print()

# The isin method is another way of applying multiple condition for filtering.
names = ['Apple', 'Mango']
sel_by_name = df[df.Fruit.isin(names)]
print('Select by names')
print(sel_by_name)
print()

# Query
print('Query')
query = df.query('Fruit == "Apple" and Fruit == "Cherry"')
print(query)
print()

# Get the two biggest numbers in column 'n'
highest_num = df.nlargest(2, 'n')
print('Highest Numbers in the data frame')
print(highest_num)
print()

# get the two smallest numbers in column 'n'
smallest_num = df.nsmallest(2, 'n')
print('Smallest Numbers in the data frame')
print(smallest_num)

#