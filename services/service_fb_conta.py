import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from setting.config import FBSetting
from setting.standar_error import StandarError


class ServiceFBConta:

    def __init__(self) -> None:
        print("Inicio construct")
        self.cert = FBSetting.GFB_CONFIG
        if not firebase_admin._apps:
            self.cred = credentials.Certificate(self.cert)
            initialize_app(self.cred)

        self.db = firestore.client()
        self.conta_ref = self.db.collection('Contas')
        print("Fim construct")

    def create(self, payload):
        """
            create() : Add document to Firestore collection with request body
            Ensure you pass a custom ID as part of json body in post request
            e.g. json={'id': '1', 'title': 'Write a blog post'}
            Return True is inserted
        """
        try:
            id = None
            self.conta_ref.document(id).set(payload)
            return True
        except StandarError as e:
            print(f"An Error Occured: {e}")
            return False

    def findOneOrAll(self, id) -> list | None:
        """
            read() : Fetches documents from Firestore collection as JSON
            Conta : Return document that matches query ID
            all_data : Return all documents
        """
        try:
            # Check if ID was passed to URL query
            if id:
                data = self.conta_ref.document(id).get()
                return data.to_dict()
            else:
                all_data = [doc.to_dict() for doc in self.conta_ref.stream()]
                return all_data
        except StandarError as e:
            print(f"An Error Occured: {e}")
            return None

    def update(self, payload, id):
        """
            update() : Update document in Firestore collection with request body
            Ensure you pass a custom ID as part of json body in post request
            e.g. json={'id': '1', 'title': 'Write a blog post today'}
        """
        try:
            self.conta_ref.document(id).update(payload)
            return True
        except StandarError as e:
            print(f"An Error Occured: {e}")
            return False

    def delete(self, id):
        """
            delete() : Delete a document from Firestore collection
        """
        try:
            # Check for ID in URL query
            self.conta_ref.document(id).delete()
            return True
        except StandarError as e:
            print(f"An Error Occured: {e}")
            return True