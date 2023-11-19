FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

COPY ./app ./
COPY .env ./


CMD ["sh","./entrypoint.sh"]