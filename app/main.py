from flask import Flask
from src.blueprint.app import app_route

app = Flask(__name__)
app.register_blueprint(app_route)

