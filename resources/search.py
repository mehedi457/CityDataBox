from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import DataModel
from schemas import DataSchema
from sqlalchemy import func

blp = Blueprint("search", __name__, description = "Search related functions")

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
    @blp.response(200, DataSchema(many=True))
    def get(self, name):
        data = DataModel.query.filter(func.lower(DataModel.country) == func.lower(name)).all()

        if not data:
            abort(404, message=f"No data found for country {name}")
                
        return data