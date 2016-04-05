from pcalc.dbaas.basemodel import db, ma, CRUD
from sqlalchemy.orm import relationship, backref

class Card(db.Model, CRUD):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(32), nullable=False) # Debit/Credit
    number = db.Column(db.String(16), nullable=False) # номер карты (16 цифр)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    account = relationship("Account")

    __mapper_args__ = {'polymorphic_on': type}

class DebitCard(Card):
    __tablename__ = 'debit_cards'
    __mapper_args__ = {'polymorphic_identity': 'DebitCard'}

    id = db.Column(None, db.ForeignKey('cards.id'), primary_key=True)

class CreditCard(Card):
    __tablename__ = 'credit_cards'
    __mapper_args__ = {'polymorphic_identity': 'CreditCard'}

    id = db.Column(None, db.ForeignKey('cards.id'), primary_key=True)
    credit_limit = db.Column(db.Integer, nullable=False)
    grace_period = db.Column(db.Integer, nullable=False)

class CardSchema(ma.ModelSchema):
    class Meta:
        model = Card