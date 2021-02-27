import logging
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Boolean, Float


USER = "admin"
PASSWORD = "password"
HOSTNAME = "localhost"
PORT = 3306
DB_NAME = "video_maker"
engine = create_engine(f'mysql+pymysql://{USER}:{PASSWORD}@{HOSTNAME}:{PORT}/{DB_NAME}')
meta = MetaData()
logging.basicConfig(level=logging.INFO)


engine.execute("drop table session")
engine.execute("drop table project")
engine.execute("drop table video_stem")
engine.execute("drop table video_result")

session = Table(
   'session', meta,
   Column('id', String(100), primary_key=True),
   Column('date_created', DateTime, index=True),
   Column('date_updated', DateTime, index=True),
)
logging.info("Set up session")

project = Table(
   'project', meta,
   Column('id', Integer, primary_key=True, autoincrement=True),
   Column('session_id', String(100), index=True),
   Column('title', String(255)),
   Column('date_created', DateTime, index=True),
   Column('date_updated', DateTime, index=True),
)
logging.info("Set up project")

video_stem = Table(
   'video_stem', meta,
   Column('id', Integer, primary_key=True, autoincrement=True),
   Column('session_id', String(100), index=True),
   Column('filename', String(100)),
   Column('file_hash', String(100)),
   Column('video_url', String(255)),
   Column('thumbnail_url', String(255)),
   Column('size', Integer),
   Column('video_date', DateTime),
   Column('duration', Float),
   Column('start_at', Integer),
   Column('end_at', Integer),
   Column('rank', Integer),
   Column('is_vertical', Boolean),
   Column('is_deleted', Boolean, index=True),
   Column('deletion_type', String(20)),
   Column('date_created', DateTime, index=True),
   Column('date_updated', DateTime, index=True),
)
logging.info("Set up video_stem")

video_result = Table(
   'video_result', meta,
   Column('id', Integer, primary_key=True, autoincrement=True),
   Column('session_id', String(100), index=True),
   Column('filename', String(100)),
   Column('url', String(255)),
   Column('size', Integer),
   Column('duration', Integer),
   Column('process_duration', Integer),
   Column('is_downloaded', Boolean, index=True),
   Column('is_deleted', Boolean, index=True),
   Column('deletion_type', String(20)),
   Column('date_created', DateTime, index=True),
   Column('date_updated', DateTime, index=True),
   Column('date_downloaded', DateTime, index=True),
)
logging.info("Set up video_result")


meta.create_all(engine)
logging.info("Created all tables successfully!")
