from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Hello(Resource):

    def get(self):
        return jsonify({'message': 'Hi There. This is BMG Homework!'})

    def post(self):
        data = request.get_json()
        return jsonify({'data': data}), 201


# bir sayının küpünü hesaplamak için başka bir kaynak
class Cube(Resource):

    def get(self, num):
        return jsonify({'cube': num ** 3})


# karşılık gelen url'leriyle birlikte kaynakları ekleme
api.add_resource(Hello, '/')
api.add_resource(Cube, '/cube/<int:num>') #/cube/<intiger numara girilir>

if __name__ == '__main__':
    app.run(debug=True)