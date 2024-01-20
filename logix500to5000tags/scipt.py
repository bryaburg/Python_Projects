import pandas as pd
import csv
import re

# File path for the source file
logix500tags = r'C:\Users\Windows\Desktop\Python_Projects\logix500to5000tags\logix500template.csv'

try:
    # Read the CSV file
    df = pd.read_csv(logix500tags)

    # Function to check if the TYPE is in the 'I:{slot}/{terminal}' or 'O:{slot}/{terminal}' format
    def is_valid_io_type(type_value):
        return re.match(r'[IO]:\d+/\d+', type_value)

    # Function to create formatted rows
    def create_formatted_rows(df, max_terminals=16):
        new_rows = []
        comment_positions = {}  # Track the last position of COMMENT rows for each Local:X:I/O

        for index, row in df.iterrows():
            if is_valid_io_type(row['TYPE']):
                io_type, slot_terminal = row['TYPE'].split(':')
                slot, terminal = slot_terminal.split('/')
                local_name = f'Local:{slot}:{io_type}'

                # Create TAG row if not already created
                if local_name not in comment_positions:
                    tag_row = ['TAG', '', local_name, '', f'AB:1756_DI:{io_type}:0', '', '(ExternalAccess := Read/Write)']
                    new_rows.append(tag_row)
                    comment_positions[local_name] = len(new_rows)  # Initialize position

                # Create COMMENT row
                description = row['DESCRIPTION'].strip('"') if row['DESCRIPTION'] else "SPARE"
                comment_row = ['COMMENT', '', local_name, description, f'{local_name}.DATA.{terminal}', '', '']
                new_rows.append(comment_row)
                comment_positions[local_name] = len(new_rows)  # Update position

        # Add SPARE COMMENT rows in the correct sequence
        for local_name, position in comment_positions.items():
            existing_terminals = {int(row[4].split('.')[2]) for row in new_rows if row[2] == local_name and row[0] == 'COMMENT'}
            for t in range(max_terminals):
                if t not in existing_terminals:
                    spare_comment_row = ['COMMENT', '', local_name, 'SPARE', f'{local_name}.DATA.{t}', '', '']
                    new_rows.insert(position + t - len(existing_terminals), spare_comment_row)

        return pd.DataFrame(new_rows, columns=["TYPE", "SCOPE", "NAME", "DESCRIPTION", "DATATYPE", "SPECIFIER", "ATTRIBUTES"])

    # Create df_new with new formatted rows
    df_new = create_formatted_rows(df)

    # Save df_new to CSV file
    df_new.to_csv(r'C:\Users\Windows\Desktop\Python_Projects\logix500to5000tags\studio5000rev.csv', index=False, quoting=csv.QUOTE_ALL)

except FileNotFoundError:
    print(f"File '{logix500tags}' not found.")
