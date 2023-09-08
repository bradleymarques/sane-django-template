#!/bin/bash
echo "💀💀💀 DELETING AND REGENERATING THE ENTIRE DATABASE SCHEMA 💀💀💀"

./scripts/flush.sh
./scripts/delete_existing_migration_files.sh
./scripts/make_migrations.sh
./scripts/migrate.sh
./scripts/seed.sh
./scripts/lint.sh
