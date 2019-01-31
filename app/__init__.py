import sys
sys.setrecursionlimit(2000)

import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/blog"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.debug = True
db = SQLAlchemy(app)


import os
app.secret_key = os.urandom(16)


from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('home/404.html'), 404