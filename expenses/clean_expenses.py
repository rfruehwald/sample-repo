# import excel
# Clean excel data
# write back to excel

import pandas as pd 

excel_workbook = 'expenses.xlsx'
sheet1 = pd.read_excel(excel_workbook, header = None, sheet_name='travel expense account')
#print(sheet1.head(1))
#print(sheet1.columns)
#print(sheet1.at[6,1])
#print(sheet1.at[0,0])
#print(sheet1.iloc[6])
#for col in sheet1.columns:
 #   print(sheet1.at())
print(sheet1[1])



#excel_startTime = sheet1('Column1')
#print(excel_startTime)

