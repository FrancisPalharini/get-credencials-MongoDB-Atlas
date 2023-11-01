import os
import gspread
from gspread_pandas import Spread

def authenticate_and_open_sheet():
    # Lê o caminho para o arquivo google_secret.json da variável de ambiente
    secret_file = os.getenv('GOOGLE_SECRET_FILE') 

    if secret_file is None:
        raise Exception("A variável de ambiente GOOGLE_SECRET_FILE não está definida.")

    # Configure a autenticação com as credenciais do Google Sheets
    gc = gspread.service_account(filename=secret_file)

    # Lê a URL da planilha da variável de ambiente
    spreadsheet_url = os.getenv('PLANILHA_URL')  

    if spreadsheet_url is None:
        raise Exception("A variável de ambiente SPREADSHEET_URL não está definida.")

    # Abra a planilha pelo seu URL
    return Spread(spreadsheet_url, client=gc)
