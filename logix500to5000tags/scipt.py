import pandas as pd
import csv

# Function to parse the tag and extract slot, data type, and terminal
def parse_tag_corrected(tag):
    try:
        parts = tag.split(':')
        if len(parts) == 2:
            data_type = parts[0]
            slot_terminal = parts[1].split('/')
            if len(slot_terminal) == 2:
                slot, terminal = slot_terminal
                return slot, data_type, terminal
    except Exception:
        return None, None, None
    return None, None, None

# Function to format a row for the new structure with comments based on each tag's terminal
def format_row_with_specific_terminal(tag, description):
    slot, data_type, terminal = parse_tag_corrected(tag)
    if slot and data_type and terminal:
        formatted_rows = []
        # TAG lines
        tag_line_c = f'TAG,,Local:{slot}:C,"","AB:1756_D{data_type}:C:1","","(ExternalAccess := Read/Write)"'
        tag_line_data_type = f'TAG,,Local:{slot}:{data_type},"","AB:1756_D{data_type}:{data_type}:0","","(ExternalAccess := Read/Write)"'
        formatted_rows.extend([tag_line_c, tag_line_data_type])

        # Determine the number of COMMENT lines based on the terminal number
        try:
            terminal_number = int(terminal)
            comment_range = range(terminal_number + 1)
        except ValueError:
            # If terminal is not a number, skip adding comment lines
            comment_range = []

        # Adding the COMMENT lines
        for i in comment_range:
            comment_line = f'COMMENT,,Local:{slot}:{data_type},"{description.strip()}",,"Local:{slot}:{data_type}.DATA.{i}"'
            formatted_rows.append(comment_line)
        
        return formatted_rows
    else:
        return []

# Read the 'Comments.csv' file
df_comments = pd.read_csv(r'C:\Users\bburgess\Desktop\Python_Projects\logix500to5000tags\K45791_01_17_2024_Comments.CSV')

# Header for the new format
header_new = 'TYPE,SCOPE,NAME,DESCRIPTION,DATATYPE,SPECIFIER,ATTRIBUTES'

# Re-formatting the rows for the new format with comments based on each tag's terminal
formatted_rows_new_with_specific_terminal = [header_new]
for _, row in df_comments.iterrows():
    tag, description = row[0], row[3]
    formatted_rows_new_with_specific_terminal.extend(format_row_with_specific_terminal(tag, description))

# Creating a DataFrame from the new formatted rows
df_formatted = pd.DataFrame({formatted_rows_new_with_specific_terminal})

# Saving the formatted data to a CSV file
output_path = r'C:\Users\bburgess\Desktop\Python_Projects\logix500to5000tags\K45791_01_17_2024-Controller-Tags copy.CSV'
df_formatted.to_csv(output_path, index=False, quoting=csv.QUOTE_ALL)
