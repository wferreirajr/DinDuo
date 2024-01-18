from flask import render_template
from . import main

import os
print(os.path.abspath('app/main/templates'))

@main.route('/')
def index():
    return render_template('index.html')
