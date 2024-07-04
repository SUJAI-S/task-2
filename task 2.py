#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

# Load the CSV file into a DataFrame
file_path = '/mnt/data/01.Data Cleaning and Preprocessing.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("Initial DataFrame:")
print(df.head())

# Filter data based on a condition (Example: Filter rows where column 'A' > 10)
# Note: Change 'A' to the actual column name in your CSV file.
# filtered_df = df[df['A'] > 10]

# Fill missing values with 0
df_filled = df.fillna(0)
print("\nDataFrame with missing values filled:")
print(df_filled)

# Drop rows with any missing values
df_dropped = df.dropna()
print("\nDataFrame with missing values dropped:")
print(df_dropped)

# Calculate and display summary statistics
summary_stats = df.describe()
print("\nSummary statistics:")
print(summary_stats)

# Calculate and display the mean of a specific column
# Note: Change 'A' to the actual column name in your CSV file.
# mean_value = df['A'].mean()
# print(f"\nMean value of column 'A': {mean_value}")

# Save the resulting DataFrames to new CSV files
filtered_file_path = '/mnt/data/filtered_data.csv'
filled_file_path = '/mnt/data/filled_data.csv'
dropped_file_path = '/mnt/data/dropped_data.csv'

# filtered_df.to_csv(filtered_file_path, index=False)
df_filled.to_csv(filled_file_path, index=False)
df_dropped.to_csv(dropped_file_path, index=False)

print("\nFiltered, filled, and dropped data saved to CSV files.")

