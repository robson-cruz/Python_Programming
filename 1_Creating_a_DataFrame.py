# import Library
import pandas as pd

# Set the dataframe df
df = pd.DataFrame({
        'Fruit': ['Apple', 'Banana', 'Strawberry', 'Blueberry', 'Mango'],
        'Aisle': [1, 1, 2, 2, 3],
        'Shelf': ['A', 'B', 'C', 'D', 'E']
})

print(df)

# Get the number of columns in the dataframe
n_col = df.shape[1]
print()
print('Number of Columns:', n_col)

# Get the number of rows
n_rows = df.shape[0]
print('Number of Rows:', n_rows)
