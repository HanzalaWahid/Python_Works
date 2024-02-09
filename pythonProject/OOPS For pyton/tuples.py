val = (5,6,74,5,46,44,32,5,6,78)
print(type(val))
print(val.count(5))
length_of_tuple = len(val)
print(length_of_tuple)
max_value = max(val)
print(max_value)
min_value = min(val)
print(min_value)
reversed = val[::-1]
print(reversed)


name = "Hanzala"
reversed = name[::-1]
print(reversed)

import pandas as pd

df = pd.read_csv(r"C:\Users\kk\Desktop\intership\DataScience\Data set\EU superstore")
df = pd.read_csv(r"C:\Users\kk\Desktop\intership\DataScience\Data set\EU superstore.csv", encoding='utf-8')
df = pd.read_csv(r"C:\Users\kk\Desktop\intership\DataScience\Data set\EU superstore")

df.open

import pandas as pd

file_path = r"C:\Users\kk\Desktop\intership\DataScience\Data set\EU superstore.csv"

try:
    df = pd.read_csv(file_path)
    # Your further processing with the DataFrame goes here
    print(df.head())
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")



