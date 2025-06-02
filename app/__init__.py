from flask import Flask
from app.extensions import mongo
from app.webhook.routes import webhook 
from app.webhook.events import data_bp
import os

def create_app():

    app = Flask(__name__)
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")  # Use environment variable or default to local MongoDB
    mongo.init_app(app)  # Initializing the mongo extension with the app
    # registering all the blueprints
    app.register_blueprint(webhook)
    app.register_blueprint(data_bp)
    
    return app
