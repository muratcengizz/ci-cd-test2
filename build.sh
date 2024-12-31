#!/bin/bash

# django_collector project
cd django_collector
docker-compose build
docker-compose up -d
cd ..

# django_processor project
cd django_processor
docker-compose build
docker-compose up -d
cd ..