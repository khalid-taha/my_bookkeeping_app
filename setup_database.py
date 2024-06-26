from db_config import db
from models import Category, Transaction

def init_db():
    db.create_all()

if __name__ == '__main__':
    from app import app
    with app.app_context():
        init_db()
    print("Database initialized successfully.")
