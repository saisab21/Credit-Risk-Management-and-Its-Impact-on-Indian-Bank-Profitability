import pandas as pd

# Load the dataset without assuming headers
file_path = "C:\\My_Projects\\Credit-Risk-Management-and-Its-Impact-on-Indian-Bank-Profitability\\DATA\\data.csv"  # Replace with your file path
dataset = pd.read_csv(file_path, header=None)

# Display the first few rows for inspection
print(dataset.head())

# Merge the first three rows into column headers
merged_headers = dataset.iloc[0].astype(str) + "_" + dataset.iloc[1].astype(str) + "_" + dataset.iloc[2].astype(str)
dataset.columns = merged_headers

# Drop the first three rows as they are now merged
dataset = dataset.iloc[3:]

# Save the transformed dataset as a CSV file
updated_file_path = "C:\\My_Projects\\Credit-Risk-Management-and-Its-Impact-on-Indian-Bank-Profitability\\DATA\\updated_data.csv"
dataset.to_csv(updated_file_path, index=False)

# Display the transformed dataset
print(dataset.head())

