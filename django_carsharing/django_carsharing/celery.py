import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_carsharing.settings")

app = Celery("django_carsharing", broker="redis://redis:6379/0", backend="redis://redis:6379/0")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(['django_carsharing'])

app.conf.beat_schedule = {
    'send-email-task': {
        'task': 'django_carsharing.tasks.send_email_task',
        'schedule': crontab(minute='*/1'),  
    },
}