from models.all_type import AllTypes
#from models.database import db
from flask_seeder import Seeder, Faker, generator



# All seeders inherit from Seeder
class AllTypeSeeder(Seeder):
    # run() will be called by Flask-Seeder
    def run2(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
        cls=AllTypes,
        init={
                #"id_num": generator.Sequence(),
                "name": generator.Name(),
                #"description": generator.Integer(start=20, end=100)
                "description": generator.Name(),
                "type_name": "555-1234",
                "disable":False,
                "globals":True
            }
        )

        # Create 5 users
        for a in faker.create(5):
            print("Adding user: %s" % a)
            self.db.session.add(a)


    def run(self):
        # Dados de exemplo
        rows = [
            AllTypes(name="PESSOA JURIDICA", description="PESSOA JURIDICA", type_name= "type_person", disable=False, globals=True ),
            AllTypes(name="PESSOA FISICA", description="PESSOA FISICA", type_name= "type_person", disable=False, globals=True ),
            AllTypes(name="DINHEIRO", description="DINHEIRO", type_name= "payment_method", disable=False, globals=True ),
            AllTypes(name="DEPOSITO", description="DINHEIRO", type_name= "payment_method", disable=False, globals=True ),
            AllTypes(name="Metro(s)",description="unity", type_name= "payment_method", disable=False, globals=True ),
            AllTypes(name="Quilo(s)", description="unity", type_name= "payment_method", disable=False, globals=True ),
            AllTypes(name="Gramas", description="unity", type_name= "payment_method", disable=False, globals=True ),
            AllTypes(name="CLIENTE COM RESTRIÇÃO", description="CLIENTE COM RESTRIÇÃO", type_name= "evaluation", disable=False, globals=True ),
            AllTypes(name="AXIS PRODUTOS SIDERURGICOS", description="AXIS PRODUTOS SIDERURGICOS", type_name= "product_category", disable=False, globals=True ),
            AllTypes(name="Placa de Metal", description="Placa de Metal", type_name="product_type", disable=False, globals=True ),
            AllTypes(name="MDF", description="MDF", type_name="product_type", disable=False, globals=True ),
            AllTypes(name="R$", description="RS", type_name="coin", disable=False, globals=True ),
            AllTypes(name="U$", description="US", type_name="coin", disable=False, globals=True ),
            AllTypes(name="FUNCIONARIO", description="FUNCIONARIO", type_name="occupation", disable=False, globals=True ),
            AllTypes(name="CONTABILIDADE", description="CONTABILIDADE", type_name="occupation", disable=False, globals=True ),
            AllTypes(name="BRASIL", description="BRASIL", type_name="country", disable=False, globals=True ),
            AllTypes(name="COMPRAS", description="COMPRA", type_name="user_sector", disable=False, globals=True ),
            AllTypes(name="VENDAS", description="VENDAS", type_name="user_sector", disable=False, globals=True ),
            AllTypes(name="ESCRITORIO", description="ESCRITORIO", type_name="type_address", disable=False, globals=True ),         
            AllTypes(name="RESIDENCIAL", description="RESIDENCIAL", type_name="type_address", disable=False, globals=True ),
            AllTypes(name="MT2", description="MT2", type_name="unity", disable=False, globals=True ),
            AllTypes(name="UN", description="UN", type_name="unity", disable=False, globals=True ),
            AllTypes(name="KG", description="KG", type_name="unity", disable=False, globals=True ),               
            AllTypes(name="SEM EXEMPLO REAL", description="SEM EXEMPLO REAL", type_name="operation", disable=False, globals=True ),
            AllTypes(name="ESTOQUE INTERNO", description="ESTOQUE INTERNO", type_name="stock_type", disable=False, globals=True ),            
            AllTypes(name="ESTOQUE RESERVA", description="ESTOQUE RESERVA", type_name="stock_type", disable=False, globals=True ),
        ]

        # Adicionar cada empresa ao banco de dados
        for c in rows:
             self.db.session.add(c)

        # Commit para salvar as mudanças
        self.db.session.commit()


