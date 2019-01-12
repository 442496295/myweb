from . import admin
from flask import render_template, redirect, url_for
@admin.route('/')
def index():
    return render_template('admin/inherit_html.html')