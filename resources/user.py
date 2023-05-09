from flask.views import MethodView
from flask_smorest import abort, Blueprint
from models import UserModel
from schemas import UserSchema
from passlib.hash import pbkdf2_sha256
from db import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
import redis
import os

blp = Blueprint("Users", __name__, description = " ")

@blp.route("/register")
class Register(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="Username is taken")
        if UserModel.query.filter_by(is_admin=True).count() > 0:
            abort(400, message="An admin user already exists!")

        user = UserModel(
            username = user_data["username"],
            password = pbkdf2_sha256.hash(user_data["password"]),
            is_admin = user_data["is_admin"]
        )

        db.session.add(user)
        db.session.commit()

        return {'message' : 'User created successfully!'}
    
@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username == user_data["username"] and UserModel.is_admin == True).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            return {"access_token" : access_token}
        abort(404, message="Invaild username or password")

@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        redis_client = redis.from_url(os.getenv("REDIS_URL"))
        redis_client.sadd("BLOCKLIST", jti)
        return {"message" : "Logged out"}

@blp.route("/user/<int:user_id>")
class user(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user
    
    @jwt_required()
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()
        
        return {"message" : "User deleted"}, 200