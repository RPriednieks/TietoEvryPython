import xlsxwriter
import vendor as v


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


def get_columns():
    column_values = []
    column_values.append({"header": "Vendor"})
    for i in v.get_fuel_types():
        column_values.append({"header": i})
    return column_values


def create_excel():
    data = get_rows()
    columns = get_columns()
    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.add_table('A1:I5', {'data': data, 'columns': columns})
    workbook.close()


create_excel()
