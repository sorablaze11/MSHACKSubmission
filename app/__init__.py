from flask import Flask

app = Flask(__name__)
wsgi_app = app.wsgi_app #Registering with IIS
from app import routes
