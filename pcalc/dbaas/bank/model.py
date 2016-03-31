from dbaas.basemodel import db, ma, CRUD

class Bank(db.Model, CRUD):
    __tablename__ = 'banks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name=''):
        self.name = name

class BankSchema(ma.ModelSchema):
    class Meta:
        model = Bank