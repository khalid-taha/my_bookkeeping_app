from flask import Flask
from setup_database import init_db

app = Flask(__name__)

# Initialize database
init_db()

import routes  # Ensure routes are imported after initializing the app

if __name__ == '__main__':
    app.run(debug=True)
