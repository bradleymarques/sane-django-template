#!/bin/bash
echo "🐚  Opening a Django shell"

docker compose run django_web python manage.py shell
