import pandas as pd
import csv

def renumber_fault_codes(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Dictionary to track the last number used in each 1000s group
    last_used = {}

    # Iterate through the DataFrame
    for index, row in df.iterrows():
        # Calculate the group (e.g., 1000, 2000, etc.)
        group = (row['fault_code'] // 1000) * 1000

        # If the group is not in the dictionary, initialize it to group + 1 (e.g., 1001)
        if group not in last_used:
            last_used[group] = group + 1
        else:
            # Increment the last used number for the group
            last_used[group] += 1

        # Assign the new, unique fault code to the row
        df.at[index, 'fault_code'] = last_used[group]

    # Save the modified DataFrame to a new CSV file
    output_file_path = 'renumbered_fault_codes.csv'
    df.to_csv(output_file_path, index=False, quoting=csv.QUOTE_ALL)

    return output_file_path

# Replace with the path to your CSV file
file_path = 'E:/kate-23.08.4-2247-windows-cl-msvc2019-x86_64/Projects/Whirlpool/Reason Codes/updated_reason_codes.csv'
new_file_path = renumber_fault_codes(file_path)
print(f"Modified file saved as {new_file_path}")

