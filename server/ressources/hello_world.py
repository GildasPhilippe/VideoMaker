from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return {'data': 'hello world'}, 200

    def post(self):
        return {'data': 'hello world'}, 200
