from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import app_active, app_config

config = app_config[app_active]

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app=app)