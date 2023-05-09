from marshmallow import Schema, fields

class DataSchema(Schema):
    id = fields.Int(dump_only=True)
    city = fields.Str(required=True)
    city_ascii = fields.Str(required=True)
    lat = fields.Str(required=True)
    lng =  fields.Str(required=True)
    country = fields.Str(required=True)
    iso2 = fields.Str(required=True)
    iso3 = fields.Str(required=True)
    admin_name = fields.Str(required=True)
    capital = fields.Str(required=True)
    population = fields.Str(required=True)

class DataListSchema(Schema):
    cities = fields.List(fields.Nested(DataSchema()))

class PageSchema(Schema):
    data = fields.List(fields.Nested(DataSchema()), dump_only=True)
    page = fields.Int(dump_only=True)
    total_pages = fields.Int(dump_only=True)
    total_data =  fields.Int(dump_only=True)
    next = fields.Str(dump_only=True)

class UserSchema(Schema):
    id= fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    is_admin = fields.Boolean(required=True)