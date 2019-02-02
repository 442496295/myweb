from . import home
from flask import render_template, redirect, url_for, request, session, flash
from .forms import Register, Login, AddBlog
from app.models import User, Comment, Blog, Userlog
from functools import wraps
from app import db

def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('account') == None:
            return redirect(url_for('home.login'))
        return f(*args, **kwargs)
    return decorated_function


# @admin.route('/')
# def inherit_html():
#     return render_template('admin/inherit_html.html')
# @user_login_req
@home.route('/')
def index():
    # result = B.query.all()
    return render_template('home/blog.html')


@home.route('/blog')
def blog():
    blogs = Blog.query.all()
    return render_template('home/blog.html', blogs=blogs)


@home.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if request.method == "POST":
        account = request.form.get('account')
        pwd = request.form.get('pwd')
        user = User.query.filter_by(name=account).all()
        for i in user:
            if account != i.name:
                flash(u'用户不存在 ')
            elif pwd != i.pwd:
                flash(u'密码不正确')
            else:
                session['account'] = account
                return redirect(url_for('home.user_center'))
    return render_template('home/login.html', form=form)


@home.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        user_pwd = request.form.get('user_pwd')
        user_email = request.form.get('user_email')
        user_phone = request.form.get('user_phone')
        user = User(name=user_name, pwd=user_pwd, email=user_email, phone=user_phone)
        db.session.add(user)
        db.session.commit()
        flash('添加成功')
        session['account'] = user_name
        return render_template('home/user_center.html')
    return render_template('home/register.html', form=form)


@home.route('/logout')
@user_login_req
def logout():
    session.pop('account')
    return render_template('home/logout.html')


@home.route('/center')
@user_login_req
def user_center():
    users = User.query.filter_by(name=session.get('account')).all()
    return render_template('home/user_center.html', users=users)


@home.route('/changepwd')
@user_login_req
def changepwd():
    users = User.query.filter_by(name=session.get('account')).all()
    return render_template('home/changepwd.html', users=users)


@home.route('/comment')
@user_login_req
def comment():
    users = User.query.filter_by(name=session.get('account')).all()
    for i in users:
        user_id = i.id
        comments = Comment.query.filter_by(user_id=user_id).all()
        for i in comments:
            print(i.content)
    return render_template('home/comment.html', users=users, comments=comments)


@home.route('/loginlog')
@user_login_req
def loginlog():
    users = User.query.filter_by(name=session.get('account')).all()
    for i in users:
        user_id = i.id
        user = session.get('account')
        user_log = Userlog(user_id=user_id)
        db.session.add(user_log)
        db.session.commit()
        userlog = Userlog.query.all()
    return render_template('home/loginlog.html', user=user, userlog=userlog)


@home.route('/collect')
@user_login_req
def collect():
    users = User.query.filter_by(name=session.get('account')).all()
    return render_template('home/collect.html', users=users)


@home.route('/about')
def about():
    return render_template('home/about.html')

@home.route('/add_blog', methods=['GET', 'POST'])
@user_login_req
def add_blog():
    form = AddBlog()
    if request.method == "POST":
        title = request.form.get('title')
        info = request.form.get('info')
        text = request.form.get('text')
        user = User.query.filter_by(name=session.get('account')).all()
        for i in user:
            blog = Blog(title=title, info=info, content=text, user_id=i.id)
            db.session.add(blog)
            db.session.commit()
            flash('添加成功')
    return render_template('home/add_blog.html', form=form)

@home.route('/add_blog', methods=['GET', 'POST'])
def all_blog():
    users = User.query.filter_by(name=session.get('account')).all()
    for i in users:
        user_id = i.id
        blogs = Blog.query.filter_by(user_id=user_id).all()
        for i in blogs:
            print(i.content)
        return render_template('home/all_blog.html', users=users, blogs=blogs)


@home.route('/add_blog', methods=['GET', 'POST'])
@user_login_req
def del_blog():
    return redirect(url_for('home.blog'))



@home.route('/add_blog', methods=['GET', 'POST'])
@user_login_req
def change_blog():
    pass


