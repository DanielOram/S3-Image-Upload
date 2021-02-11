from celery.schedules import crontab
# from celery.decorators import periodic_task
from celery import shared_task

from .models import TestCeleryModel
from datetime import datetime

# @shared_task(run_every=(crontab(minute='*/1')), name="test_task", ignore_result=True)
@shared_task(name="test_task")
def test_task():
    print('running test task...')
    TestCeleryModel.objects.create(name='Created by celery task at {}'.format(datetime.now()))

    # do something

from app.celery import app

app.conf.beat_schedule = {
    # Executes every minute
    'test task with beat schedule': {
        'task': 'test_task',
        'schedule': crontab(minute='*/1')
    },
}