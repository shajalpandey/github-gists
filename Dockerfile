##Dockerfile for Gists API 
FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 8080

# USER 10001:10001

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
