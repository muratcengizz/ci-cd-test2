#!/bin/bash

cd django_api
docker-compose down
cd ..

cd django_collector
docker-compose down
cd ..

cd django_processor
docker-compose down
cd ..