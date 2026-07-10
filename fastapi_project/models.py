from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Invoice(Base):
    __tablename__ = "kafka_invoices"

    id = Column(Integer, primary_key=True, index=True)
    vendor = Column(String)
    amount = Column(Integer)
    status = Column(String)
