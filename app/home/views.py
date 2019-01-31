from . import home
from flask import render_template, redirect, url_for, request, session, flash
from .forms import Register, Login
from app.models import User, Comment
from functools import wraps


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
    return render_template('home/blog.html')


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
    # if request.method == "POST":
    #     username = request.form['user_name']
    #     return redirect(url_for('home.index'))
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
        print(i.id)
        comments = Comment.query.filter_by(user_id=user_id).all()
        for i in comments:
            print(i.content)
    return render_template('home/comment.html', users=users, comments=comments)


@home.route('/loginlog')
@user_login_req
def loginlog():
    return render_template('home/loginlog.html')


@home.route('/collect')
@user_login_req
def collect():
    users = User.query.filter_by(name=session.get('account')).all()
    return render_template('home/collect.html', users=users)


@home.route('/about')
def about():
    return render_template('home/about.html')
