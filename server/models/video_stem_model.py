from datetime import datetime, timezone
import logging
import pandas as pd
from utils.db_utils import get_engine


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
        'video_date': pd.to_datetime(metadata.get("video_date")),
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
    logging.info(f"Created session {session_id}")
    return data