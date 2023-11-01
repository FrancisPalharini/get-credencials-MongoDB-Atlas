# API Client para Consulta de Credenciais no MongoDB Atlas

Este é um script Python que utiliza a API do MongoDB Atlas para consultar informações de usuários em um projeto específico e na organização usando autenticação Digest. Ele foi desenvolvido para fins de validação periódica das credenciais de acesso ao MongoDB.


## Requisitos

Para executar este script, você precisa das seguintes bibliotecas Python instaladas:

- `requests` para fazer chamadas à API.
- `python-dotenv` para carregar variáveis de ambiente de um arquivo `.env`.
- `gspread` para interagir com o Google Sheets e salvar os resultados.

Você pode instalar as dependências usando o `pip`:

pip install requests python-dotenv gspread gspread-pandas


## Configuração

Antes de executar o script, você deve configurar as variáveis de ambiente necessárias em um arquivo `.env`. Você pode criar um arquivo `.env` no mesmo diretório que o script e definir as seguintes variáveis:

- `ATLAS_BASE_URL_API`: A URL base da API do MongoDB Atlas.
- `ATLAS_USERNAME`: Seu nome de usuário para autenticação Digest.
- `ATLAS_PASSWORD`: Sua senha para autenticação Digest.
- `ATLAS_ORG_ID_PREFIX`: O do ID da organização.
- `ATLAS_PROJECT_ID_PREFIX`: O do ID do projeto.
- `PLANILHA_URL`: A URL da planilha do Google Sheets para salvar os resultados.
- `GOOGLE_SECRET_FILE`:´caminho para arquivo JSON de credenciais do Google Cloud


Um exemplo de arquivo `.env`:
```
ATLAS_BASE_URL_API=https://cloud.mongodb.com/api/atlas/v2/
ATLAS_USERNAME=seu_usuario
ATLAS_PASSWORD=sua_senha
ATLAS_ORG_ID_PREFIX=org123
ATLAS_PROJECT_ID_PREFIX=proj456
PLANILHA_URL = url_sua_planilha
GOOGLE_SECRET_FILE = "google_secret.json"
```

## Uso

Após configurar as variáveis de ambiente, você pode executar os scripts para consultar informações de usuários no MongoDB Atlas e salvar os resultados em uma planilha do Google Sheets. Há duas chamadas na api:

1. `Atlas_Users.py` : Consulta de informações de usuários e permissões a nível da organização

2. `Database_Users.py`: Consulta de informações de usuários e permissões do banco de dados no projeto definido pela variável de ambiente ATLAS_PROJECT_ID_PREFIX

Para executar o script:

`python nome_do_script.py`


Certifique-se de que o ambiente virtual, se estiver usando um, esteja ativado e que o arquivo `.env` esteja no mesmo diretório que o script.

Os resultados da consulta serão salvos na planilha do Google Sheets especificada.

**Nota:** Certifique-se de que o arquivo `google_secret.json` está na mesma pasta que o script, ou defina o caminho correto para ele na variável de ambiente `GOOGLE_SECRET_FILE` no arquivo `.env.

**Observação:** A planilha do Google Sheets deve ser compartilhada e configurada para ser acessível pela conta de serviço usada no arquivo `google_secret.json`. 
