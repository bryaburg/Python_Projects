import pandas as pd
import re

'''
RangeIndex: 352 entries, 0 to 351
Data columns (total 29 columns):
 #   Column                 Non-Null Count  Dtype
---  ------                 --------------  -----
 0   ;Tag Type              352 non-null    object
 1   Tag Name               349 non-null    object
 2   Tag Description        2 non-null      object
 3   Read Only              349 non-null    object
 4   Data Source            349 non-null    object
 5   Security Code          349 non-null    object
 6   Alarmed                349 non-null    object
 7   Native Type            238 non-null    object
 8   Value Type             238 non-null    object
 9   Min Analog             238 non-null    float64
 10  Max Analog             238 non-null    float64
 11  Initial Analog         238 non-null    float64
 12  Scale                  238 non-null    float64
 13  Offset                 238 non-null    float64
 14  DeadBand               238 non-null    float64
 15  Units                  0 non-null      float64
 16  Off Label Digital      111 non-null    float64
 17  On Label Digital       111 non-null    float64
 18  Initial Digital        111 non-null    float64
 19  Length String          0 non-null      float64
 20  Initial String         0 non-null      float64
 21  Retentive              0 non-null      float64
 22  Address                349 non-null    object
 23  System Source Name     0 non-null      float64
 24  System Source Index    0 non-null      float64
 25  RIO Address            0 non-null      float64
 26  Element Size Block     0 non-null      float64
 27  Number Elements Block  0 non-null      float64
 28  Initial Block          0 non-null      float64
dtypes: float64(19), object(10)
memory usage: 79.9+ KB
RangeIndex(start=0, stop=352, step=1)
'''

csv = r"C:\Users\bburgess\OneDrive - ESCO\Desktop\Python_Projects\FTV_Tags\Heinz_K45791-Tags.CSV"

df = pd.read_csv(csv, sep=',', skipinitialspace=True)

df_info = df.info()

df_index = df.index

df_row_address = df.loc[:, "Address"]

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
