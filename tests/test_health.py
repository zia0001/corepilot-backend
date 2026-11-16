from fastapi.testclient import TestClient
from app.main import app






# Create a TestClient instance to simulate requests to the FastAPI app
client = TestClient(app)


def test_health():
    response = client.get("/health")
#check that the response status code is 200 (OK) and the response body matches the expected output
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}