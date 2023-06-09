from db import db

class DataModel(db.Model):
    __tablename__ = "Data"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), unique=False, nullable=False)
    city_ascii = db.Column(db.String(80), unique=False, nullable=False)
    lat = db.Column(db.String(80), unique=False, nullable=False)
    lng = db.Column(db.String(80), unique=False, nullable=False)
    country = db.Column(db.String(80), unique=False, nullable=False)
    iso2 = db.Column(db.String(2), unique=False, nullable=False)
    iso3 = db.Column(db.String(3), unique=False, nullable=False)
    admin_name = db.Column(db.String(80), unique=False, nullable=False)
    capital = db.Column(db.String(80), unique=False, nullable=True)
    population = db.Column(db.String(80), unique=False, nullable=True)
