import logging

from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename

from models.video_stem_model import get_session_videos, get_video
from utils.session_utils import check_id_integrity, save_session_id
from utils.file_utils import is_valid_file, upload_video


UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']


class Videos(Resource):

    def post(self, session_id):
        try:
            if not check_id_integrity(session_id):
                return {'message': 'Unauthorized session id'}, 400
            save_session_id(session_id)
            if 'file' not in request.files:
                return {'message': 'No file has been sent'}, 400
            uploaded_file = request.files['file']
            if uploaded_file.filename == '':
                return {'message': 'No selected file'}, 400
            filename = secure_filename(uploaded_file.filename)
            if not is_valid_file(filename, uploaded_file):
                return {'message': "Invalid file"}, 400
            response_data = upload_video(session_id, filename, uploaded_file)
            return {'message': 'Video have been well uploaded', "data": response_data}, 201

        except Exception as e:
            logging.error(str(e))
            return {'message': 'An internal error occurred'}, 500

    def get(self, session_id, video_id):
        if not check_id_integrity(session_id):
            return {'message': 'Unauthorized session id'}, 400
        if video_id == "all":
            data = get_session_videos(session_id)
            if not len(data):
                return {'message': f'No video for session id {session_id}'}, 404
            else:
                return {"videos": data}
        if check_id_integrity(video_id):
            data = get_video(session_id, video_id)
            if not len(data):
                return {'message': 'Video not found'}, 404
            else:
                return {"videos": data}, 200
        return {'message': 'Video not found'}, 404
