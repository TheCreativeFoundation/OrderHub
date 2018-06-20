FROM python:3.6

COPY engine/ .
COPY requirements.txt /tmp

RUN pip install -r tmp/requirements.txt

CMD ["python3", "server.py"]