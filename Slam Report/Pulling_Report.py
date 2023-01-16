import csv
import pandas as pd
import requests
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
import openpyxl
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles.numbers import NUMBER_FORMAT
import io

goog_url = "https://monitorportal.amazon.com/mws?Action=GetGraph&Version=2007-07-07&SchemaName1=Search&Pattern1" \
           "=marketplace%3D%24DSM5%24%20methodname%3D%24ALL%24%20metric%3DDSM5-SLAM%20%28LabelScan%20OR%20LabelZone" \
           "%20OR%20PackageCleared%20OR%20NoRead%20OR%20MultiRead%29&Period1=OneHour&Stat1=sum&SchemaName2=Search" \
           "&Pattern2=marketplace%3D%24DSM5%24%20methodname%3D%24processPackageVerified%24%20metric%3DDSM5%20Shipped" \
           "%20&Stat2=n&HeightInPixels=250&WidthInPixels=600&GraphTitle=SLAM%20REPORT%20v5&TZ=CST6CDT@TZ%3A%20CST6CDT" \
           "&StartTime1=-PT12H&EndTime1=-PT0H&OutputFormat=CSV_TRANSPOSE "

# This grabs the slam data and saves it in a CSV file
def download_slam_data(csv_url):
    
    #This Auth me getting the info from the URL
    download = requests.get(csv_url, auth=HTTPKerberosAuth(OPTIONAL), verify=False)
    
    # This decodes it and then saves it to a CSV file
    decoded_csv = download.content.decode('utf-8')
    cr = csv.reader(decoded_csv.splitlines(), delimiter=',')
    my_list = list(cr)
    df = pd.DataFrame(my_list)
    df.to_csv("SLAM_file.csv", header=False, index=False)
    
    # Open the existing Excel file and put in csv data
    with pd.ExcelWriter('C:/Users/bryaburg/Desktop/Python_Projects/Python_Projects/Slam Report/SLAM Report.xlsx', engine= "openpyxl", mode='a') as writer:
        # Read the excel file
        df = pd.read_csv('SLAM_file.csv')

        # Write the data to the specified sheet
        df.to_excel(writer, sheet_name='DATA', startrow=writer.sheets['DATA'].max_row, index=False, header=False)
        writer.save()
        
    # Load the existing excel file
    book = load_workbook('C:/Users/bryaburg/Desktop/Python_Projects/Python_Projects/Slam Report/SLAM Report.xlsx')
    worksheet = book["DATA"]

    for col in worksheet.iter_cols(values_only=True):
        for cell in col:
            if isinstance(cell, (int, float)):
                worksheet[cell.coordinate].number_format = NUMBER_FORMAT

    book.save('C:/Users/bryaburg/Desktop/Python_Projects/Python_Projects/Slam Report/SLAM Report.xlsx')

'''    with pd.ExcelWriter('C:/Users/bryaburg/Desktop/Python_Projects/Python_Projects/Slam Report/SLAM Report.xlsx', mode='a') as writer:
        # Read the excel file
        df = pd.read_csv('SLAM_file.csv')
        #Convert data in Dataframe to float
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col], errors='ignore')
            except ValueError:
                pass
        # Write the data to the specified sheet as numbers
        df.to_excel(writer, sheet_name='DATA', startrow=writer.sheets['DATA'].max_row, index=False, header=False)'''


download_slam_data(goog_url)