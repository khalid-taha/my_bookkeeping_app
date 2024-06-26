from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application
app = Flask(__name__)

# Configure the SQLAlchemy part of the application instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookkeeping.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Define Your Models
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Transaction {self.date} - {self.amount} - {self.category}>"

# Function to create the database and tables
def initialize_database():
    with app.app_context():
        db.create_all()
