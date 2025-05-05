import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
PATH_SERVICE_ACCOUNT = "credentials.json"
cred = credentials.Certificate(PATH_SERVICE_ACCOUNT)
firebase_admin.initialize_app(cred)
db = firestore.client()