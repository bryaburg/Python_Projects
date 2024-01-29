import pandas as pd

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

datatypes = ['T4','I','0','N7','N11','N12','N15','N16','N25','N26','B3','C5', 'S']
array = ['']
bit = ['','PRE']

print(df.loc[:,["Address"]])
