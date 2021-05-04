from .worker import app
from celery.utils.log import get_task_logger
from .ml.trainingservice import run_training

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)

@app.task(name='boston_housing.train_model')
def train_model(dataset_split):
    run_training(dataset_split)
    celery_log.info(f"Celery task completed!")
    return 'OK'