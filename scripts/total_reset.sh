#!/bin/bash
./scripts/down.sh
./scripts/regenerate_db_schema.sh
./scripts/up.sh
