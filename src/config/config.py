import os
from dotenv import load_dotenv

# Ensure mysqlclient works with pymysql
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # Allow HTTP traffic for local dev

load_dotenv()  # Load environment variables from a .env file

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # e.g. "mysql+pymysql://username:password@localhost/dbname"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

