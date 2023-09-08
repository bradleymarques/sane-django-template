#!/bin/bash
echo "🏗️  Making migration files"

poetry run python manage.py makemigrations
