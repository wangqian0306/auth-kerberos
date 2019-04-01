from flask import Flask
from flask import render_template
from flask_cors import CORS
from flask_kerberos import init_kerberos
from flask_kerberos import requires_authentication


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(__name__)
    CORS(app)

    @app.route('/')
    @requires_authentication
    def hello(user):
        return render_template('index.html', user=user)

    init_kerberos(app)
    return app
