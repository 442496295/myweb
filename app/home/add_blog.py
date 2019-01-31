from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/blog"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

from app.models import Blog


blog1 = Blog(title='flask学习', info='Flask 数据库调用教程',
             looknum=2131, content='以上文字皆由数据库调用而出,便于学习数据库', commentnum=222, length=84, )
db.session.add(blog1)
db.session.commit()


