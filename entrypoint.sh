#!/bin/bash

cd /code/
python create_faker_models.py
cd app/ 
IFS=, read -r -a databases <<<"$FAKER_DATABASE"
python manage.py makemigrations faker_meta_db
for database in "${databases[@]}"; do echo "" && echo "MIGRATE: $database" && echo "--------------------------" && python manage.py migrate faker_meta_db --database $database --fake-initial; done