import pandas as pd

# File path
file_path = r"C:\My_Projects\Credit-Risk-Management-and-Its-Impact-on-Indian-Bank-Profitability\DATA\REFINED_DATA.csv"
new_file_path = r"C:\My_Projects\Credit-Risk-Management-and-Its-Impact-on-Indian-Bank-Profitability\DATA\data_excetable.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Merge the first three rows and create a new row
new_row = '_'.join(df.iloc[0:3].astype(str).values.flatten())

# Add the new row as the first row and remove the first three
df.loc[-1] = [new_row] + [''] * (len(df.columns) - 1)  # Add at the beginning
df.index = df.index + 1  # Shift index
df = df.sort_index()  # Sort index to reset

# Drop the first three rows
df = df.drop(df.index[1:4])

# Save the modified data to a new CSV file
df.to_csv(new_file_path, index=False)
