FROM python:3.4

ADD . /data/jzspyw.com

RUN pip install -r /data/jzspyw.com/requirements.txt

WORKDIR /data/jzspyw.com

EXPOSE 8080

CMD ["python", "server.py"]