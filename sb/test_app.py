import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_hello_world(self):
        response = self.client.get('/api/sb')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello from Service B!", response.data)

if __name__ == '__main__':
    unittest.main()