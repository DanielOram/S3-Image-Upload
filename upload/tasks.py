from celery.schedules import crontab
# from celery.decorators import periodic_task
from celery import shared_task

from datetime import datetime

# @shared_task(run_every=(crontab(minute='*/1')), name="test_task", ignore_result=True)
@shared_task(name="test_task")
def test_task():
    print('running test task...')


def 

from app.celery import app

app.conf.beat_schedule = {
    # Executes every minute
    'test task with beat schedule': {
        'task': 'test_task',
        'schedule': crontab(minute='*/1')
    },
}