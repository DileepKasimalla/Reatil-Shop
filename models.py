from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Debt(Base):
    __tablename__ = "debts"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    item = Column(JSONB)                 # <-- FIX
    cost = Column(JSONB)                 # <-- FIX
    total_cost = Column(Float)
    date = Column(DateTime(timezone=True), server_default=func.now())
    repaid = Column(Boolean, default=False)


class Advance(Base):
    __tablename__ = "advances"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    amount = Column(Float)
    used_amount = Column(Float, default=0)
    pending_amount = Column(Float)
    date = Column(DateTime(timezone=True), server_default=func.now())
    repaid = Column(Boolean, default=False)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    min_price = Column(Float)
    max_price = Column(Float)
