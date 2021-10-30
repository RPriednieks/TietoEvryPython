import random
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
import vendor


fuel_types = vendor.get_fuel_types()

workbook = Workbook()
sheet = workbook.active

# Let's create some sample sales data
rows = [
    ["", "95", "95 Premium", "98", "DD", "DD Premium", "LPG", "CNG", "85"],
    ["Neste", ],
    ["Virši", ],
    ["CircleK", ],
    ["Viada", ],
]


for i in fuel_types:
    sheet.append(i)

#
# for row in sheet.iter_rows(min_row=2,
#                            max_row=4,
#                            min_col=2,
#                            max_col=13):
#     for cell in row:
#         cell.value = random.randrange(5, 100)

workbook.save(filename="hello_world.xlsx")