from fastapi import FastAPI
from app.controllers import task_controller

app = FastAPI()

app.include_router(task_controller.router)