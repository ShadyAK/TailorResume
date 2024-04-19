from flask import Flask
from src.main.controller import endpoint_blueprints

app = Flask(__name__)
app.register_blueprint(endpoint_blueprints)

if __name__ == '__main__':
    app.run(debug=True)