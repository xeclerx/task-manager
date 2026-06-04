from backend.app.services.task import TaskService
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.app.db.session import get_db


def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(db)
