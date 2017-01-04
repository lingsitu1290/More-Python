from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# class Student(Resource):
#     def get(self, name):
#         return {'student': name}
#
#
# api.add_resource(Student, '/student/<string:name>')

items = []

class Item(Resource):
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

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        # 201 status code is "created", 202 is "accepted"
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
