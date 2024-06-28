from flask import Flask, render_template, request, redirect, url_for
from db_config import db
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# Print the database URI to ensure it's correctly loaded
print(f"App Config: SQLALCHEMY_DATABASE_URI={app.config['SQLALCHEMY_DATABASE_URI']}")

# Initialize SQLAlchemy instance with the app
try:
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Ensure all tables are created within app context
    print("Database initialized and tables created successfully.")
except Exception as e:
    print(f"Error initializing the database: {e}")

@app.route('/')
def index():
    return redirect(url_for('list_transactions'))

@app.route('/new_transaction', methods=['GET', 'POST'])
def new_transaction():
    from models import Category, Transaction
    if request.method == 'POST':
        category_id = request.form['category']
        total_amount = request.form['total_amount']
        amount = request.form['amount']
        vat = request.form['vat']
        description = request.form.get('description', '')

        new_transaction = Transaction(
            total_amount=total_amount, 
            amount=amount, 
            vat=vat, 
            category_id=category_id, 
            transaction_description=description
        )
        db.session.add(new_transaction)
        db.session.commit()

        return redirect(url_for('list_transactions'))
    else:
        categories = Category.query.all()
        return render_template('new_transaction.html', categories=categories)

@app.route('/edit_transaction/<int:id>', methods=['GET', 'POST'])
def edit_transaction(id):
    from models import Category, Transaction
    transaction = Transaction.query.get(id)
    if request.method == 'POST':
        transaction.category_id = request.form['category']
        transaction.total_amount = request.form['total_amount']
        transaction.amount = request.form['amount']
        transaction.vat = request.form['vat']
        transaction.transaction_description = request.form.get('description', '')
        db.session.commit()
        return redirect(url_for('list_transactions'))
    else:
        categories = Category.query.all()
        return render_template('edit_transaction.html', transaction=transaction, categories=categories)

@app.route('/delete_transaction/<int:id>', methods=['POST'])
def delete_transaction(id):
    from models import Transaction
    transaction = Transaction.query.get(id)
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for('list_transactions'))

@app.route('/transactions')
def list_transactions():
    from models import Transaction
    transactions = Transaction.query.all()
    return render_template('transactions.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)
