from flask import Flask, render_template, request
from db_config import db
from setup_database import init_db

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Initialize the database
with app.app_context():
    init_db()

@app.route('/')
def index():
    return "Hello, this is the Bookkeeping App!"

@app.route('/new_transaction', methods=['GET', 'POST'])
def new_transaction():
    from models import Category  # Import here to avoid circular import
    if request.method == 'POST':
        # Handle form submission
        pass
    else:
        categories = Category.query.all()
        return render_template('new_transaction.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
