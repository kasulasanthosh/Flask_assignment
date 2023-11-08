from flask_restful import Resource
from model.book import BookModel
from flask import request,jsonify

class BookRoute(Resource):
    def post(self):
        data = request.get_json()
        name = data["name"]
        price = data["price"]
        publication = data["publication"]

        obj = BookModel.find_by_name(name)
        if obj is not None:
            return make_response(jsonify({
                "Msg": "Book Exists",
                "Status": 404
            }),404)
        bookObj = BookModel(name=name,price=price,publication=publication)

        bookObj.add_to_db()

        return make_response(jsonify({
                "Msg": "Book Added",
                "Status": 200
            }),200)
    def get(self):
        data = request.get_json()
        name = data["name"]

        obj = BookModel.find_by_name(name)

        if obj is not None:
            return make_response(jsonify({
                "Name": obj.name,
                "Price": obj.price,
                "Publication": obj.publication
            }),200)

        return make_response(jsonify({
                "Msg": "Book Does not exist",
                "Status": 404
            }),404)
    def delete(self):
        data = request.get_json()
        name = data["name"]

        obj = BookModel.find_by_name(name)

        if obj is None:
            return make_response(jsonify({
                "Msg": "Book Does not exist",
                "Status": 404
            }),404)
        
            obj.delete_from_db()

            return make_response(jsonify({
            "Msg": "Book Deleted",
            "Status": 202
