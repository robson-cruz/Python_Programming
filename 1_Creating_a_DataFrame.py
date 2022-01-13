# import Library
import pandas as pd

# Set the dataframe df
df = pd.DataFrame({
        'Fruit': ['Apple', 'Banana', 'Strawberry', 'Blueberry', 'Mango'],
        'Aisle': [1, 1, 2, 2, 3],
        'Shelf': ['A', 'B', 'C', 'D', 'E']
})

print(df, end='\n\n')

# Get the number of rows
n_rows = df.shape[0]
print('Number of Rows:', n_rows)

# Get the number of columns in the dataframe
n_col = df.shape[1]
print('Number of Columns:', n_col, end='\n\n')

# Get column names
print('Column names:', df.columns, end='\n\n')

# Replace 'fruit' column name with 'item'
df.columns = ['Item', 'Aisle', 'Shelf']
print(df)

# save as .csv
df.to_csv("df.csv", index=False)
