FROM python:3.9-alpine
WORKDIR /backend
COPY . .
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN python3 db.py
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask","run"]