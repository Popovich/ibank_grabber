from sqlalchemy import Column
from sqlalchemy.types import Integer, String

class Bank(object):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    def __init__(self, name=''):
        self.name = name

    def __repr__(self):
        return "<Bank('%s')" % self.name