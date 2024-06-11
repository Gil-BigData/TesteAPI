from sqlalchemy.orm import Session
from app.models.task_model import Task
from app.repositories import task_repository

def get_task(db: Session, task_id: int):
    return task_repository.get_task(db, task_id)

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return task_repository.get_tasks(db, skip, limit)

def create_task(db: Session, title: str, description: str):
    task = Task(title=title, description=description)
    return task_repository.create_task(db, task)

def update_task(db: Session, task_id: int, title: str, description: str, status: str):
    task_data = {"title": title, "description": description, "status": status}
    return task_repository.update_task(db, task_id, task_data)

def delete_task(db: Session, task_id: int):
    return task_repository.delete_task(db, task_id)