import gspread

gc = gspread.service_account('service_account_credentials.json')

spreadsheet = gc.open_by_key('1hYwobeQRr3hF0cZfbDy0-kHNhchdsZqfJljur7q-iHo')

ws = spreadsheet.worksheet('Ratings')

# formula = '=AVERAGE(B2:E2)'
#
# ws.update_acell('F2', formula)

rng = 'B2:E11'

data = ws.get(rng)

for i, row in enumerate(data):
    for j, val in enumerate(row):
        if not val.isnumeric():
            data[i][j] = ''
        elif int(val) < 0:
            data[i][j] = 0
        elif int(val) > 10:
            data[i][j] = 10
        else:
            data[i][j] = int(val)

ws.update(data, rng)

formulas = [['Average Rating']]

for i in range(len(data)):
    current_row = str(i + 2)
    # formula_cell = f'F{current_row}', could be useful if using update_acell
    formula = f'=AVERAGE(B{current_row}:E{current_row})'
    formulas.append([formula])

formula_range = f'F1:F{str(len(formulas))}'

ws.update(formulas, formula_range, raw=False)