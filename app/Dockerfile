FROM python:3.14.0-alpine3.22

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY app/app.py .
COPY app/wsgi.py .


COPY templates/ ./templates/

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]