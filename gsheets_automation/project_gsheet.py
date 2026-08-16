import gspread

gc = gspread.service_account('service_account_credentials.json')

wb = gc.open_by_key('1zU-iZKc7VOp_TZPUqYLBtqCiFJds5wh3ekkteMUvRzo')

while True:
    ws1_name = input("Please enter the name of the first worksheet: ")
    rng1_addr = input("Please specify the target range of cells on the first worksheet: ")

    ws2_name = input("Please enter the name of the second worksheet: ")
    rng2_addr = input("Please specify the target range of cells on the second worksheet: ")

    ws1 = wb.worksheet(ws1_name)
    ws2 = wb.worksheet(ws2_name)

    rng1 = ws1.get(rng1_addr)
    rng2 = ws2.get(rng2_addr)

    num_rows = len(rng1)
    num_cols = len(rng1[0])

    if num_rows == len(rng2) and num_cols == len(rng2[0]):
        break
    else:
        print('Please select two ranges with identical dimensions.')

headers = rng1[0]
diffs = []

for i in range(1, num_rows):
    for j in range(num_cols):
        cell1 = rng1[i][j]
        cell2 = rng2[i][j]

        if cell1 != cell2:
            if cell1.isnumeric():
                cell1 = float(cell1)

            if cell2.isnumeric():
                cell2 = float(cell2)

            diff = [i, headers[j], cell1, cell2]
            diffs.append(diff)

diffs_ws = wb.add_worksheet(title='Diffs', rows=num_rows, cols=num_cols)
diffs_ws.update(diffs, f'A2:D{str(len(diffs) + 1)}', raw=False)

diffs_headers = ['Row', 'Column', 'Value 1', 'Value 2']
diffs_ws.update([diffs_headers], 'A1:D1')

# prepare for delta cell
diffs_ws.update_acell(f'E1', 'Delta')

percentage_styles = {
    "textFormat": {
        "foregroundColor": {
            "red": 1.0,
            "green": 0.0,
            "blue": 0.0
        },
        "fontSize": 12,
    },
    "numberFormat": {
        "type": "PERCENT"
    }
}


data = diffs_ws.get(f'A2:D{str(len(diffs) + 1)}')
for idx, row in enumerate(data):
    current_row = str(idx + 2)
    diff_data = diffs[idx]

    if diff_data[2].isnumeric() and diff_data[3].isnumeric():
        current_row = str(idx + 2)
        cell1_add = f'C{current_row}'
        cell2_add = f'D{current_row}'
        formula_cell = f'=ABS({cell1_add}-{cell2_add})/AVERAGE({cell1_add}:{cell2_add})'
        diffs_ws.update_acell(f'E{current_row}', formula_cell)
        diffs_ws.format(f'E{current_row}', percentage_styles)


