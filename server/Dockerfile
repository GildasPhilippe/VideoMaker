FROM python:3.8
RUN apt-get -y update && apt-get -y install ffmpeg
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD [ "python", "server.py" ]
