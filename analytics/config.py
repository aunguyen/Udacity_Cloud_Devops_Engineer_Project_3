import logging
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Environment variables for database connection
db_username = os.getenv("DB_USER", "myuser")
db_password = os.getenv("DB_PASSWORD", "mypassword")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME", "mydatabase")

# Flask and SQLAlchemy setup
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
db = SQLAlchemy(app)

# Set logging level to DEBUG
app.logger.setLevel(logging.DEBUG)
