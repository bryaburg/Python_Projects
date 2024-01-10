import pandas as pd
import csv

csv1 = 'E:/kate-23.08.4-2247-windows-cl-msvc2019-x86_64/Projects/Whirlpool/Reason Codes/Line52_DT_Codes.csv'

df1 = pd.read_csv(csv1, sep=',')

df_new = pd.DataFrame({

    "dt_name" : "",
    "dt_code" : df1["Event Description"],
    "dt_wcm" : "",
    "dt_group" : "",
    "dt_class" : "",
    "dt_cluster" : "LN52states",
    "dt_priority" : "-1",
    "dt_user_selectable" : "false",
    "oeeType" : "Performance",
    "fault_code" : df1["Fault Code"]
})

df_new.to_csv('E:/kate-23.08.4-2247-windows-cl-msvc2019-x86_64/Projects/Whirlpool/Reason Codes/updated_reason_codes.csv', index=False, quoting=csv.QUOTE_ALL)
