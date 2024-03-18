from celery import shared_task
import time


@shared_task()
def check_celery():
    time.sleep(5)
    print('Hello from celery!')