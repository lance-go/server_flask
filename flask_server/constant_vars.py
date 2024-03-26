from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
import os

load_dotenv()

cred = credentials.Certificate("/etc/secrets/key.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

stripe_keys = {
    "secret_key": os.environ.get('SECRET_KEY'),
    "publishable_key": os.environ.get('PUBLISHABLE_KEY'),
}

endpoint_secret = os.environ.get('ENDPOINT_SECRET')
