from . import admin
from flask import render_template, redirect, url_for, request, session
from .forms import Register
from functools import wraps

def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_name' not in session:
            return redirect(url_for('index'))
        return decorated_function

# @admin.route('/')
# def inherit_html():
#     return render_template('admin/inherit_html.html')
@user_login_req
@admin.route('/')
def index():
    return render_template('admin/index.html')

@admin.route('/login')
def login():
    return render_template('admin/login.html')

@admin.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if request.method == "POST":
        username = request.form['user_name']
        return redirect(url_for('admin.index'))
    return render_template('admin/register.html', form=form)

@admin.route('/logout')
def logout():
    return render_template('admin/logout.html')

@admin.route('/center')
def user_center():
    return render_template('admin/user_center.html')

@admin.route('/changepwd')
def changepwd():
    return render_template('admin/changepwd.html')

@admin.route('/comment')
def comment():
    return render_template('admin/comment.html')

@admin.route('/loginout')
def loginlog():
    return render_template('admin/loginlog.html')

@admin.route('/collect')
def collect():
    return render_template('admin/collect.html')