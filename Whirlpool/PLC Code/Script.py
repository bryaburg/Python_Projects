import os

def generate_code(input_path: str, output_name: str) -> None:
    """Generate code from an input text file and write it to an output text file."""
    with open(input_path, 'r') as in_file, open(
        os.path.join(os.path.dirname(input_path), output_name), 'w'
    ) as out_file:
        template = "[CLR({}),XIC(ESTOP)MOV(1,{}),XIC(ANDON_BUTTON)MOV(2,{}),XIC(NOT_MACHINE)MOV(4,{}),XIC(PE)MOV(8,{}),MOV({},LN51_TO_DC01_{}_MESSAGE{}[{}])];"
        index = 1
        for line in (line.strip() for line in in_file):
            station_id, message_type, station_letter = line[5:8]
            out_file.write(template.format(
                station_id, station_id, station_id, station_id, station_id,
                station_id, message_type, station_letter, index
            ))
            index += 1
input_file_path = r'C:\Users\bburgess\Desktop\Python_Projects-1\Whirlpool\PLC Code\Line51DC.txt'
output_file_name = 'Line51dcupdate.txt'
generate_code(input_file_path, output_file_name)


