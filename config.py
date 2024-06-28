from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Get DATABASE_URL from environment and convert to absolute path if necessary
db_path = os.getenv('DATABASE_URL')
if db_path and db_path.startswith('sqlite:///'):
    relative_path = db_path.replace('sqlite:///', '')
    absolute_path = os.path.abspath(relative_path)
    db_path = f'sqlite:///{absolute_path}'

class Config:
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False

print(f"Config: SQLALCHEMY_DATABASE_URI={db_path}")
