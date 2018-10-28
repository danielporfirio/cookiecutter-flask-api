import unittest
import json

from {{cookiecutter.package_name}} import create_app, db
from {{cookiecutter.package_name}}.models import Person, Job


class Base(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def get_api_headers(self):
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_not_found_404_code(self):
        response = self.client.get('/wrong/url',
                                   headers=self.get_api_headers())

        self.assertEqual(response.status_code, 404)

        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['error'], 'not found')