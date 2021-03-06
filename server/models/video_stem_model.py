from datetime import datetime, timezone
import logging

from flask import escape
import pandas as pd

from utils.db_utils import get_engine


DATE_COLUMNS = ["video_date", "date_created", "date_updated"]


def insert_video_stem(session_id, filename, file_hash, video_url, thumbnail_url, metadata):
    engine = get_engine()
    rank = pd.read_sql(f'SELECT count(*) nb FROM video_stem WHERE session_id="{session_id}"', engine)["nb"][0]  # concurrency ?
    upload_date = datetime.now(tz=timezone.utc)
    duration = metadata.get("duration")
    data = pd.DataFrame([{
        'session_id': session_id,
        'filename': filename,
        'file_hash': file_hash,
        'video_url': video_url,
        'thumbnail_url': thumbnail_url,
        'size': None,
        'title': None,
        'video_date': pd.to_datetime(metadata.get("video_date")),
        'location': None,
        'duration': duration,
        'start_at': 0,
        'end_at': int(duration) if duration else duration,
        'rank': rank,
        'is_vertical': metadata.get("is_vertical", False),
        'is_deleted': False,
        'deletion_type': None,
        'date_created': upload_date,
        'date_updated': upload_date,
    }])
    data.to_sql("video_stem", engine, if_exists="append", index=False)
    logging.info(f"Inserted video_stem {file_hash}")
    data[DATE_COLUMNS] = data[DATE_COLUMNS].astype(str)
    return data.to_dict(orient="records")[0]


def get_session_videos(session_id):
    query = f"select * from video_stem where session_id = '{session_id}'"
    return get_video_stem_data(query)


def get_video(session_id, video_hash):
    query = f"select * from video_stem where session_id = '{session_id}' and file_hash = '{video_hash}'"
    return get_video_stem_data(query)


def get_video_stem_data(query):
    engine = get_engine()
    data = pd.read_sql(query, engine)
    data[DATE_COLUMNS] = data[DATE_COLUMNS].astype(str)
    return data.to_dict(orient="records")


def update_video(session_id, video_id, data):
    logging.warning(data)
    columns = ["title", "location", "video_date", "start_at", "end_at"]
    updated_data = {key: escape(value) for key, value in data.items() if key in columns}
    if "video_date" in updated_data.keys():
        updated_data["video_date"] = pd.to_datetime(updated_data.get("video_date"), errors="coerce")
    updated_data["date_updated"] = datetime.now()
    if len(updated_data):
        engine = get_engine()
        set_clauses = [
            f"{key} = {escape(value)}" if isinstance(value, int) else f"{key} = '{escape(value)}'"
            for key, value in updated_data.items()
        ]
        query = f"""
            UPDATE video_stem
            SET {', '.join(set_clauses)}
            WHERE session_id = '{session_id}'
            AND file_hash = '{video_id}'
        """
        logging.warning(query)
        engine.execute(query)
        logging.info(f"Updated video stem {video_id}")
