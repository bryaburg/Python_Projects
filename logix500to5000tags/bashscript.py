"""Quick Bash script for ouput
for x in $(seq 1 $(wc -l K45791_01_17_2024_Comments.CSV | cut -f1 -d" "))
do
    line=$(cat K45791_01_17_2024_Comments.CSV | head -n +"$x" | tail -n 1)
    iostr=$(echo "$line" | cut -f1 -d,)
    desc=$(echo "$line" | cut -f4 -d,)
    ioaddr=$(echo "$iostr" | cut -f1 -d":")
    ioslot=$(echo "$iostr" | cut -f2 -d":" | cut -f1 -d"/")
    ioterminal=$(echo "$iostr" | cut -f2 -d":" | cut -f2 -d"/")
    printf "Addr: %s\nSlot: %s\nTerminal: %s\nDescription: %s\n" "$ioaddr" "$ioslot" "$ioterminal" "$desc"
done
"""

def Tag_Value(csv_file_path, txt_file_path):
    with open(csv_file_path, 'r') as file:
        lines = file.readlines()

    with open(txt_file_path, 'w') as output_file:
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) >= 4:
                iostr = parts[0]
                desc = parts[3]

                iostr_parts = iostr.split(':')
                if len(iostr_parts) == 2 and '/' in iostr_parts[1]:
                    ioaddr = iostr_parts[0]
                    ioslot, ioterminal = iostr_parts[1].split('/')

                    output_file.write(f"Addr: {ioaddr}\nSlot: {ioslot}\nTerminal: {ioterminal}\nDescription: {desc}\n\n")

csv_file_path = r'C:\Users\bburgess\Desktop\Python_Projects\logix500to5000tags\K45791_01_17_2024_Comments.CSV'  # Replace with your CSV file path
txt_file_path = r'C:\Users\bburgess\Desktop\Python_Projects\logix500to5000tags\output.txt'

Tag_Value(csv_file_path, txt_file_path)

