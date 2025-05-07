import os
import glob
import pandas as pd

# Define the folder containing the CSV files
folder_path = "NISSAN LEAF"

# Use glob to get a list of all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Initialize an empty list to hold DataFrames
dfs = []

# Loop over the list of files and read each CSV into a DataFrame
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all DataFrames into one DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv("combined_nissan_leaf.csv", index=False)

print("CSV files combined successfully into 'combined_nissan_leaf.csv'")
