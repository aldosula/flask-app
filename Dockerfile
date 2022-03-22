
FROM python:3.8-slim


WORKDIR /app
COPY . /app

RUN python -m pip install -r requirements.txt

COPY task2.py task2.py


CMD python3 task2.py