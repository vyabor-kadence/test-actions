import gspread
import pandas as pd
from google.oauth2 import service_account
import yaml
import os

os.getcwd()
secret_service = os.environ["service"]

scope = ['https://www.googleapis.com/auth/spreadsheets']

# credentials = service_account.Credentials.from_service_account_file(filename = '../src/service.json', scopes = scope)
#with open(r'.github/workflows/main.yml') as file:
#    y = yaml.safe_load(file)
#globals().update(y)
credentials = service_account.Credentials.from_service_account_file(filename = secret_service, scopes = scope)

gc = gspread.authorize(credentials)

workbook = gc.open_by_key("1Bcvw-Q4Nwz58e0UUolhyiQ1lHt0H9DEFdx0s_SaAZ4E")
sheet = workbook.worksheet("Sheet1")

sheet.update("C2", "This is automatically added from Python!")
