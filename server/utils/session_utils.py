import logging
import re

import pandas as pd

from .db_utils import get_engine


ID_REGEX = re.compile(r'^[A-z0-9]{56}$')


def check_id_integrity(resource_id):
    return ID_REGEX.match(resource_id)


def save_session_id(session_id):
    engine = get_engine()
    data = pd.read_sql(f'SELECT * FROM session WHERE id="{session_id}"', engine)
    if not len(data):
        query = f"""
            INSERT INTO session (id, date_created, date_updated)
            VALUES ("{session_id}", NOW(), NOW())
            ON DUPLICATE KEY UPDATE date_updated=NOW()
            WHERE id = {session_id}
        """
        # data.to_sql("session", engine, if_exists="append", index=False)  # TODO: engine.execute(query)
        logging.info(f"Created session {session_id}")
    return data
