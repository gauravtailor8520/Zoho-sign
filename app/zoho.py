import requests
import os

class ZohoSign:
    def __init__(self):
        self.client_id = os.getenv('ZOHO_CLIENT_ID')
        self.client_secret = os.getenv('ZOHO_CLIENT_SECRET')
        self.redirect_uri = os.getenv('ZOHO_REDIRECT_URI')
        self.auth_url = os.getenv('ZOHO_AUTH_URL')
        self.token_url = os.getenv('ZOHO_TOKEN_URL')
        self.api_base = os.getenv('ZOHO_SIGN_API_BASE')

    def get_auth_url(self):
        return f"{self.auth_url}?client_id={self.client_id}&response_type=code&redirect_uri={self.redirect_uri}&scope=ZohoSign.documents.ALL"

    def get_access_token(self, code):
        data = {
            'code': code,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code'
        }
        response = requests.post(self.token_url, data=data)
        return response.json()

    def create_signing_request(self, access_token, template_id):
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            "templates": [{
                "template_id": template_id,
                "actions": [{
                    "role": "signer",
                    "is_embedded": True
                }]
            }]
        }
        response = requests.post(
            f"{self.api_base}/requests",
            headers=headers,
            json=data
        )
        return response.json()

# app/routes.py
