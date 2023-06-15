import pytest
import mongomock
from app.api.schemas import Build, Task


@pytest.fixture()
def mongo_mock(monkeypatch):
    client = mongomock.MongoClient()
    database = client.sbr_build
    tasks_col = database.tasks
    builds_col = database.builds

    build_data: Build = {
        "name": "test_test_build",
        "tasks": [
            "test_test_task",
            "test_test_task1",
        ],
    }

    task_data: Task = {"name": "test_test_task", "dependencies": ["test_test_task1"]}

    task_data1: Task = {"name": "test_test_task1", "dependencies": []}

    builds_col.insert_one(build_data)
    tasks_col.insert_one(task_data)
    tasks_col.insert_one(task_data1)

    def get_fake_db():
        return database

    def get_fake_tasks_collection():
        return tasks_col

    def get_fake_builds_collection():
        return builds_col

    monkeypatch.setattr("app.db.settings.get_db", get_fake_db)
    monkeypatch.setattr(
        "app.db.settings.get_builds_collection", get_fake_builds_collection
    )
    monkeypatch.setattr(
        "app.db.settings.get_tasks_collection", get_fake_tasks_collection
    )
