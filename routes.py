from flask import render_template, request
from app import app
from models import Category

@app.route('/')
def index():
    return "Hello, this is the Bookkeeping App!"

@app.route('/new_transaction', methods=['GET', 'POST'])
def new_transaction():
    if request.method == 'POST':
        # Handle form submission
        pass
    else:
        categories = Category.query.all()
        return render_template('new_transaction.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
