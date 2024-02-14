from celery import shared_task
from time import sleep

@shared_task
def example_task():
    print("Your celery is working")