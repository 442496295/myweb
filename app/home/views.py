from . import home
from flask import render_template, redirect, url_for, request, session
from .forms import Register
from functools import wraps


# def user_login_req(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'user_name' not in session:
#             return redirect(url_for('index'))
#         return decorated_function

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

@home.route('/login')
def login():
    return render_template('home/login.html')

@home.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if request.method == "POST":
        username = request.form['user_name']
        return redirect(url_for('home.index'))
    return render_template('home/register.html', form=form)

@home.route('/logout')
def logout():
    return render_template('home/logout.html')

@home.route('/center')
def user_center():
    return render_template('home/user_center.html')

@home.route('/changepwd')
def changepwd():
    return render_template('home/changepwd.html')

@home.route('/comment')
def comment():
    return render_template('home/comment.html')

@home.route('/loginlog')
def loginlog():
    return render_template('home/loginlog.html')

@home.route('/collect')
def collect():
    return render_template('home/collect.html')

@home.route('/about')
def about():
    return render_template('home/about.html')
