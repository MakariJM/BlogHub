#!/usr/bin/env python
from flask import Flask, request, make_response, session, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ne5by5vrhg5v7u7r' 
app.json.compact = False


db.init_app(app)
migrate = Migrate(app, db)



@app.route('/')
def index():
    return '<h1>BBlogging System</h1>'

if __name__== '_main_':
    app.run(port=5555, debug=True)