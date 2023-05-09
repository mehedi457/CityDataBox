from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import DataModel
from schemas import DataSchema, DataListSchema, PageSchema
from db import db
from sqlalchemy.exc import SQLAlchemyError
from flask import request
from flask_jwt_extended import jwt_required

blp = Blueprint("data", __name__, description = " ")

@blp.route("/cities")
class CityList(MethodView):
    @blp.response(200, PageSchema)
    def get(self):
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=100, type=int)
        data = DataModel.query.paginate(page=page, per_page=per_page)

        result = {
            'data': data,
            'page': data.page,
            'total_pages': data.pages,
            'total_data': data.total
        }
        if data.has_next:
            next_url = request.base_url + '?page=' + str(data.next_num)
            result['next'] = next_url
        return result
    
    @jwt_required()
    def delete(self):
        data = DataModel.query.all()
        for d in data:
            db.session.delete(d)
        db.session.commit()
        return {"message" : "Data deleted"}

    @jwt_required()
    @blp.arguments(DataListSchema)
    def post(self, data):
        try:
            for d in data["cities"]:
                data = DataModel(**d)
                db.session.add(data)
            db.session.commit()
            return {"message" : "Successfully added"}
        except SQLAlchemyError as e:
            abort(500, message=f"{e}")

@blp.route("/city")
class City(MethodView):
    @jwt_required()
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
    @jwt_required()
    def delete(self, id):
        data = DataModel.query.get_or_404(id)
        db.session.delete(data)
        db.session.commit()
        return {"message" : "Data deleted"}