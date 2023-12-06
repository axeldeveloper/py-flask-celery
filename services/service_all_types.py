from models.all_type import AllTypes
from models.all_type_schema import AllTypeSchema
from models.database import db
from sqlalchemy import exc


class ServiceAllTypes:

    def __init__(self):
        self.schemas = AllTypeSchema(many=True)
        self.schema = AllTypeSchema()

    def findAll(self):
        rows = AllTypes.query.all()
        return self.schemas.dump(rows)

    def findOne(self, id):
        row = AllTypes.query.get_or_404(id)
        return self.schema.dump(row)

    def create(self, data):
        try:
            new_user = AllTypes(
                name=data['name'],
                description=data['description'],
                type_name=data['type_name'],
                disable=data['disable'],
                globals=data['globals']
            )
            db.session.add(new_user)
            db.session.commit()
            return True, self.schema.dump(data)
        except exc.SQLAlchemyError as e:
            print(e)
            return False, {'message': 'Error create', 'trace': e}

    def update(self, data, id):
        try:
            row = AllTypes.query.filter_by(id=id).first()
            if row:
                row.name = data['name']
                row.description = data['description']
                db.session.commit()
                load_data = self.schema.load(data, session=db.session)
                print(">>>>>" * 20)
                print(load_data)
                return True, self.schema.dump(data)
            return {'message': 'AllTypes not found'}
        except exc.SQLAlchemyError as e:
            return False, {'message': 'Error update', 'trace': e}

    def delete(self, id):
        try:
            row = AllTypes.query.get_or_404(id)
            db.session.delete(row)
            db.session.commit()
            return True, self.schema.dump(row)
        except exc.SQLAlchemyError as e:
            return False, {'message': 'Error delete AllTypes not found', 'trace': e}