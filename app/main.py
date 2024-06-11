# app/main.py
from fastapi import FastAPI
from app.controllers import task_controller
from app.database import create_database

app = FastAPI()

app.include_router(task_controller.router)

# Create the database tables
create_database()
