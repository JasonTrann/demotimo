import ExcelUtil
import sys
sys.path.append('TimoAndroid/Lib/TimoApp')
excel_util = ExcelUtil()
exel_data = excel_util.xls_to_dict('MoveMoneyTestData.xlsx')
print('excel data: ', exel_data)

excel_data2 = excel_util.load_as_dict('MoveMoneyTestData.xlsx')

for sheet in exel_data:
    print(f"sheet = {sheet}")
    sheet_dict = exel_data[sheet]
    print(f"{sheet} has data: {sheet_dict}")
    for row_as_dict in sheet_dict:
        print(row_as_dict)
        for key in row_as_dict:
            print(f"{key} -> {row_as_dict[key]}")


# Check amount = 0
# Skip test case if payee list is empty
# Skip test case save payee if payee is existing in payee list
# Check finger
# get payeelist length
# from Lib.TimoApp.ExcelUtil import ExcelUtil