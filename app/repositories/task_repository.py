from sqlalchemy.orm import Session
from app.models.task_model import Task

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: Task):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def update_task(db: Session, task_id: int, task_data: dict):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        for key, value in task_data.items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task