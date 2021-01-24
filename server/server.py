from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={"/*": {"origins": ["http://localhost:3001"]}})
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'data': 'hello world'}, 200


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
