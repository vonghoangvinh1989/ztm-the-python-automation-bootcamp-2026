import openpyxl
from openpyxl.styles import Font, numbers

# load the spreadsheet
employee_sales_spreadsheet = openpyxl.load_workbook('Employee Sales.xlsx')

# take user input to specify worksheets and ranges
while True:
    worksheet_1 = str(input("Please enter the name of the first worksheet:\n")).strip()
    worksheet_1_range = str(input("Please specify the target range of cells on the first worksheet:\n")).strip().upper()
    worksheet_2 = str(input("Please enter the name of the second worksheet:\n")).strip()
    worksheet_2_range = str(input("Please specify the target range of cells on the second worksheet:\n")).strip().upper()

    if worksheet_1_range != worksheet_2_range:
        print("Please select two ranges with identical dimensions\n")
    else:
        break

# perform comparison between specified cell ranges
range_1 = employee_sales_spreadsheet[worksheet_1][worksheet_1_range]
range_2 = employee_sales_spreadsheet[worksheet_2][worksheet_2_range]

column_names = {
    1: 'Employee Name',
    2: 'Q1 Sales',
    3: 'Q2 Sales',
    4: 'Q3 Sales',
    5: 'Q4 Sales',
}

differences = [['Row', 'Column', 'Value 1', 'Value 2', 'Delta']]
for row_1, row_2 in zip(range_1, range_2):
    for cell_1, cell_2 in zip(row_1, row_2):
        if cell_1.value != cell_2.value:
            if isinstance(cell_1.value, (int, float)) and isinstance(cell_1.value, (int, float)):
                formulas = f'=ABS({cell_1.value} - {cell_2.value}) / AVERAGE({cell_1.value}, {cell_2.value})'
                differences.append([cell_1.row - 1, column_names[cell_1.column], cell_1.value, cell_2.value, formulas])
            else:
                differences.append([cell_1.row - 1, column_names[cell_1.column], cell_1.value, cell_2.value, ''])

diff_sheets = employee_sales_spreadsheet.create_sheet('Diffs')
for row in differences:
    diff_sheets.append(row)

for cell in diff_sheets["E"][1:]:
    if cell.value is not None:
        cell.font = Font(color="FF0000")
        cell.number_format = numbers.FORMAT_PERCENTAGE_00

employee_sales_spreadsheet.save('Employee Sales.xlsx')