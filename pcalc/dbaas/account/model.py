from pcalc.dbaas.basemodel import db, ma, CRUD
from sqlalchemy.orm import relationship, backref

class Account(db.Model, CRUD):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(20), nullable=False, unique=True) # номер счёта (20 цифр)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'))
    bank = relationship("Bank")

    currency_id = db.Column(db.Integer, db.ForeignKey('currencies.id'))
    currency = relationship("Currency")

class AccountSchema(ma.ModelSchema):
    class Meta:
        model = Account