from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pydantic import BaseModel

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(String, default="Pendente")
    created_at = Column(DateTime, default=datetime.utcnow)

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    title: str
    description: str
    status: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_at: datetime

    class Config:
        orm_mode = True