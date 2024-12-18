from unittest import result
import pandas as pd

def my_read_excel(excel_path="D:\\VScode\\workhome\\test\\ykdtest\\data\\ykdtest.xlsx",skip_first=True):
    excelFile = pd.ExcelFile(excel_path)
    for my_sheet_name in excelFile.sheet_names:
        df = pd.read_excel(excelFile,sheet_name=my_sheet_name)
        if skip_first == True:
            start_row = 1
        else:
            start_row = 0
        for index, row in df.iterrows():
            results = row
            print(results)
    return results

        
