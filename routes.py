from flask import render_template, request
from app import app
from models import Category

@app.route('/')
def index():
    print("Index route accessed")
    return "Hello, this is the Bookkeeping App!"

@app.route('/new_transaction', methods=['GET', 'POST'])
def new_transaction():
    print("New transaction route accessed")
    if request.method == 'POST':
        # Handle form submission
        pass
    else:
        categories = Category.query.all()
        return render_template('new_transaction.html', categories=categories)
