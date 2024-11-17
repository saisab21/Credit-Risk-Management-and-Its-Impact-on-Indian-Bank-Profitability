import pandas as pd

# File path
file_path = r"C:\My_Projects\Credit-Risk-Management-and-Its-Impact-on-Indian-Bank-Profitability\DATA\REFINED_DATA.csv"
new_file_path = r"C:\My_Projects\Credit-Risk-Management-and-Its-Impact-on-Indian-Bank-Profitability\DATA\data_excetable.csv"

# Read the CSV file without headers
df = pd.read_csv(file_path, header=None)

# Create a new row by merging the first three rows (A1, A2, A3) for each column
new_row = ['_'.join(df.iloc[0:3, col].astype(str)) for col in range(df.shape[1])]

# Add the new row as the first row
df.loc[-1] = new_row  # Insert the new row at the beginning
df.index = df.index + 1  # Shift the index
df = df.sort_index()  # Sort the index to reset

# Drop the first three rows (A1, A2, A3)
df = df.drop(df.index[1:4])

# Save the modified data to a new CSV file
df.to_csv(new_file_path, index=False, header=False)
