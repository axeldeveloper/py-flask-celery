import unittest

from dotenv import load_dotenv
load_dotenv()

class MyTestCase(unittest.TestCase):
    def test_create(self):
        """
            create() : Add document to Firestore collection with request body
            Ensure you pass a custom ID as part of json body in post request
            e.g. json={'id': '1', 'title': 'Write a blog post'}
        """

        payload = {
            "ano_comp": "2022",
            "confirmado": False,
            "created": "20/05/2022",
            "dia_comp": "20",
            "forma": "Cartão de credito Nubank",
            "id": "bea07ac5-e313-4f0f-92a8-54b7b3acfc2c",
            "mes_comp": "4",
            "nome": "Aluguel 2",
            "nparcela": 36,
            "origem": "Banco do brasil",
            "origem_tipo": "Conta corrente",
            "pagamento": "",
            "parcela": "",
            "tipo": "Despesa",
            "update": "",
            "valor": 0,
            "valor_pagamento": 0,
            "vencimento": "20/05/2022"
        }
        from services.service_fb_conta import ServiceFBConta
        ret = ServiceFBConta().create(payload)
        assert ret is not False  # add assertion here

    def test_findOneOrAll(self):
        """
            read() : Fetches documents from Firestore collection as JSON
            todo : Return document that matches query ID
            all_todos : Return all documents
        """

        # Check if ID was passed to URL query
        id = '-MV19lG2FW9l4iEzPl_d'
        from services.service_fb_conta import ServiceFBConta
        ret = ServiceFBConta().findOneOrAll(id)
        assert ret is not None  # add assertion here

    def test_update(self):
        """
            update() : Update document in Firestore collection with request body
            Ensure you pass a custom ID as part of json body in post request
            e.g. json={'id': '1', 'title': 'Write a blog post today'}
        """


        payload = {
            "ano_comp": "2021",
            "created": "05/03/2021",
            "dia_comp": "5",
            "forma": "Dinheiro",
            "mes_comp": "3",
            "nome": "Água 45",
            "nparcela": 0,
            "origem": "Banco do brasil",
            "origem_tipo": "Conta corrente",
            "pagamento": "05/03/2021",
            "parcela": 0,
            "tipo": "Despesa",
            "valor": 84.34,
            "valor_pagamento": 84.34,
            "vencimento": "05/03/2021"
        }

        id = '-MV19lG2FW9l4iEzPl_d'
        from services.service_fb_conta import ServiceFBConta
        ret = ServiceFBConta().update(payload, id)
        assert ret is not False  # add assertion here

    def test_delete(self):
        """
            delete() : Delete a document from Firestore collection
        """
        # Check for ID in URL query
        id = 'vAd6hSnTAM2rvpyNNuPq'
        from services.service_fb_conta import ServiceFBConta
        ret = ServiceFBConta().delete(id)
        assert ret is not False  # add assertion here


if __name__ == '__main__':
    unittest.main()