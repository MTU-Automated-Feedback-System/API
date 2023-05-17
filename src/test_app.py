import pytest
from flask import json
from flask_testing import TestCase
from app import app  # replace 'your_application' with the name of the file containing your Flask app
import repositories.submission_repo as db_submission
import repositories.exercise_repo as db_exercise

class TestSubmissionRoutes(TestCase):
    def __init__(self):
        app.config['TESTING'] = True
        return app

    def test_post_submission(self):
        submission_data = {
            "exercise_id": "test_exercise_id",
            "student_id": "test_student_id",
            "code": "print('Hello, World!')",
        }

        response = self.client.post('/submission', data=json.dumps(submission_data), content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "id" in data
        assert "response" in data

    def test_update_submission(self):
        submission_data = {
            "submission_id": "test_submission_id",
            "exercise_id": "test_exercise_id",
            "compiled_output": "Hello, World!",
            "compiled_status": "success",
            "error_type": None,
            "test_cases": [],
            "feedback": "Good job!",
            "cases": []
        }

        response = self.client.patch('/submission', data=json.dumps(submission_data), content_type='application/json')
        assert response.status_code == 200

    def test_get_submission(self):
        submission_id = "test_submission_id"
        exercise_id = "test_exercise_id"

        response = self.client.get(f'/submission/i?submission_id={submission_id}&exercise_id={exercise_id}')
        assert response.status_code == 200

    def test_get_submission_query(self):
        submission_id = "test_submission_id"
        response = self.client.get(f'/submission/{submission_id}')
        assert response.status_code == 200

    def test_get_submissions_query(self):
        student_id = "test_student_id"
        response = self.client.get(f'/submissions/{student_id}')
        assert response.status_code == 200

    def test_get_all_submissions(self):
        response = self.client.get('/submission/all')
        assert response.status_code == 200

if __name__ == '__main__':
    pytest.main(["-s", "test_app.py"])
