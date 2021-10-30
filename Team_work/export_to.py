import xlsxwriter
import vendor as v

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

def get_rows():
    data = []
    for i in v.get_vendors():
        sublist = []
        sublist.append(i)
        prices = v.get_prices(i)
        for key in prices:
            sublist.append(prices[key])
        data.append(sublist)
    return data

data = get_rows()

column_values = []
column_values.append({"header": "Vendor"})
for i in v.get_fuel_types():
    column_values.append({"header": i})

worksheet.add_table('A1:I5', {'data': data, 'columns': column_values})
workbook.close()
