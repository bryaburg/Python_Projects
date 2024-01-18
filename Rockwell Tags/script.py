import pandas as pd

csv_file = 'C:/Users/bburgess/Desktop/Python_Projects/Rockwell Tags/K45791_01_17_2024-Controller-Tags.CSV'

try:
    df = pd.read_csv(csv_file, sep=',', skiprows=6)
except pd.errors.ParserError as e:
    print(f"An error occurred while reading the CSV file: {e}")
    raise

while True:
    value_to_find = input("Enter the value you want to find (or type 'exit' to quit): ")
    if value_to_find.lower() == 'exit':
        print("Exiting program.")
        break

    if df.isin([value_to_find]).any().any():
        replacement_value = input("Enter the replacement value: ")
        df.replace(value_to_find, replacement_value, inplace=True)

        output_file = 'C:/Users/bburgess/Desktop/Python_Projects/Rockwell Tags/Controller-Tags_Update.CSV'
        df.to_csv(output_file, index=False)

        print("Modifications completed and saved to the new CSV file.")
        break
    else:
        print("Value not found in the file. Please try again.")
