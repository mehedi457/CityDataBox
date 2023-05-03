from marshmallow import Schema, fields

class DataSchema(Schema):
    id = fields.Int(dump_only=True)
    city = fields.Str(required=True)
    city_ascii = fields.Str(required=True)
    lat = fields.Float(required=True)
    lng =  fields.Float(required=True)
    country = fields.Str(required=True)
    iso2 = fields.Str(required=True)
    iso3 = fields.Str(required=True)
    admin_name = fields.Str(required=True)
    capital = fields.Str(required=True)
    population = fields.Int(required=True)

