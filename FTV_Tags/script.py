import pandas as pd
import re

'''
#Old style {datatype}:{array}.{bit}
#New Style {datatype}{[array]}.{bit}

Data Types 
;Tag Type                 object
Tag Name                  object
Tag Description           object
Read Only                 object
Data Source               object
Security Code             object
Alarmed                   object
Native Type               object
Value Type                object
Min Analog               float64
Max Analog               float64
Initial Analog           float64
Scale                    float64
Offset                   float64
DeadBand                 float64
Units                    float64
Off Label Digital        float64
On Label Digital         float64
Initial Digital          float64
Length String            float64
Initial String           float64
Retentive                float64
Address                   object
System Source Name       float64
System Source Index      float64
RIO Address              float64
Element Size Block       float64
Number Elements Block    float64
Initial Block            float64
'''

csv = r"C:\Users\bburgess\OneDrive - ESCO\Desktop\Python_Projects\FTV_Tags\Heinz_K45791-Tags.CSV"

df = pd.read_csv(csv, sep=',', skipinitialspace=True)

df = df.dropna(subset=['Address'])

regex_patterns = {
    'I': r'::\[[a-zA-Z0-9]+\]I:\d+/\d+',
    'O': r'::\[[a-zA-Z0-9]+\]O:\d+/\d+',
    'B3': r'\[k45791\]B3/\d+',
    'N7': r'::\[[a-zA-Z0-9]+\]N\d+:\d+',
    'N11': r'::\[[a-zA-Z0-9]+\]N\d+:\d+',
    'N12': r'::\[[a-zA-Z0-9]+\]N\d+:\d+',
    'N15': r'::\[[a-zA-Z0-9]+\]N\d+:\d+',
    'N16': r'::\[[a-zA-Z0-9]+\]N\d+:\d+',
    'N25': r'::\[[a-zA-Z0-9]+\]N\d+:\d+',
    'N26': r'::\[[a-zA-Z0-9]+\]N\d+:\d+',
    'S': r'',
    'T4': r'::\[[a-zA-Z0-9]+\]T4:\d+\.[A-Z]+',
    'C5': r'::\[[a-zA-Z0-9]+\]C5:\d+\.ACC'
}


datatypes = {
    'I': {'array': [''], 'bit': ['']},

    'O': {'array': [''], 'bit': ['']},

    'B3': {'array': [''], 'bit': ['']},

    'N7': {'array': [''], 'bit': ['']},
    'N11': {'array': [''], 'bit': ['']},
    'N12': {'array': [''], 'bit': ['']},
    'N15': {'array': [''], 'bit': ['']},
    'N16': {'array': [''], 'bit': ['']},
    'N25': {'array': [''], 'bit': ['']},
    'N26': {'array': [''], 'bit': ['']},

    'S': {'array': [''], 'bit': ['']},
    
    'T4': {'array': [''], 'bit': ['PRE']},

    'C5': {'array': [''], 'bit': ['ACC']}   

}

N = 237
bits_per_word = 16

def calculate_B3(N, bits_per_word):
    array_index = N // bits_per_word
    bit_index = N % bits_per_word
    print(f"B3[{array_index}].{bit_index}")
    return(f"B3[{array_index}].{bit_index}")

calculate_B3(N, bits_per_word)
