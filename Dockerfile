FROM python:3.12-slim

LABEL authors="Арсений"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

COPY /requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD alembic upgrade head && python app/main.py
