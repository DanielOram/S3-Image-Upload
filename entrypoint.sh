#!/bin/sh

if ["$DATABASE" = "postgres"]
then
    echo "Waiting for database..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "Database has started!"
fi


python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate

exec "$@"