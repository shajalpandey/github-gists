##Dockerfile for Gists API 
FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip setuptools==6.1.0 wheel==0.46.2 \
    && pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD wget -q -O /dev/null http://localhost:8080/health || exit 1

USER 10001:10001

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
