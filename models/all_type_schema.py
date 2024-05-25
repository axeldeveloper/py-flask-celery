from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.all_type import AllTypes


class AllTypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AllTypes
        load_instance = True
