from dbaas.basemodel import db, ma, CRUD
from sqlalchemy.orm import relationship, backref

class Card(db.Model, CRUD):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'))
    bank = relationship("Bank", backref=backref('banks'))

class CardSchema(ma.ModelSchema):
    class Meta:
        model = Card