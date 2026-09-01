#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python3 manage.py create_default_admin