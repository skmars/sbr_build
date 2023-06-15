import json
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


async def test_get_sorted_tasks(mongo_mock):
    build_data = {"build": "voice_central"}
    resp = client.post("/get_tasks", data=json.dumps(build_data))
    data_from_resp = resp.json()
    assert resp.status_code == 200
    assert data_from_resp.len() != 0


async def test_tasks_not_found(mongo_mock):
    build_data = {"build": "test_test_build"}
    resp = client.post("/get_tasks", data=json.dumps(build_data))
    assert resp.status_code == 404


@pytest.mark.parametrize(
    "build_title_to_get_tasks, expected_status_code, expected_detail",
    [
        (
            {"build": 333},
            422,
            {
                "detail": "build name should contain string with only letters and underscores"
            },
        ),
        (
            {"build": []},
            422,
            {
                "detail": "build name should contain string with only letters and underscores"
            },
        ),
    ],
)
async def test_get_tasks_validation_error(
    mongo_mock, build_title_to_get_tasks, expected_status_code, expected_detail
):
    resp = client.post("/get_tasks", data=json.dumps(build_title_to_get_tasks))
    assert resp.status_code == expected_status_code
    resp_data = resp.json()
    assert resp_data == expected_detail
