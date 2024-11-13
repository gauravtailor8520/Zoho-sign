from flask import Flask
from flask_session import Session
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SESSION_TYPE'] = 'filesystem'
    
    Session(app)
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app

# app/zoho.py
