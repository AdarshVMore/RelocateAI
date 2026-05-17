import firebase_admin
from firebase_admin import credentials, auth
import os

_initialized = False

def _init():
    global _initialized
    if _initialized:
        return
    key_path = os.environ.get("FIREBASE_SERVICE_ACCOUNT_PATH", "serviceAccountKey.json")
    cred = credentials.Certificate(key_path)
    firebase_admin.initialize_app(cred)
    _initialized = True

def verify_firebase_token(id_token):
    _init()
    try:
        return auth.verify_id_token(id_token)
    except Exception:
        return None