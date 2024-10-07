# IMPORTS
from flask import request, session, abort
from flask_restful import Resource
from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError
import traceback

load_dotenv()

# Local imports
from config import app, db, api, os

# Add your model imports
from models import *

#secret_key
app.secret_key = os.getenv('SECRET_KEY')

if __name__ == "__main__":
    app.run(debug=True)