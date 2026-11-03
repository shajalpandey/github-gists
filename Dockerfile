##Dockerfile for Gists API 
FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD wget -q -O /dev/null http://localhost:8080/health || exit 1

USER 10001:10001

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
