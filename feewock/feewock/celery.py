from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

#celery basic setup 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feewock.settings')
app = Celery('feewock')
app.conf.enable_utc = False
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://127.0.0.1:6379/0'
app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')


#celery beat set up


app.autodiscover_tasks()

    
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

