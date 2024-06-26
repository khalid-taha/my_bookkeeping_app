from app import app, db
from models import Category

with app.app_context():
    categories = Category.query.all()
    for category in categories:
        print(category.id, category.name)

with app.app_context():
    categories = [
        "Purchases",
        "Sales",
        "Purchase Returns",
        "Sales Returns",
        "Receipts",
        "Payments",
        "Petty Cash Expenses",
        "Asset Purchases and Adjustments",
        "Corrections and Adjustments"
    ]

    for category_name in categories:
        category = Category(name=category_name)
        db.session.add(category)
    
    db.session.commit()
    print("Categories added successfully.")

