import gspread

gc = gspread.service_account('service_account_credentials.json')

new_spreadsheet = gc.open('gspread 201')

new_spreadsheet.share('vonghoangvinh1989@gmail.com', perm_type='user', role='writer')

