from sqlalchemy.orm import validates
from models.database import db
from datetime import datetime


class AllTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.String(128))
    type_name = db.Column(db.String(128))
    disable = db.Column(db.Boolean)
    globals = db.Column(db.Boolean)

    # t.references: customer, foreign_key: true
    # t.references: company, foreign_key: true

    create_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @validates('type_name')
    def validate_username(self, key, value):
        if not value:
            raise ValueError("Must have a type_name")
        return value
    
    def __str__(self):
        return "ID=%d, Name=%s, Globals=%d" % (self.id, self.name, self.globals)
