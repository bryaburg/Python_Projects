"""Quick Bash script for ouput
for x in $(seq 1 $(wc -l K45791_01_17_2024_Comments.CSV | cut -f1 -d" "))
do
    line=$(cat K45791_01_17_2024_Comments.CSV | head -n +"$x" | tail -n 1)
    iostr=$(echo "$line" | cut -f1 -d,)
    desc=$(echo "$line" | cut -f4 -d,)
    ioaddr=$(echo "$iostr" | cut -f1 -d":")
    ioslot=$(echo "$iostr" | cut -f2 -d":" | cut -f1 -d"/")
    ioterminal=$(echo "$iostr" | cut -f2 -d":" | cut -f2 -d"/")
    printf "COMMENT,,Local:%s:%s,%s,,\"Local:%s:%s.DATA.%s\"\n" "$ioslot" "$ioaddr" "$desc" "$ioslot" "$ioaddr" "$ioterminal"
done

TAG,,Local:{slot}:{addr},"","AB:1756_D{addr}:{addr}:0","","(ExternalAccess := Read/Write)"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"
"""

import csv

def read_line(file_name, line_number):
    with open(file_name, 'r') as file:
        for current_line, content in enumerate(file, 1):
            if current_line == line_number:
                return content.strip()
    return None

file_path = r'C:\Users\bburgess\Desktop\Python_Projects\logix500to5000tags\K45791_01_17_2024_Comments.CSV'
output_path = r'C:\Users\bburgess\Desktop\Python_Projects\logix500to5000tags\output.csv'

with open(file_path, 'r') as file:
    total_lines = sum(1 for line in file)

# Open the output file in write mode
with open(output_path, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)

    for x in range(1, total_lines + 1):
        line = read_line(file_path, x)
        if line:
            parts = line.split(',')
            iostr = parts[0]
            desc = parts[3]

            io_parts = iostr.split(':')
            ioaddr = io_parts[0]

            if '/' in io_parts[1]:
                ioslot, ioterminal = io_parts[1].split('/')
            else:
                ioslot = io_parts[1]
                ioterminal = ''  # or some default value

            # Write the formatted data to the CSV file
            csv_writer.writerow([f"COMMENT", "", f"Local:{ioslot}:{ioaddr}", desc, "", f"Local:{ioslot}:{ioaddr}.DATA.{ioterminal}"])


