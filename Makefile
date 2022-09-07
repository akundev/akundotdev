lint:
	pipenv run isort --recursive --force-single-line-imports --line-width 999 .
	pipenv run autoflake --recursive --ignore-init-module-imports --in-place --remove-all-unused-imports .
	pipenv run isort --recursive --use-parentheses --trailing-comma --multi-line 3 --force-grid-wrap 0 --line-width 88 .
	pipenv run black .

run:
	pipenv run python3 ./manage.py runserver

prod:
	pipenv run gunicorn -b 0.0.0.0:8000 -w 4 settings.wsgi:application

sttc:
	pipenv run python3 ./manage.py collectstatic

tst:
	pipenv run python3 ./manage.py test