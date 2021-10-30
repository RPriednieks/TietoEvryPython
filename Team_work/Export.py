from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"
my_dict = {'a': 5, 'b': 6, 'c': 5}
workbook.save(filename="hello_world.xlsx")

def print_rows():
    for row in sheet.iter_rows(values_only=True):
        print(row)

print_rows()