from sqlalchemy.orm import Session
from typing import List
from models.task import Task
from dtos.dtos import TaskCreateRequest

class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task_request: TaskCreateRequest) -> Task:
        task = Task(**task_request.dict(), status="waiting")
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_tasks(self) -> List[Task]:
        return self.db.query(Task).all()