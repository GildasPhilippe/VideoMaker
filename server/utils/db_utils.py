from sqlalchemy import create_engine


USER = "admin"
PASSWORD = "password"
HOSTNAME = "db"
PORT = 3306
DB_NAME = "video_maker"


def get_engine():
    return create_engine(f'mysql+pymysql://{USER}:{PASSWORD}@{HOSTNAME}/{DB_NAME}')
