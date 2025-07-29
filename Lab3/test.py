import unittest
from my_app import app 

app.testing = True

class FlaskTests(unittest.TestCase):
    def test_hello(self):
        client = app.test_client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()