from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Boolean
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    sripe_id = Column(String(100), index = True)
    name = Column(String(100))
    surname = Column(String(100))
    email = Column(String(100))
    date_created = Column(Date)
    charges = relationship("Charge")

class Charge(Base):
    __tablename__ = 'charge'
    
    id = Column(Integer, primary_key=True)
    sripe_id = Column(String(100), index = True)
    date_created = Column(Date)
    amount = Column(Float)
    is_recurring = Column(Boolean)
    is_refunded = Column(Boolean)
    customer_id = Column(Integer, ForeignKey('customer.id'))

    

    

