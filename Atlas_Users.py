import os
from dotenv import load_dotenv
from ApiClient import ApiClient
from GoogleSheets import authenticate_and_open_sheet
from datetime import datetime
import pandas as pd


# Carregue as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém os valores das variáveis de ambiente
base_url = os.getenv('ATLAS_BASE_URL_API')
username = os.getenv('ATLAS_USERNAME')
password = os.getenv('ATLAS_PASSWORD')
org_id_prefix = os.getenv('ATLAS_ORG_ID_PREFIX')
project_id_prefix = os.getenv('ATLAS_PROJECT_ID_PREFIX')

# Autentique e abra a planilha
spread = authenticate_and_open_sheet()

api = ApiClient(base_url, username, password, org_id_prefix, project_id_prefix)

response = api.make_request('users')

if response.status_code == 200:
    data = response.json()

    user_info = []  # Lista para armazenar informações de usuário

    for user in data['results']:
        email = user['emailAddress']
        roles = user['roles']

        # Verifique se o campo 'lastAuth' existe no objeto antes de acessá-lo
        if 'lastAuth' in user:
            last_auth = user['lastAuth']
        else:
            last_auth = None  # Ou qualquer valor padrão que você desejar

        user_info.append({
            'last_export': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Adicione a data da escrita
            'email': email,
            'lastAuth': last_auth,
            'roles': roles
        })

    # Crie um DataFrame do Pandas com os dados
    df = pd.DataFrame(user_info)

    # Salve o DataFrame na planilha
    spread.df_to_sheet(df, index=False, sheet="Atlas_Users")

    print("Informações de Usários do Atlas salvas na planilha Atlas_Users com sucesso")

else:
    print(f'Falha na solicitação. Código de status: {response.status_code}')
