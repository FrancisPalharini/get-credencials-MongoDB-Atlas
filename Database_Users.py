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

response = api.make_request('databaseUsers', id_prefix=project_id_prefix)

if response.status_code == 200:
    data = response.json()

    user_info = []  # Lista para armazenar informações de usuário

    for user in data['results']:
        username = user.get('username', '')  # Obtém o campo 'username' do objeto

        roles = user.get('roles', [])  # Use get para evitar erros se 'roles' não estiver presente no objeto

        for role in roles:
            role_name = role.get('roleName', '')  # Use get para evitar erros se 'roleName' não estiver presente

            user_info.append({
                'last_export': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Adicione a data da escrita
                'username': username,
                'roleName': role_name

            })

    # Crie um DataFrame do Pandas com os dados
    df = pd.DataFrame(user_info)

    # Salve o DataFrame na planilha
    spread.df_to_sheet(df, index=False, sheet=f'Database_Users_{project_id_prefix}')

    print(f'Informações de database users salvas na planilha Database_Users_{project_id_prefix} com sucesso')

else:
    print(f'Falha na solicitação. Código de status: {response.status_code}')