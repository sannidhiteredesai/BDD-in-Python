import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'this-is-dev-only-secret-key'

# Import all the routes for your application
from application.routes import routes
