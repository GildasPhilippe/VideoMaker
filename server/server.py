from datetime import datetime, timezone
import logging
from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS

from ressources import HelloWorld, Videos


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3001/*"]}})
api = Api(app)

logging.basicConfig(
    filename=f'./logs/logs-{datetime.now(timezone.utc).strftime("%Y-%m-%d")}.log',
    level=logging.INFO,
    filemode='a'
)


app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'


@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413


@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


api.add_resource(HelloWorld, '/')
api.add_resource(Videos, '/videos/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
