from datetime import datetime, timezone
import imghdr
import logging
import os
import re

from flask import Flask, request, send_from_directory
from flask_restful import Resource, Api
from flask_cors import CORS
from werkzeug.utils import secure_filename


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3001"]}})
api = Api(app)

logging.basicConfig(
    filename=f'./logs/logs-{datetime.now(timezone.utc).strftime("%Y-%m-%d")}.log',
    level=logging.INFO,
    filemode='a'
)

SESSION_ID_REGEX = re.compile(r'^[A-z0-9]{32}$')


app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


class HelloWorld(Resource):
    def get(self):
        return {'data': 'hello world'}, 200


class Videos(Resource):
    def post(self):
        session_id = request.form['session-id']
        if not SESSION_ID_REGEX.match(session_id):
            return {'message': 'Unauthorized session id'}, 401
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext != validate_image(uploaded_file.stream):
                return "Invalid image", 400
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        return {'message': 'Videos have been well uploaded'}, 204


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413


@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


api.add_resource(HelloWorld, '/')
api.add_resource(Videos, '/ressources/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
