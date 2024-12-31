#!/bin/bash

# django_collector project
docker exec -i django-collector-container python manage.py makemigrations
docker exec -i django-collector-container python manage.py migrate

# django_processor project
docker exec -i processor-django-container python manage.py makemigrations
docker exec -i processor-django-container python manage.py migrate