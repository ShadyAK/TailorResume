from flask import Blueprint

endpoint_blueprints = Blueprint('endpoints', __name__)
print(' from blueprint ', __name__)
@endpoint_blueprints.route('/')
def index():
    return "HELLO WORLD"
