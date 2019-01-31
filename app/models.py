from datetime import datetime
from app import db

# 会员
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text, default=None)       # 个性简介
    face = db.Column(db.String(255), unique=True, default=None)   # 头像
    addtime = db.Column(db.DATETIME, index=True, default=datetime.utcnow)
    uuid = db.Column(db.String(255), unique=True)   # 唯一标识符
    userlogs = db.relationship("Userlog", backref='user')  # 会员日志外键关联
    comments = db.relationship('Comment', backref='user')   # 评论外键关系关联
    blogcols = db.relationship('Blogcol', backref='user')  # 收藏外键关系关联
    def __repr__(self):
        return "<User %r>" % self.name

# 会员登陆日志
class Userlog(db.Model):
    __tablename__ = 'userlog'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # 所属会员
    ip = db.Column(db.String(100))      # 登陆ip
    addtion = db.Column(db.DATETIME, index=True, default=datetime.utcnow)   # 登陆时间

    def __repr__(self):
        return "<Userlog &r>" % self.id


# 标签
class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    addtion = db.Column(db.DATETIME, index=True, default=datetime.utcnow)
    blogs = db.relationship('Blog', backref='tag')  # 博客外键关系关联

    def __str__(self):
        return "<Tag %r>" % self.name

class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)   # 简介
    looknum = db.Column(db.BigInteger)
    content = db.Column(db.Text)
    commentnum = db.Column(db.BigInteger)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    length = db.Column(db.String(100))
    addtime = db.Column(db.DATETIME, index=True, default=datetime.utcnow)   # 添加时间
    comments = db.relationship('Comment', backref='blog')
    blogcols = db.relationship('Blogcol', backref='blog')

    def __repr__(self):
        return "<Movie %r>" % self.title



# 评论
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))     # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))       # 所属用户
    addtime = db.Column(db.DATETIME, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Comment %r>" % self.id

# 博客收藏
class Blogcol(db.Model):
    __tablename__ = "blogcol"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))     # 所属博客
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))       # 所属用户
    addtime = db.Column(db.DATETIME, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Blogcol %r>" % self.id

# 权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DATETIME, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Auth %r>" % self.name

# 角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    auths = db.Column(db.String(600))
    addtime = db.Column(db.DATETIME, index=True, default=datetime.utcnow)
    admins = db.relationship('Admin', backref='role')

    def __repr__(self):
        return "<Role %r>" % self.name

# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)  # 是否为超级管理员
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 所属角色
    addtime = db.Column(db.DATETIME, index=True, default=datetime.utcnow)
    adminlogs = db.relationship('Adminlog', backref='admin')
    oplogs = db.relationship('Oplog', backref='admin')

    def __repr__(self):
        return "<User %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)

# 会员登陆日志
class Adminlog(db.Model):
    __tablename__ = 'adminlog'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id')) # 所属会员
    ip = db.Column(db.String(100))      # 登陆ip
    addtion = db.Column(db.DATETIME, index=True, default=datetime.utcnow)   # 登陆时间


    def __repr__(self):
        return "<Adminlog &r>" % self.id

# 操作日志
class Oplog(db.Model):
    __tablename__ = 'oplog'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id')) # 所属会员
    ip = db.Column(db.String(100))      # 登陆ip
    reason = db.Column(db.String(600))      # 操作原因
    addtion = db.Column(db.DATETIME, index=True, default=datetime.utcnow)   # 登陆时间

    def __repr__(self):
        return "<Oplog &r>" % self.id


if __name__ == '__main__':
    db.create_all()




    # print(admin.pwd)

