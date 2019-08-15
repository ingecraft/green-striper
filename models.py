from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Boolean
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    date_created = Column(Date)
    charges = relationship("Charge")

class Charge(Base):
    __tablename__ = 'charge'
    
    date_created = Column(Date)
    amount = Column(Float)
    is_recurring = Column(Boolean)
    is_refunded = Column(Boolean)
    customer_id = Column(Integer, ForeignKey('customer.id'))

    

    

