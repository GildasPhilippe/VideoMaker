from datetime import datetime
import imghdr
import logging
import os
import re

from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename


SESSION_ID_REGEX = re.compile(r'^[A-z0-9]{32}$')
MAX_CONTENT_LENGTH = 2 * 1024 * 1024
UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
UPLOAD_PATH = 'uploads'


class Videos(Resource):
    def post(self):
        session_id = request.form['session-id']
        if not SESSION_ID_REGEX.match(session_id):
            return {'message': 'Unauthorized session id'}, 401
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in UPLOAD_EXTENSIONS or file_ext != validate_image(uploaded_file.stream):
                return "Invalid image", 400
            uploaded_file.save(os.path.join(UPLOAD_PATH, filename))
        return {'message': 'Videos have been well uploaded'}, 204


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')
