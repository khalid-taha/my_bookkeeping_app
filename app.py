from flask import Flask
from config import Config
from models import db
from routes import app as routes_app

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(routes_app)

if __name__ == '__main__':
    app.run(debug=True)
