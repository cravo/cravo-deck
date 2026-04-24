FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE ${PORT}

CMD gunicorn --bind 0.0.0.0:${PORT} --workers 4 --timeout 120 server:app
