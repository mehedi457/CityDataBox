from db import db
from sqlalchemy import event
from sqlalchemy.exc import IntegrityError

class UserModel(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

def validate_admin_count(mapper, connection, user):
    if user.is_admin and UserModel.query.filter_by(is_admin=True).count() > 0:
        raise IntegrityError('More than one admin user is not allowed')

event.listen(UserModel, 'before_insert', validate_admin_count)
event.listen(UserModel, 'before_update', validate_admin_count)