from pydantic import BaseModel

class RequestData(BaseModel):
    dataset_split: float

class Task(BaseModel):
    # Celery task representation
    task_id: str
    status: str


class Result(BaseModel):
    # Celery task result
    task_id: str
    status: str