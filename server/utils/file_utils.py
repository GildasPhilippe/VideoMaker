from datetime import datetime, timezone
import hashlib
import logging
import os

import ffmpeg
from PIL import Image

from models.video_stem_model import insert_video_stem


VIDEO_DIRECTORY = 'uploads/videos/'
THUMBNAIL_DIRECTORY = 'uploads/thumbnails/'
THUMBNAIL_WIDTH = 480
PLAY_BUTTON_PATH = "data/play_button.png"
UPLOAD_EXTENSIONS = ['mp4', 'png', 'gif']


def is_valid_file(filename, uploaded_file):
    valid_ext = '.' in filename and filename.rsplit('.', 1)[-1].lower() in UPLOAD_EXTENSIONS
    valid_size = True  # TODO: check size
    return valid_ext and valid_size


def upload_video(session_id, filename, uploaded_file):
    video_dir_name = os.path.join(VIDEO_DIRECTORY, session_id)
    thumbnail_dir_name = os.path.join(THUMBNAIL_DIRECTORY, session_id)
    for directory in [video_dir_name, thumbnail_dir_name]:
        if not os.path.isdir(directory):
            logging.info(f"Creating directory: {directory}")
            os.makedirs(directory)

    file_hash = hashlib.sha224(f"{session_id}_{datetime.now(timezone.utc)}_{filename}".encode('utf-8')).hexdigest()
    extension = filename.split(".")[-1]
    hashed_filename = f"{file_hash}.{extension}"
    video_url = os.path.join(video_dir_name, hashed_filename)

    logging.info(f" Saving file: {hashed_filename}")
    uploaded_file.save(video_url)
    if extension == "mp4":
        thumbnail_url, is_vertical = generate_thumbnail(video_url, thumbnail_dir_name, file_hash)
        metadata = extract_metadata(video_url, is_vertical)
        response_data = insert_video_stem(session_id, filename, file_hash, video_url, thumbnail_url, metadata)
    else:  # FOR DEV PURPOSES:
        import pandas as pd
        response_data = insert_video_stem(session_id, filename, file_hash, video_url, "thumbnail_url", {
            "duration": 0, "is_vertical": False, "date": pd.to_datetime("2020-01-01")})
    return response_data


def extract_metadata(filename, is_vertical):
    result = {
        "is_vertical": is_vertical
    }
    logging.info(f"Extracting metadata from {filename}")
    try:
        streams = ffmpeg.probe(filename).get('streams', [])
        metadata = streams[0 if streams[0].get("codec_type") == 'video' else 1]
        result["video_date"] = metadata.get("tags", {}).get("creation_time")
        duration = metadata.get("duration")
        result["duration"] = float(duration) if duration else duration
    except Exception as e:
        logging.error(f"An error happened during the metadata extraction from video {filename}: {e}")
    return result


def generate_thumbnail(video_path, upload_directory, file_hash):
    try:
        thumbnail_url = os.path.join(upload_directory, f"{file_hash}.png")
        (
            ffmpeg
            .input(video_path, ss=0)
            .filter('scale', THUMBNAIL_WIDTH, -1)
            .output(thumbnail_url, vframes=1)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        thumbnail = Image.open(thumbnail_url, 'r')
        thumb_w, thumb_h = thumbnail.size
        is_vertical = thumb_w < thumb_h
        if is_vertical:
            thumb_w, thumb_h = THUMBNAIL_WIDTH * thumb_w // thumb_h, THUMBNAIL_WIDTH
            thumbnail = thumbnail.resize((thumb_w, thumb_h))
        play_button = Image.open(PLAY_BUTTON_PATH, 'r')
        pb_w, pb_h = play_button.size
        offset = ((thumb_w - pb_w) // 2, (thumb_h - pb_h) // 2)
        thumbnail.paste(play_button, offset, play_button)
        thumbnail.save(thumbnail_url)
        return thumbnail_url, is_vertical
    except ffmpeg.Error as e:
        logging.error(f"Error while creating a thumbnail: {e}")
        return None
