import pandas as pd
import json
import os


csv_files = {
    "51A - PreFoam": "E:/kate-23.08.4-2247-windows-cl-msvc2019-x86_64/Projects/Whirlpool/Ignition Json Tags/Amana LN51/PreFoam.csv",
    "51B - Side Line": "E:/kate-23.08.4-2247-windows-cl-msvc2019-x86_64/Projects/Whirlpool/Ignition Json Tags/Amana LN51/Side Line.csv",
    "51C - Charge": "E:/kate-23.08.4-2247-windows-cl-msvc2019-x86_64/Projects/Whirlpool/Ignition Json Tags/Amana LN51/Charge.csv",
    "51D - Doors Pantry": "E:/kate-23.08.4-2247-windows-cl-msvc2019-x86_64/Projects/Whirlpool/Ignition Json Tags/Amana LN51/Doors Pantry.csv",
    "51E - Inspection": "E:/kate-23.08.4-2247-windows-cl-msvc2019-x86_64/Projects/Whirlpool/Ignition Json Tags/Amana LN51/Inspection.csv"
}

def create_json_files(template, csv_file_path, section_name):
    df = pd.read_csv(csv_file_path, header = None)
    stations = df[0].unique()
    tags_list = []

    for station in stations:
        station_data = {
            "name": station,
            "typeId": "AssemblyWorkStation",
            "parameters": {
                "DataConcentratorName": {"dataType": "String", "value": "M317-DC1"},
                "OPCTagName": {"dataType": "String", "value": station},
                "KepDevice": {"dataType": "String", "value": "AMA-M317-DC1-CH1"}
            },
            "tagType": "UdtInstance",
            "tags": [
                {"name": "State", "tagType": "AtomicTag"},
                {"name": "EQName", "tagType": "AtomicTag"}
            ]
        }
        tags_list.append(station_data)

    modified_template = template.copy()
    modified_template['name'] = section_name
    modified_template['tags'] = tags_list

    json_directory = "json_files"
    os.makedirs(json_directory, exist_ok=True)
    file_path = f"{json_directory}/{section_name}.json"
    print(f"Saving combined JSON file: {file_path}")
    with open(file_path, 'w') as json_file:
        json.dump(modified_template, json_file, indent=4)

template = {
    "name": "",
    "tagType": "Folder",
    "tags": []
}


for section_name, csv_file in csv_files.items():
    create_json_files(template, csv_file, section_name)
