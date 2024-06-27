import pandas as pd
import numpy as np


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# Create a dictionary
data = {
    'Category': x,
    'Value': y
}

# Create a DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame by the 'Value' column
sorted_df = df.sort_values(by='Value')

# Display the sorted DataFrame
print(sorted_df)

