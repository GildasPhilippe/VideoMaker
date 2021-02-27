import logging

from flask import request
from flask_restful import Resource

from utils.session_utils import check_session_id_integrity
from utils.queue_utils import add_session_id_to_queue


class Processor(Resource):

    def put(self, session_id):
        if not check_session_id_integrity(session_id):
            return {"data": "Unauthorized session"}, 400
        logging.info(f"Launching process session_id {session_id}")
        logging.info(f"Updating data for session_id {session_id}")  # TODO
        add_session_id_to_queue(session_id)
        return {"data": "Success!"}, 200  # TODO
