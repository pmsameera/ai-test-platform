from backend.app.models import requirement
from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)


def test_get_requirements():
  response = client.get("/api/v1/requirements")
  assert response.status_code == 200
  body=response.json()
  assert isinstance(body, list)
  assert len(body) > 0, "No requirements found"
  for requirement in body:
     assert "id" in requirement, "id field is missing in requirement" 
     assert "title" in requirement, "title field is missing in requirement"
     assert "description" in requirement, "description field is missing in requirement"

     assert isinstance(requirement["id"], int), "id field should be an integer"
     assert isinstance(requirement["title"], str), "title field should be a string"
     assert isinstance(requirement["description"], str), "description field should be a string"
     
     assert requirement["id"] > 0
     assert requirement["title"].strip() != ""
     assert requirement["description"].strip() != ""


def test_get_requirement():
  response = client.get("/api/v1/requirements/1")
  assert response.status_code == 200
  requirement=response.json()
  assert "id" in requirement, "id field is missing in requirement" 
  assert "title" in requirement, "title field is missing in requirement"
  assert "description" in requirement, "description field is missing in requirement"
 
  assert isinstance(requirement["id"], int), "id field should be an integer"
  assert isinstance(requirement["title"], str), "title field should be a string"
  assert isinstance(requirement["description"], str), "description field should be a string"
      
  assert requirement["id"] > 0
  assert requirement["title"].strip() != ""
  assert requirement["description"].strip() != ""
 

def test_add_requirement():
  response = client.post("/api/v1/requirements", json={"title": "New Requirement", "description": "This is a new requirement"})
  assert response.status_code == 201
 
  body = response.json()
  assert "id" in body, "id field is missing in response"
  assert "title" in body, "title field is missing in response"
  assert "description" in body, "description field is missing in response"  

  assert isinstance(body["id"], int), "id field should be an integer"
  assert isinstance(body["title"], str), "title field should be a string"
  assert isinstance(body["description"], str), "description field should be a string" 

  assert body["id"] > 0
  assert body["title"] == "New Requirement"
  assert body["description"] == "This is a new requirement" 

def test_update_requirement():
  response = client.put("/api/v1/requirements/1", json={"title": "Updated Requirement"})
  assert response.status_code == 200

  body = response.json()
  assert "id" in body, "id field is missing in response"
  assert "title" in body, "title field is missing in response"
  assert "description" in body, "description field is missing in response"  
 
  assert isinstance(body["id"], int), "id field should be an integer"
  assert isinstance(body["title"], str), "title field should be a string"
  assert isinstance(body["description"], str), "description field should be a string" 
 
  assert body["id"] > 0
  assert body["title"] == "Updated Requirement"
  assert body["description"] == "This is a new requirement"