from flask import Flask
from flask_smorest import Api
import os
from db import db
from resources.city import blp as DataBlueprint
from resources.search import blp as SearchBlueprint
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "MY First Rest API"
    app.config["API_VERSION"] = "V1.0"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///city.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app=app)

    migrate = Migrate(app, db)

    api = Api(app=app)

    api.register_blueprint(DataBlueprint)
    api.register_blueprint(SearchBlueprint)

    return app




