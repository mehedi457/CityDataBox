from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import DataModel
from schemas import DataSchema, PageSchema
from sqlalchemy import func
from flask import request

blp = Blueprint("search", __name__, description = " ")

@blp.route("/city/<string:name>")
class SearchByCityName(MethodView):
    @blp.response(200, DataSchema)
    def get(self, name):
        data = DataModel.query.filter(func.lower(DataModel.city) == func.lower(name)).first()
    
        if not data:
            abort(404, message=f"No data found for city {name}")
        
        return data
       
@blp.route("/city/<int:id>")
class SearchById(MethodView):
    @blp.response(200, DataSchema)
    def get(self, id):
        data = DataModel.query.get_or_404(id)
        
        return data
        
@blp.route("/country/<string:name>")
class SearchByCountryName(MethodView):
    @blp.response(200, PageSchema)
    def get(self, name):
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=100, type=int)
        data = DataModel.query.filter(func.lower(DataModel.country) == func.lower(name)).paginate(page=page, per_page=per_page)
        result = {
                    'data': data,
                    'page': data.page,
                    'total_pages': data.pages,
                    'total_data': data.total
                    }

        if data.has_next:
            next_url = request.base_url + '?page=' + str(data.next_num)
            result['next'] = next_url
        
        if result["total_data"] != 0:
            return result
        
        abort(404, message=f"No data found for country {name}")

@blp.route("/country/iso3/<string:iso3>")
class SearchByISO3(MethodView):
    @blp.response(200, PageSchema)
    def get(self, iso3):
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=100, type=int)
        data = DataModel.query.filter_by(iso3=iso3).paginate(page=page, per_page=per_page)
        result = {
                    'data': data,
                    'page': data.page,
                    'total_pages': data.pages,
                    'total_data': data.total
                    }
        
        if data.has_next:
            next_url = request.base_url + '?page=' + str(data.next_num)
            result['next'] = next_url
    
        if result["total_data"] != 0:
            return result
        
        abort(404, message=f"No data found for iso3 {iso3}")

@blp.route("/country/iso2/<string:iso2>")
class SearchByISO2(MethodView):
    @blp.response(200, PageSchema)
    def get(self, iso2):
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=100, type=int)
        data = DataModel.query.filter_by(iso2=iso2).paginate(page=page, per_page=per_page)
        result = {
                    'data': data,
                    'page': data.page,
                    'total_pages': data.pages,
                    'total_data': data.total
                    }
        if data.has_next:
            next_url = request.base_url + '?page=' + str(data.next_num)
            result['next'] = next_url
    
        if result["total_data"] != 0:
            return result
        
        abort(404, message=f"No data found for iso2 {iso2}")


@blp.route("/city/lat/<string:lat>/lng/<string:lng>")
class SearchByLatAndLng(MethodView):
    @blp.response(200, DataSchema)
    def get(self, lat, lng):
        data = DataModel.query.filter(DataModel.lat == lat and DataModel.lng == lng).first()
        
        if data.lat == lat and data.lng == lng:
            return data
        
        abort(404, message=f"No data found for lat {lat} and lng {lng}")
                