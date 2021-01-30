import logging
import re
from datetime import datetime, timezone

import pandas as pd

from .db_utils import get_engine


SESSION_ID_REGEX = re.compile(r'^[A-z0-9]{64}$')


def check_session_id_integrity(session_id):
    return SESSION_ID_REGEX.match(session_id)


def save_session_id(session_id):
    engine = get_engine()
    data = pd.read_sql(f'SELECT * FROM session WHERE id="{session_id}"', engine)
    if not len(data):
        query = f"""
            INSERT INTO table (id, date_created, date_updated)
            VALUES ("{session_id}", NOW(), NOW())
            ON DUPLICATE KEY UPDATE date_updated=NOW()
            WHERE id = {session_id}
        """
        data.to_sql("session", engine, if_exists="append", index=False)
        logging.info(f"Created session {session_id}")
    return data
