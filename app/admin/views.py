from . import admin
from flask import render_template, redirect, url_for, request, session, flash
from functools import wraps
from app.models import Admin
from app.admin.forms import LoginForm


def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(session['admin'])
        if session['admin'] == None:
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function


@admin.route('/')
@user_login_req
def index():
    cc = Admin.query.all()
    print(cc)
    return render_template('admin/index.html', cc=cc)


@admin.route('/login', methods=['GET', 'POST'])
@user_login_req
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data['account']).first()
        if not admin.check_pwd(data['pwd']):
            flash('密码错误！')
            return redirect(url_for('admin.login'))
        session['admin'] = data['account']
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template('admin/login.html', form=form)


@admin.route('/register', methods=['GET', 'POST'])
@user_login_req
def register():
    # form = Register()
    # if request.method == "POST":
    #     username = request.form['user_name']
    #     return redirect(url_for('admin.index'))
    # return render_template('admin/register.html', form=form)
    return render_template('admin/register.html')


@admin.route('/logout')
@user_login_req
def logout():
    return render_template('admin/logout.html')


@admin.route('/center')
@user_login_req
def user_center():
    return render_template('admin/user_center.html')


@admin.route('/changepwd')
@user_login_req
def changepwd():
    return render_template('admin/changepwd.html')


@admin.route('/comment')
@user_login_req
def comment():
    return render_template('admin/comment.html')


@admin.route('/loginout')
@user_login_req
def loginlog():
    session.pop()
    return render_template('admin/loginlog.html')


@admin.route('/collect')
@user_login_req
def collect():
    return render_template('admin/collect.html')
