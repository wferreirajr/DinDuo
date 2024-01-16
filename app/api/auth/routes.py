from . import auth

@auth.route('/login')
def login():
    return 'Página de login'
    