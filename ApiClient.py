import requests
from requests.auth import HTTPDigestAuth

class ApiClient:
    def __init__(self, base_url, username, password, org_id_prefix, project_id_prefix):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.org_id_prefix = org_id_prefix
        self.project_id_prefix = project_id_prefix
        self.headers = {
            'Accept': "application/vnd.atlas.2023-02-01+json"
        }

    def make_request(self, endpoint, id_prefix=None):
        # Verifique se a API busca em /orgs ou /groups
        if id_prefix is None:
            url_prefix = 'orgs/'
            id_prefix = self.org_id_prefix
        else:
            url_prefix = 'groups/'
            id_prefix = self.project_id_prefix
        url = f'{self.base_url}{url_prefix}{id_prefix}/{endpoint}'
        auth = HTTPDigestAuth(self.username, self.password)
        response = requests.get(url, auth=auth, headers=self.headers)

        return response