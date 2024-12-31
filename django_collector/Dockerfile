FROM python:3.9-slim

RUN mkdir /django_collector_project

WORKDIR /django_collector_project

COPY . .

RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]