from db_config import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    transactions = db.relationship("Transaction", back_populates="category")

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    total_amount = db.Column(db.Double, nullable=False)  # Changed
    amount = db.Column(db.Double, nullable=False)  # Changed
    vat = db.Column(db.Double, nullable=False)  # Changed
    transaction_description = db.Column(db.String, nullable=True)  # Changed
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship("Category", back_populates="transactions")
