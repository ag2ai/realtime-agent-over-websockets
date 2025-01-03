from fastapi.testclient import TestClient

from realtime_over_websockets.main import app

client = TestClient(app)


def test_index_page():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "WebSocket Audio Stream Server is running!"}
