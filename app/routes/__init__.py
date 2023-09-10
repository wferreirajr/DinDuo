from flask import Blueprint

# Crie um Blueprint
routes = Blueprint('routes', __name__)

# Importa os módulos de rotas para garantir que as rotas sejam registradas no Blueprint
from . import users, auth, transactions, users, families
