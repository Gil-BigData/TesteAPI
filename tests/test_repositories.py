# tests/test_repositories.py
from app.repositories.task_repository import create_task, get_task
from app.models.task_model import TaskCreate
from app.database import get_db, create_database

def test_create_task():
    # Create the database tables
    create_database()

    # Test case 1: Successful task creation
    db = next(get_db())
    task_data = TaskCreate(title="Test Task", description="Test Description")
    created_task = create_task(db, task_data)
    assert created_task.title == "Test Task"
    assert created_task.description == "Test Description"

    # Test case 2: Error handling for invalid task creation
    invalid_task_data = TaskCreate(title="", description="")
    try:
        create_task(db, invalid_task_data)
    except ValueError as e:
        assert str(e) == "Title and description cannot be empty"
    else:
        raise AssertionError("Expected ValueError but none was raised")

def test_get_task():
    # Create the database tables
    create_database()

    # Test case 1: Successful task retrieval
    db = next(get_db())
    task_data = TaskCreate(title="Test Task", description="Test Description")
    created_task = create_task(db, task_data)
    retrieved_task = get_task(db, created_task.id)
    assert retrieved_task.id == created_task.id

    # Test case 2: Error handling for non-existent task
    non_existent_task_id = 100
    retrieved_task = get_task(db, non_existent_task_id)
    assert retrieved_task is None
