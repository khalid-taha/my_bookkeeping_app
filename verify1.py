from app import app, db
from models import Category

with app.app_context():
    categories = Category.query.all()
    for category in categories:
        print(category.id, category.name)

