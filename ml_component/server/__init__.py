# ml_component/server/__init__.py
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS 
import os 


app = Flaks(__name__)
app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)
db = SQLAlchemy(app)


import ml_component.routes