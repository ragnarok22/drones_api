# drones-api
Drone Transportation Infrastructure API

![Django CI](https://github.com/ragnarok22/drones_api/actions/workflows/django-test.yml/badge.svg)

## License

Distributed under the terms of the [MIT](LICENSE) license.

## Running in development mode
### create a isolation environment
(This step is not required if you use [poetry](https://python-poetry.org))

    python -m venv .venv

### install the dependencies

    pip install .

or use poetry:

    poetry install

### Activate the local environment

    source .venv/bin/activate

or use poetry:

    poetry shell

Then run the development server

    python manage.py runserver
