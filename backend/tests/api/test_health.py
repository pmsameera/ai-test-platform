from tests.conftest import client

def test_health_check():
  response = client.get("api/v1/health")

  assert response.status_code == 200
  body=response.json()
  assert body["status"] == "healthy"
  assert body["service"] == "ai-test-platform-api"
  assert body["version"] == "0.1.0"