#!/bin/bash
echo "🗑️ Flushing uploaded files"
rm -rf sane_django_template/uploaded_media

echo "🗑️ Deleting the database"
rm sane_django_template/db.sqlite3
