# tests/test_controllers.py
from fastapi import HTTPException
from app.controllers.task_controller import create_task, read_task
from app.models.task_model import TaskCreate
from app.database import get_db, create_database

def test_create_task():
    # Create the database tables
    create_database()

    # Test case 1: Successful task creation
    db = next(get_db())
    task_data = TaskCreate(title="Test Task", description="Test Description")
    created_task = create_task(task_data, db)
    assert created_task.title == "Test Task"
    assert created_task.description == "Test Description"

    # Test case 2: Error handling for invalid task creation
    invalid_task_data = TaskCreate(title="", description="")
    try:
        create_task(invalid_task_data, db)
    except HTTPException as e:
        assert e.status_code == 422  # Unprocessable Entity
    else:
        raise AssertionError("Expected HTTPException but none was raised")

def test_read_task():
    # Create the database tables
    create_database()

    # Test case 1: Successful task retrieval
    db = next(get_db())
    task_data = TaskCreate(title="Test Task", description="Test Description")
    created_task = create_task(task_data, db)
    retrieved_task = read_task(created_task.id, db)
    assert retrieved_task.id == created_task.id

    # Test case 2: Error handling for non-existent task
    non_existent_task_id = 100
    try:
        read_task(non_existent_task_id, db)
    except HTTPException as e:
        assert e.status_code == 404  # Not Found
    else:
        raise AssertionError("Expected HTTPException but none was raised")
