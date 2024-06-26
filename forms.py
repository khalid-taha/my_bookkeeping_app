from flask_wtf import FlaskForm
from wtforms import SelectField
from models import Category

class TransactionForm(FlaskForm):
    category = SelectField('Category', choices=[(cat.id, cat.name) for cat in Category.query.all()])
    # other form fields
