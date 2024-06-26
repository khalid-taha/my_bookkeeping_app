from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from setup_database import Base

class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'extend_existing': True}  # Add this line
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    transactions = relationship("Transaction", back_populates="category")

class Transaction(Base):
    __tablename__ = 'transactions'
    __table_args__ = {'extend_existing': True}  # Add this line
    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="transactions")
