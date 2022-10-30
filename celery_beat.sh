#!/bin/sh

celery -A config beat -l INFO -S django
