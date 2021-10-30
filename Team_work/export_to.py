import xlsxwriter
import vendor as v
import datetime

workbook = xlsxwriter.Workbook("Fuel prices {:%Y-%m-%d %H-%M-%S}.xlsx".format(datetime.datetime.now()))

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
    currency_format = workbook.add_format({'num_format': '€ #.###'})
    column_values.append({"header": "Vendor"})
    for i in v.get_fuel_types():
        column_values.append({"header": i, "format": currency_format})
    return column_values


def create_excel():
    data = get_rows()
    columns = get_columns()
    worksheet = workbook.add_worksheet()
    worksheet.add_table(0, 0, len(get_rows()), len(get_columns())-1, {"data": data, "columns": columns, "autofilter": False})
    workbook.close()


create_excel()
# x = get_columns()
# print(x)