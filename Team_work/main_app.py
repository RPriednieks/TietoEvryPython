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

def get_series(line):
    """"
    input value for function = string
    Returns dictionary to generate series in chart.
    Output example:
        {'name':'=Sheet1!$B$1','categories':'=Sheet1!$A$2:$A$7','values':'=Sheet1!$B$2:$B$7'}
    """
    series = {}
    name = "=Sheet1!$A$" + line
    categories = "=Sheet1!$B$1:$I$1"
    values = "=Sheet1!$B$" + line + ":$I$" + line
    series['name'] = name
    series['categories'] = categories
    series['values'] = values
    return series


def create_excel():
    data = get_rows()
    columns = get_columns()
    worksheet = workbook.add_worksheet()
    worksheet.add_table(0, 0, len(get_rows()), len(get_columns())-1, {"data": data, "columns": columns, "autofilter": False})

    chartsheet = workbook.add_chartsheet()
    chart1 = workbook.add_chart({'type': 'bar'})

    for i in range(len(v.get_vendors())):
        x = get_series(str(i + 2))
        chart1.add_series(x)

    chart1.set_title({'name': 'Degvielas cenu salīdzinājums'})
    chart1.set_x_axis({'name': 'Cena (€)'})
    chart1.set_y_axis({'name': 'Degvielas tipi'})
    chart1.set_style(12)
    chartsheet.set_chart(chart1)

    workbook.close()


create_excel()
# x = get_columns()
# print(x)