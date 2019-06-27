from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
database = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    database.init_app(app)

    from .flights import flights as flights_blueprint
    app.register_blueprint(flights_blueprint)

    return app