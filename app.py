from flask import Flask, render_template, request, redirect, url_for
from db_config import db
from config import Config  # Import the Config class

app = Flask(__name__)
app.config.from_object(Config)  # Use the configuration from config.py

# Initialize SQLAlchemy instance with the app
db.init_app(app)

@app.route('/')
def index():
    return redirect(url_for('list_transactions'))

@app.route('/new_transaction', methods=['GET', 'POST'])
def new_transaction():
    from models import Category, Transaction  # Import here to avoid circular import
    if request.method == 'POST':
        category_id = request.form['category']
        total_amount = request.form['total_amount']  # Changed
        amount = request.form['amount']  # Changed
        vat = request.form['vat']  # Changed
        description = request.form.get('description', '')  # Changed

        # Create a new transaction
        new_transaction = Transaction(total_amount=total_amount, amount=amount, vat=vat, category_id=category_id, transaction_description=description)  # Changed
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
        transaction.total_amount = request.form['total_amount']  # Changed
        transaction.amount = request.form['amount']  # Changed
        transaction.vat = request.form['vat']  # Changed
        transaction.transaction_description = request.form.get('description', '')  # Changed
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
