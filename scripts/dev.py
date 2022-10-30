"""Poetry commands for development
"""
import shlex
import subprocess


def __run_process(command: str) -> str:
    try:
        process = subprocess.run(shlex.split(command), universal_newlines=True)
        return process.stdout
    except KeyboardInterrupt:
        pass


def runserver():
    __run_process("python manage.py runserver")


def test():
    __run_process("coverage run manage.py test apps")


def celery():
    __run_process("celery -A config.celery beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler")
