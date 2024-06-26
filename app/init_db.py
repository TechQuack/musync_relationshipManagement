import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import func, create_engine
from sqlalchemy.orm import sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tech:quack@database_relationship_management:5432/main'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


Session = sessionmaker()
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session.configure(bind=engine)
