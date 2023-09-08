#!/bin/bash
echo "🌱  Seeding the database "
poetry run python manage.py seed
