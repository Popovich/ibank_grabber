from pcalc.dbaas.basemodel import db, ma, CRUD
from sqlalchemy.orm import relationship, backref

class Transaction(db.Model, CRUD):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    descr = db.Column(db.String(500), nullable=True)
    amount = db.Column(db.Numeric(precision=2))
    mcc = db.Column(db.Integer, nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    account = relationship("Account")

    authorization_date = db.Column(db.DateTime, nullable=False)
    authorized = db.Column(db.Boolean)

    post_date = db.Column(db.DateTime, nullable=True)

class TransactionSchema(ma.ModelSchema):
    class Meta:
        model = Transaction