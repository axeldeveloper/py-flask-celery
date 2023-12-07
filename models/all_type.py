from sqlalchemy.orm import validates

from models.database import db


class AllTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.String(128))
    type_name = db.Column(db.String(128))
    disable = db.Column(db.Boolean)
    globals = db.Column(db.Boolean)

    # t.references: customer, foreign_key: true
    # t.references: company, foreign_key: true

    # from datetime import datetime
    # timestamp = db.Column(
    #     db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    # )

    @validates('type_name')
    def validate_username(self, key, value):
        if not value:
            raise ValueError("Must have a type_name")
        return value
