from flask import Flask
from setup_database import init_db

app = Flask(__name__)

# Initialize database
init_db()

if __name__ == '__main__':
    app.run(debug=True)
