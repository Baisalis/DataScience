# ml_component/server/__init__.py
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS 
import os 


app = Flaks(__name__)
# set config here 
db = SQLAlchemy(app)


import ml_component.routes