#!/bin/bash
echo "💥💥💥  Deleting existing migration files!"
find . -path "./.venv" -prune -o -name "__init__.py" -prune -o -path '*/migrations/*.py' -print | grep py | xargs rm -f
