#!/bin/bash

cd /code/
python create_faker_models.py
cd app/ 
IFS=, read -r -a databases <<<"$FAKER_DATABASE"
python manage.py makemigrations faker_meta_db
echo "-------------------------------------------"
echo "MIGRATE TYPE: $FAKER_MIGRATE"
if [ $FAKER_MIGRATE == "jdbc" ]
    then 
        for database in "${databases[@]}"; do echo "" && echo "MIGRATE: $database" && echo "--------------------------" && python manage.py migrate faker_meta_db --database $database --fake-initial; done
elif [ $FAKER_MIGRATE == "sql" ]
    then 
        echo "Migrate SQL default database";
        echo "-----------------------------------------------"
        if [[ $FAKER_MIGRATE_SQLFILE ]]
        then 
            python manage.py sqlmigrate faker_meta_db 0001 > $FAKER_MIGRATE_SQLFILE
            echo "CREATE FILE: $FAKER_MIGRATE_SQLFILE"
        else 
            python manage.py sqlmigrate faker_meta_db 0001
        fi
        echo "-----------------------------------------------"
fi