from flask import Flask
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
        for item in items:
            if item['name'] == name:
                return item
        # When can't find the item, thus 404(not found)
        return {'item': None}, 404

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        # 201 status code is "created", 202 is "accepted"
        return item, 201


api.add_resource(Item, '/item/<string:name>')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
