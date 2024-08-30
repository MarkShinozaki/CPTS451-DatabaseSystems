import pandas as pd

# Path to your CSV file
csv_file_path = 'C:/Users/mark-/OneDrive/LapTop - Desktop/MASTER - 451/Homeworks/Homework 5/mySalesData.csv'
processed_csv_file_path = 'C:/Users/mark-/OneDrive/LapTop - Desktop/MASTER - 451/Homeworks/Homework 5/mySalesData_processed.csv'

# Specify the correct headers
headers = ['pname', 'discount', 'month', 'price']

# Read the CSV file into a pandas DataFrame with the correct headers
data = pd.read_csv(csv_file_path, header=None, names=headers)

# Print the first few rows to verify
print("Data preview:")
print(data.head())

# Remove percentage signs from the 'discount' column and convert to numeric
data['discount'] = data['discount'].str.rstrip('%').astype(float)

# Save the processed DataFrame to a new CSV file
data.to_csv(processed_csv_file_path, index=False)
print("Processed CSV file saved as:", processed_csv_file_path)
