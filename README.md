# drones-api

Drone Transportation Infrastructure API

![Django CI](https://github.com/ragnarok22/drones_api/actions/workflows/django-test.yml/badge.svg)
[![GitHub license](https://img.shields.io/github/license/ragnarok22/drones_api)](https://github.com/ragnarok22/drones_api/blob/main/LICENSE)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/ragnarok22/drones_api)
![GitHub repo size](https://img.shields.io/github/repo-size/ragnarok22/drones_api)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/ragnarok22/drones_api)

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

## load testing data
This project create for you an administration account with username `admin` and password `admin1`.

For providing initial data for models you can run this commands:

    python manage.py loaddata drones  # this create somes drones
    python manage.py loaddata medications  # this create some medications

## Deploy

This project use [Docker](https://www.docker.com) for deployment

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

    docker-compose up -d

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