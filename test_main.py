from fastapi.testclient import TestClient
from main import app, calls

client = TestClient(app)


def test_duplicate_call_is_not_stored_twice():
    calls.clear()

    data = {
        "call_id": "abc123",
        "status": "answered",
        "duration_secs": 42
    }

    first = client.post("/call-ended", json=data)
    second = client.post("/call-ended", json=data)

    assert first.status_code == 200
    assert second.status_code == 200
    assert len(calls) == 1