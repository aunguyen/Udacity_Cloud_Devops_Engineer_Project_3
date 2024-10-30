import logging
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Environment variables for database connection
db_username = os.getenv("DB_USER", "auntk")
db_password = os.getenv("DB_PASSWORD", "auntkP@ssword")
db_host = os.getenv("DB_HOST", "auntk-postgres")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME", "auntk_prj3_db")

# Flask and SQLAlchemy setup
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
db = SQLAlchemy(app)

# Set logging level to DEBUG
app.logger.setLevel(logging.DEBUG)
