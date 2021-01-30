import logging

from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename

from utils.session_utils import check_session_id_integrity, save_session_id
from utils.file_utils import is_valid_file, save_file


MAX_CONTENT_LENGTH = 2 * 1024 * 1024
UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
UPLOAD_PATH = 'uploads'


class Videos(Resource):
    def post(self):
        try:
            session_id = request.form['session-id']
            if not check_session_id_integrity(session_id):
                return 'Unauthorized session id', 400
            save_session_id(session_id)
            if 'file' not in request.files:
                return 'No file has been sent', 400
            uploaded_file = request.files['file']
            if uploaded_file.filename == '':
                return 'No selected file', 400
            filename = secure_filename(uploaded_file.filename)
            if not is_valid_file(filename, uploaded_file):
                return "Invalid file", 400
            save_file(session_id, filename, uploaded_file, UPLOAD_PATH)
            return 'Videos have been well uploaded', 204

        except Exception as e:
            logging.error(str(e))
            return 'An internal error occurred', 500
