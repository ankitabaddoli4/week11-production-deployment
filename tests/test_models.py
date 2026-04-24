from src.models import Task

def test_task_creation():
    task = Task(1, "Test Task", "pending")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.status == "pending"

def test_task_to_dict():
    task = Task(1, "Test Task", "pending")
    result = task.to_dict()

    assert result["id"] == 1
    assert result["title"] == "Test Task"
    assert result["status"] == "pending"