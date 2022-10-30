#!/bin/bash

celery -A config beat -l INFO -S django
