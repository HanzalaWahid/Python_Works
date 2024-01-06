import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [28, 24, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Set 'Name' as the index
df.set_index('Name', inplace=True)

# Perform some operations that may change the index
df['Occupation'] = ['Engineer', 'Doctor', 'Teacher']

# Reset the index
df_reset = df.reset_index()

# Display the original and reset DataFrames
print("Original DataFrame:")
print(df)

print("\nDataFrame after resetting the index:")
print(df_reset)
