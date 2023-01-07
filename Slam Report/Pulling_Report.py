import csv
import pandas as pd
import requests
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
import openpyxl
from openpyxl import load_workbook

goog_url = "https://monitorportal.amazon.com/mws?Action=GetGraph&Version=2007-07-07&SchemaName1=Search&Pattern1" \
           "=marketplace%3D%24DSM5%24%20methodname%3D%24ALL%24%20metric%3DDSM5-SLAM%20%28LabelScan%20OR%20LabelZone" \
           "%20OR%20PackageCleared%20OR%20NoRead%20OR%20MultiRead%29&Period1=OneHour&Stat1=sum&SchemaName2=Search" \
           "&Pattern2=marketplace%3D%24DSM5%24%20methodname%3D%24processPackageVerified%24%20metric%3DDSM5%20Shipped" \
           "%20&Stat2=n&HeightInPixels=250&WidthInPixels=600&GraphTitle=SLAM%20REPORT%20v5&TZ=CST6CDT@TZ%3A%20CST6CDT" \
           "&StartTime1=-PT12H&EndTime1=-PT0H&OutputFormat=CSV_TRANSPOSE "


def download_slam_data(csv_url):
    download = requests.get(csv_url, auth=HTTPKerberosAuth(OPTIONAL), verify=False)

    decoded_csv = download.content.decode('utf-8')

    cr = csv.reader(decoded_csv.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(my_list)
    df = pd.DataFrame(my_list)
    df.to_csv("SLAM_file.csv")
    
# Read the CSV file
df = pd.read_csv('SLAM_file.csv')

# Open the existing Excel file
with pd.ExcelWriter('C:/Users/bryaburg/Desktop/Python_Projects/Python_Projects/Slam Report/SLAM Report.xlsm', mode='a', engine= "openpyxl", if_sheet_exists = 'replace') as writer:
    # Write the data to the specified sheet
    df.to_excel(writer, startrow=0, startcol=0,  index=False, header=False, sheet_name='DATA', )

download_slam_data(goog_url)