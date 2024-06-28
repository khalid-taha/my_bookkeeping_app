from db_config import db
from sqlalchemy import Date

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    transactions = db.relationship("Transaction", back_populates="category")

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    transaction_date = db.Column(Date, nullable=False)  # Changed to Date
    total_amount = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    vat = db.Column(db.Float, nullable=False)
    transaction_description = db.Column(db.String, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship("Category", back_populates="transactions")
