from flask import flask
from app import app
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

db = sqlalchemy(app)