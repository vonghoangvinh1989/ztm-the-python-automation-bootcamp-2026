import gspread

gc = gspread.service_account('service_account_credentials.json')

spreadsheet = gc.open_by_key('15WA4SZB8898vixQrvy6dxy50vnP9HngnN36RBiMbVMw')

ws = spreadsheet.worksheet('Copy of Ratings')

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