# ml_component/server/config.py
import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://postgres:@localhost/'
database_name = 'spotify_suggester'


class DevelopmentConfig:
    """Development configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestingConfig:
    """Testing configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig:
    """Production configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///' + database_name
