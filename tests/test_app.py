import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))
from app import app
from models import QA

@pytest.fixture
def init_database():
    pass
    
#test checks if the /ask endpoint responds successfully
def test_ask_question_success(init_database):
    with app.test_client() as client:
        response = client.post('/ask', json={'question': 'can you help me ?'})
        print(f"checks if the /ask endpoint responds successfully, status_code {response.status_code}")
        assert response.status_code == 200

#test checks if a question and answer are correctly saved to the database after making a POST request to the /ask endpoint.
def test_record_in_database(init_database):
    with app.test_client() as client:
        client.post('/ask', json={'question': 'are you clever?'})

    with app.app_context():
        record = QA.query.filter_by(question='are you clever?').first()
        print(f"checks if the question saved correctly, the Question: {record.question}")
        assert record.question is not None
        print(f"checks if the answer saved correctly, the Answer: {record.answer}")
        assert record.answer is not None