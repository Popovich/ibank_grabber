from .models import Bank, BankSchema, db
from flask_restful import Api, Resource
from flask import request, jsonify

schema = BankSchema()
api = Api(prefix='/pcalc/dbaas/v1')

class GetBank(Resource):
    def get(self, id):

        try:
            query = Bank.query.get(id)
        except IntegrityError as e:
            return jsonify({"message": "Bank could not be found."}), 400

        result = schema.dump(query)
        return jsonify({"bank": result.data})

class BanksList(Resource):
    
    def get(self):
        query = Bank.query.all()
        results = schema.dump(query, many=True).data
        return results

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return jsonify({'message': 'No input data provided'}), 400

        data, errors = schema.load(json_data)
        if errors:
            return jsonify(errors), 422

        try:
            data.add(data)
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 403
            return resp

        query = Bank.query.get(data.id)
        results = schema.dump(query).data
        return results, 201

api.add_resource(GetBank, '/bank/<int:id>')
api.add_resource(BanksList, '/banks')