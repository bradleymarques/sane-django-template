#!/bin/bash
echo "🏗️  Running migrations"

poetry run python manage.py migrate
