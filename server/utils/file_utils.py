from datetime import datetime, timezone
import hashlib
import logging
import os

from models.video_stem import create_stem_data


UPLOAD_EXTENSIONS = ['jpg', 'png', 'gif']


def is_valid_file(filename, uploaded_file):
    valid_ext = '.' in filename and filename.rsplit('.', 1)[-1].lower() in UPLOAD_EXTENSIONS
    valid_size = True  # TODO: check size
    return valid_ext and valid_size


def save_file(session_id, filename, uploaded_file, upload_folder):
    dir_name = os.path.join(upload_folder, session_id)
    if not os.path.isdir(dir_name):
        logging.info(f"Creating folder: {dir_name}")
        os.makedirs(dir_name)
    file_hash = hashlib.sha224(f"{session_id}_{datetime.now(timezone.utc)}_{filename}".encode('utf-8')).hexdigest()
    extension = filename.split(".")[-1]
    hashed_filename = f"{file_hash}.{extension}"
    logging.info(f" Saving file: {hashed_filename}")
    url = os.path.join(dir_name, hashed_filename)
    uploaded_file.save(url)
    create_stem_data(session_id, filename, file_hash, url)
