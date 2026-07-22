from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)
response = client.get("api/v1/health")

def test_health_check():
  assert response.status_code == 200
  body=response.json()
  assert body["status"] == "healthy"
  assert body["service"] == "ai-test-platform-api"
  assert body["version"] == "0.1.0"