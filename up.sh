#!/bin/bash

cd django_collector
docker-compose up -d
cd ..

cd django_processor
docker-compose up -d
cd ..