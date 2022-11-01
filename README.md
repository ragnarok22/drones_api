# drones-api

Drone Transportation Infrastructure API

![Django CI](https://github.com/ragnarok22/drones_api/actions/workflows/django-test.yml/badge.svg)
![Codecov](https://img.shields.io/codecov/c/github/ragnarok22/drones_api)
[![GitHub license](https://img.shields.io/github/license/ragnarok22/drones_api)](https://github.com/ragnarok22/drones_api/blob/main/LICENSE)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/ragnarok22/drones_api)
![GitHub repo size](https://img.shields.io/github/repo-size/ragnarok22/drones_api)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/ragnarok22/drones_api)

## License

Distributed under the terms of the [MIT](LICENSE) license.

## Running in development mode
This project was built using:
- [Python](https://python.org)
- [Django](https://djangoproject.com)
- [Django Rest Framework](https://django-rest-framework.org)
- [Docker](https://docker.com)
- [Poetry](https://python-poetry.org) (not required)

### create an isolation environment

(This step is not required if you use poetry)

```shell
python -m venv .venv
```

### install dependencies

```shell
pip install .
```

or use poetry:

```shell
poetry install
```

### Activate the local environment

```shell
source .venv/bin/activate
```

or use poetry:

```shell
poetry shell
```

Then run the development server

```shell
python manage.py runserver
```

## load testing data
This project creates for you an administration account with username `admin` and password `admin1`.

For providing initial data for models you can run these commands:

```shell
python manage.py loaddata drones  # this create some drones
python manage.py loaddata medications  # this create some medications
```

### Run periodic task to check the drone battery
This will create a periodic task to check the Drone battery and create a Log every 8 hours
```shell
python manage.py check_battery
```

## Deploy

This project uses [Docker](https://www.docker.com) for deployment

### environment variables

You must create .env file with the next variables:

- `DJANGO_SETTINGS_MODULE`: project settings. (set `config.settings.develop`).
- `SECRET_KEY`: used to provide cryptographic signing.
- `DB_HOST`: postgres database host.
- `DB_PORT`: postgres database port.
- `DB_USER`: postgres database user.
- `POSTGRES_PASSWORD`: postgres database password.
- `POSTGRES_DB`: postgres database name.
- `ALLOWED_HOSTS`: A list of strings representing the host/domain names that this Django site can serve.

[Here](.env-example) you have an example

### deploy the application

You must have installed Docker and Docker Compose to run the application:

```shell
docker-compose up -d
```

### Set Nginx

Here set an example for a nginx configuration and with the certbot to manage the ssl.
This project is set to only run in secure protocol (https)

    server {
        server_name drones-api.ragnarok22.dev;

        location / {
            proxy_pass http://localhost:8000;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $host;
            proxy_redirect off;
        }
    
        listen [::]:443 ssl ipv6only=on; # managed by Certbot
        listen 443 ssl; # managed by Certbot
        ssl_certificate /etc/letsencrypt/live/drones-api.ragnarok22.dev/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/drones-api.ragnarok22.dev/privkey.pem; # managed by Certbot
        include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    }
    
    server {
        if ($host = drones-api.ragnarok22.dev) {
            return 301 https://$host$request_uri;
        } # managed by Certbot
    
        listen 80;
        listen [::]:80;

        server_name drones-api.ragnarok22.dev;
        return 404; # managed by Certbot
    }

### Run periodic task in production

```shell
docker-compose run api python manage.py check_battery
```

## Running tests
For running test

```
coverage run manage.py test apps
coverage report
```

## API Documentation
This API documentation is in [Postman](https://documenter.getpostman.com/view/8475386/2s8YKGjgb2)