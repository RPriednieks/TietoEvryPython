import xlsxwriter
import vendor as v
import datetime

# Creates Excel file
workbook = xlsxwriter.Workbook("Fuel prices {:%Y-%m-%d %H-%M-%S}.xlsx".format(datetime.datetime.now()))


def get_rows():
    """
    Returns list of list for table contents.
    Output example:
        [['Neste', 1.487, None, 1.527, 1.367, 1.457, None, None, None],
        ['Circle K', 1.504, None, 1.564, 1.384, 1.444, 0.755, None, None]
    """
    data = []
    for i in v.get_vendors(v.vendors):
        sublist = []
        sublist.append(i)
        prices = v.get_prices(i)
        for key in prices:
            sublist.append(prices[key])
        data.append(sublist)
    return data


def get_columns():
    """
    Returns list of dictionaries for column names and data type.
    Output example:
        [{'header': 'Vendor'}, {'header': '95', 'format': <xlsxwriter.format.Format object at 0x7f78a80d6dc0>}]
    """
    column_values = []
    currency_format = workbook.add_format({'num_format': '€ 0.000'})
    column_values.append({"header": "Vendor"})
    for i in v.get_fuel_types(v.fuel_types):
        column_values.append({"header": i, "format": currency_format})
    return column_values


def get_series(line):
    """"
    Input arguments for function = string
    Returns dictionary to create series for a chart.
    Input example:
        get_series("4")
    Output example:
        {'name': '=Sheet1!$A$4', 'categories': '=Sheet1!$B$1:$I$1', 'values': '=Sheet1!$B$4:$I$4'}
    """
    series = {}
    name = "=Sheet1!$A$" + line
    categories = "=Sheet1!$B$1:$I$1"
    values = "=Sheet1!$B$" + line + ":$I$" + line
    # Vendor name
    series['name'] = name
    # Fuel types (At the moment fixed. How to expand automatically?)
    series['categories'] = categories
    # Fuel prices
    series['values'] = values
    return series


def create_excel():
    """
    Creates Excel with two sheets.
    """
    data = get_rows()
    columns = get_columns()
    worksheet = workbook.add_worksheet()

    worksheet.add_table(0, 0, len(get_rows()), len(get_columns()) - 1,
                        {"data": data, "columns": columns, "autofilter": False})
    # Here chart part starts
    chart_sheet = workbook.add_chartsheet()
    chart1 = workbook.add_chart({'type': 'bar'})
    # Iterate vendors to create one series per vendor
    for i in range(len(v.get_vendors(v.vendors))):
        x = get_series(str(i + 2))
        chart1.add_series(x)
    # Chart design and style
    chart1.set_title({'name': 'Degvielas cenu salīdzinājums'})
    chart1.set_x_axis({'name': 'Cena (€)', 'min': 0.5})
    chart1.set_y_axis({'name': 'Degvielas tipi', 'major_gridlines': {'visible': True,'line': {'width': 1.25, 'dash_type': 'dash'}},
                       'num_font': {'size': 14, 'bold': True}})
    chart1.set_style(2)
    chart_sheet.set_chart(chart1)
    workbook.close()


if __name__ == "__main__":
    create_excel()
