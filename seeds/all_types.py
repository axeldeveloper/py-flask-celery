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
            AllTypes(name="Acme Corporation", description="123 Elm St", type_name="555-1234", disable=False, globals=True ),
            AllTypes(name="Globex Corporation", description="456 Oak St", type_name="555-5678", disable=False, globals=True ),
            AllTypes(name="Soylent Corp", description="789 Pine St", type_name="555-9012", disable=False, globals=True )
        ]

        # Adicionar cada empresa ao banco de dados
        for c in rows:
             self.db.session.add(c)

        # Commit para salvar as mudanças
        self.db.session.commit()


