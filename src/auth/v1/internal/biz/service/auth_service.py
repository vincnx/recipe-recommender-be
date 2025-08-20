import google_auth_oauthlib.flow
from google.oauth2 import id_token
from google.auth.transport import requests
from ...adapter.repo.auth_repo import AuthRepo
from flask import session

class AuthService:
    def __init__(self, oauth_config, auth_repo: AuthRepo):
        self.flow = None
        self.oauth_config = oauth_config
        self.auth_repo = auth_repo
        self._load_flow()

    def get_authorization_url(self, state = None):
        authorization_url, state = self.flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true',
            prompt='consent',
            state=state
        )
        return authorization_url, state

    def google_login(self, code: str):
        try:
            self.flow.fetch_token(code=code)
            
            credentials = self.flow.credentials
            
            id_info = id_token.verify_oauth2_token(
                credentials.id_token, 
                requests.Request(), 
                self.oauth_config['client_id']
            )
            
            user_info = {
                'email': id_info['email'],
                'name': id_info.get('name'),
                'picture': id_info.get('picture'),
                'collections': []
            }
            
            user = self.auth_repo.find_user(user_info['email'])
            if not user:
                user_info['_id'] = str(self.auth_repo.insert_user(user_info))
            else:
                user_info['_id'] = str(user['_id'])
            
            session['user'] = user_info
            session['access_token'] = credentials.token
            
            return {
                'success': True,
                'user': user_info,
                'access_token': credentials.token,
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def get_current_user(self):
        user = session.get('user')
        if not user:
            return None
        return user

    def logout(self):
        session.clear()
        return {'success': True}

    def _load_flow(self):
        self.flow = google_auth_oauthlib.flow.Flow.from_client_config(
            {
                "web": {
                    "client_id": self.oauth_config['client_id'],
                    "client_secret": self.oauth_config['client_secret'],
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "redirect_uris": ["http://localhost:5173/callback"]
                }
            },
            scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
        )
        self.flow.redirect_uri = self.oauth_config['callback_url']