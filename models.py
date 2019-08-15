from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    date_created = Column(Date)
    recurring_gifts = relationship("RecurringGift")


class RecurringGift(Base):
    __tablename__ = "reccuring_gift"

    id = Column(Integer, primary_key=True)
    date_created = Column(Date)
    customer_id = Column(Integer, ForeignKey('customer.id')
    


class Charge(Base):
    __tablename__ = 'charge'
    

