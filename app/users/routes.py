from flask import render_template
from . import users

@users.route('/register')
def register():
    return render_template('users/register.html')