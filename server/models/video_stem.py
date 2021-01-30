from datetime import datetime, timezone
import logging
import pandas as pd
from utils.db_utils import get_engine


def create_stem_data(session_id, filename, file_hash, url):
    engine = get_engine()
    rank = pd.read_sql(f'SELECT count(*) nb FROM video_stem WHERE session_id="{session_id}"', engine)["nb"][0]  # concurrency ?
    date = datetime.now(tz=timezone.utc)
    duration = 1
    data = pd.DataFrame([{
        'session_id': session_id,
        'filename': filename,
        'file_hash': file_hash,
        'url': url,
        'size': None,
        'duration': duration,
        'start_at': 0,
        'end_at': duration,
        'rank': rank,
        'is_deleted': False,
        'deletion_type': None,
        'date_created': date,
        'date_updated': date,
    }])
    data.to_sql("video_stem", engine, if_exists="append", index=False)
    logging.info(f"Created session {session_id}")
    return data
