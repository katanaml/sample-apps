from celery import Celery

app = Celery(
    'celery_web',
    broker='pyamqp://guest@localhost//',
    backend='rpc://',
    include=['boston_housing.tasks']
)