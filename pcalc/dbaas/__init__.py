from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    # init Flask-SQLAlchemy
    from .basemodel import db
    db.init_app(app)

    # init Flask-marshmallow
    from .basemodel import ma
    ma.init_app(app)

    # Create database
    with app.app_context():
        db.create_all()

    from .endpoints import rest_api
    rest_api.init_app(app)

    return app