from . import main

@main.route('/')
def index():
    return 'Bem-vindo ao DinDuo!'