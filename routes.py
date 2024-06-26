from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import Transaction, db

app = Blueprint('app', __name__)

@app.route('/')
def index():
    transactions = Transaction.query.all()
    return render_template('index.html', transactions=transactions)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    date = request.form['date']
    amount = request.form['amount']
    category = request.form['category']
    description = request.form['description']
    new_transaction = Transaction(date=date, amount=amount, category=category, description=description)
    db.session.add(new_transaction)
    db.session.commit()
    return redirect(url_for('app.index'))

@app.route('/update_transaction/<int:id>', methods=['GET', 'POST'])
def update_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    if request.method == 'POST':
        transaction.date = request.form['date']
        transaction.amount = request.form['amount']
        transaction.category = request.form['category']
        transaction.description = request.form['description']
        db.session.commit()
        return redirect(url_for('app.index'))
    return render_template('update_transaction.html', transaction=transaction)

@app.route('/delete_transaction/<int:id>', methods=['POST'])
def delete_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for('app.index'))
