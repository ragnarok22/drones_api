#!/bin/sh

celery -A config worker -l INFO
