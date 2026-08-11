import gspread
import re

gc = gspread.service_account('service_account_credentials.json')

spreadsheet = gc.open_by_key('1qDp9768HXetmIXD9TMd3er3hqW5QRFiZw6Z0trzq3p4')

pattern = r'^Sheet\d+$'

all_ws = spreadsheet.worksheets()

for ws in all_ws:
    if re.search(pattern, ws.title) is not None:
        spreadsheet.del_worksheet(ws)