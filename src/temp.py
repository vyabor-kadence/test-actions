import gspread
from google.oauth2 import service_account

scope = ['https://www.googleapis.com/auth/spreadsheets']
credentials = service_account.Credentials.from_service_account_file(filename = "secrets.json", scopes = scope)

gc = gspread.authorize(credentials)

workbook = gc.open_by_key("1Bcvw-Q4Nwz58e0UUolhyiQ1lHt0H9DEFdx0s_SaAZ4E")
sheet = workbook.worksheet("Sheet1")

sheet.update("C2", "This is automatically added from Python!")
