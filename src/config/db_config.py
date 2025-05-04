import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
PATH_SERVICE_ACCOUNT = "credentials.json"
cred = credentials.Certificate(PATH_SERVICE_ACCOUNT)
firebase_admin.initialize_app(cred)
db = firestore.client()

# validad conexion
def validate_connection():
    try:
        test_ref = db.collection("test_collection").limit(1).get()
        if test_ref:
            print("Connection to Firestore is successful.")
        else:
            print("Connection to Firestore failed.")
    except Exception as e:
        print(f"Error connecting to Firestore: {e}")

validate_connection()