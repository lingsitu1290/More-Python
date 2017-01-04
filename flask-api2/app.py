from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'abc'
api = Api(app)

jwt = JWT(app, authenticate, identity) #creates new endpoint /auth

# class Student(Resource):
#     def get(self, name):
#         return {'student': name}
#
#
# api.add_resource(Student, '/student/<string:name>')

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannont be left blank!"
    )
    data = parser.parse_args()

    @jwt_required()
    def get(self, name):
        # This section can be replaced with the filter/ lambda function
        # for item in items:
        #     if item['name'] == name:
        #         return item
        item = next(filter(lambda x: x['name'] == name, items), None)
        # When can't find the item, thus 404(not found)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # If the item exists:
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        # 201 status code is "created", 202 is "accepted"
        return item, 201

    def delete(self, name):
        # The items we will use is the global items variable
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    # Create items or update existing items
    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
