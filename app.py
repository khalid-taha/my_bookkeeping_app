from flask import Flask
from setup_database import init_db

app = Flask(__name__)

# Initialize the database
init_db()

# Import routes after initializing the app to avoid circular imports
import routes

if __name__ == '__main__':
    app.run(debug=True)
