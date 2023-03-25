export DJANGO_SETTINGS_MODULE=config.settings.local

python3 manage.py migrate
python3 manage.py collectstatic

python3 manage.py loaddata ../fixtures/admin.json
python3 manage.py loaddata ../fixtures/all.json
