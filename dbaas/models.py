from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()
ma = Marshmallow()

# Class to add, update and delete data via SQLALchemy sessions
class CRUD():   

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()   
 
    def update(self):
        return db.session.commit()
 
    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

class Bank(db.Model, CRUD):
    __tablename__ = 'banks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name=''):
        self.name = name

class BankSchema(ma.ModelSchema):
    class Meta:
        model = Bank

class Card(db.Model, CRUD):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'))
    bank = relationship("Bank", backref=backref('banks'))

class CardSchema(ma.ModelSchema):
    class Meta:
        model = Card