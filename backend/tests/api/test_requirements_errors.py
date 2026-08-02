404, 401
from tests.conftest import client


def test_get_requirements():
  response = client.get("/api/v1/requirements")
  assert response.status_code == 200
  body=response.json(