import os

def generate_code(input_file_path, output_file_name):
    dir_path = os.path.dirname(input_file_path)
    with open(input_file_path, 'r') as file:
        station_ids = file.readlines()
    station_ids = [id.strip() for id in station_ids]
    template = "[CLR({station_id}),XIC(ESTOP)MOV(1,{station_id}),XIC(ANDON_BUTTON)MOV(2,{station_id}),XIC(NOT_MACHNE)MOV(4,{station_id}),XIC(PE)MOV(8,{station_id}),MOV({station_id},LN51_TO_DC01_{message_type}_MESSAGE_{letter}[{index}])];"
    new_lines = []
    current_letter = None
    index = 1
    current_message_type = None
    for station_id in station_ids:
        letter = station_id[5] 
        message_type = 'MAIN' if station_id[6] == 'M' else 'SUB'
        if letter != current_letter or message_type != current_message_type:
            current_letter = letter
            current_message_type = message_type
            index = 1
        new_line = template.format(message_type=message_type, letter=letter, index=index, station_id=station_id)
        new_lines.append(new_line)
        index += 1
    output_file_path = os.path.join(dir_path, output_file_name)
    with open(output_file_path, 'w') as output_file:
        for line in new_lines:
            output_file.write(line + '\n')
input_file_path = 'Line51DC.txt'
output_file_name = 'Line51dcupdate.txt'
generate_code(input_file_path, output_file_name)


