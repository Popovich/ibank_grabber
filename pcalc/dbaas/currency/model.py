from pcalc.dbaas.basemodel import db, ma, CRUD

class Currency(db.Model, CRUD):
    __tablename__ = 'currencies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(3), nullable=False, unique=True) # in ISO 4217 format (RUB, USD, etc)

    def __init__(self, name=''):
        self.name = name

class CurrencySchema(ma.ModelSchema):
    class Meta:
        model = Currency