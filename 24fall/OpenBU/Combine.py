import os
import pandas as pd

# Specify the directory containing your CSV files
directory_path = "./Results"

# Initialize an empty DataFrame to hold the combined data
combined_df = pd.DataFrame()

# Loop through all files in the directory
for file_name in os.listdir(directory_path):
    if file_name.endswith(".csv"):
        # Read each CSV file
        file_path = os.path.join(directory_path, file_name)
        df = pd.read_csv(file_path)
        
        # Append the data to the combined DataFrame
        combined_df = pd.concat([combined_df, df], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv("combined_output.csv", index=False)

print("CSV files combined successfully into 'combined_output.csv'")
