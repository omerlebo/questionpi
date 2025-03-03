from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_question():
    question_id = 5
    wanted_response = {"id": 5,
    "difficulty": "medium",
    "category": "Entertainment",
    "question": "Who directed the movie \"Titanic\"?",
    "correctAnswer": "James Cameron"}
    response = client.get(url=f"/question/{question_id}")
    assert response.status_code == 200
    assert response.json() == wanted_response
