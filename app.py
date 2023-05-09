from flask import Flask, jsonify
from flask_smorest import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

import os
from db import db
import secrets
import redis

from resources.city import blp as DataBlueprint
from resources.search import blp as SearchBlueprint
from resources.user import blp as UserBlueprint

def create_app():
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "CityDataBox"
    app.config["API_VERSION"] = "V1.0"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@4.18.3/"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///city.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    migrate = Migrate(app, db)

    jwt_secret_key = secrets.token_urlsafe(32)
    app.config["JWT_SECRET_KEY"] = jwt_secret_key
    redis_client = redis.from_url(os.getenv("REDIS_URL"))
    redis_client.setex("jwt_secret_key", 86400, jwt_secret_key)

    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_token(jwt_header, jwt_payload):
        redis_client = redis.from_url(os.getenv("REDIS_URL"))
        jti = jwt_payload['jti']
        return redis_client.sismember('BLOCKLIST', jti)
    
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return jsonify({"description": "The token has been revoked.", "error": "token_revoked"})
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (jsonify({"message": "The token has expired.", "error": "token_expired"}), 401,)

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (jsonify({"message": "Signature verification failed.", "error": "invalid_token"}), 401,)

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify({"description": "Request does not contain an access token.",
                    "error": "authorization_required",}), 401,)

    api = Api(app)
    api.register_blueprint(DataBlueprint)
    api.register_blueprint(SearchBlueprint)
    api.register_blueprint(UserBlueprint)

    return app




