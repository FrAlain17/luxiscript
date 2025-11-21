#!/bin/sh

# Wait for DB if needed (simple sleep for now, or use wait-for-it in future)
# sleep 5

echo "Applying migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec "$@"
