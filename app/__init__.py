import os
os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')
import sys
sys.setrecursionlimit(2000)


from flask import Flask
app = Flask(__name__)
app.secret_key = os.urandom(16)
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')