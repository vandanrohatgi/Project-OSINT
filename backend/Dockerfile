FROM python:3.9-alpine
COPY . /backend/
WORKDIR /backend/app
RUN python3 db.py
WORKDIR /backend
RUN pip install -r requirements.txt
RUN pip install -e .
ENV FLASK_APP=/app:flask_app
CMD flask run --host 0.0.0.0 --port $PORT