from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import DataModel
from schemas import DataSchema, DataListSchema
from db import db
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("data", __name__, description = " ")

@blp.route("/city/all")
class CityList(MethodView):
    @blp.response(200, DataSchema(many=True))
    def get(self):
        return DataModel.query.all()
    
    def delete(self):
        data = DataModel.query.all()
        for d in data:
            db.session.delete(d)
        db.session.commit()
        return {"message" : "Data Deleted"}

    @blp.arguments(DataListSchema)
    def post(self, data):
        try:
            for d in data["cities"]:
                data = DataModel(**d)
                db.session.add(data)
            db.session.commit()
            return {"message" : "Succefully added"}
        except SQLAlchemyError as e:
            abort(500, message=f"{e}")

@blp.route("/city")
class City(MethodView):
    @blp.arguments(DataSchema)
    @blp.response(201, DataSchema)
    def post(self, data):
        data = DataModel(**data)
        try:
            db.session.add(data)
            db.session.commit()

        except SQLAlchemyError as e:
            abort(500, message=f"{e}")
        return data
    
@blp.route("/city/<int:id>")
class CityDelete(MethodView):
    def delete(self, id):
        data = DataModel.query.get_or_404(id)
        db.session.delete(data)
        db.session.commit()
        return {"message" : "Data Deleted"}