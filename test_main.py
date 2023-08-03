import unittest
from fastapi.testclient import TestClient
from main import app
from fibonacci import fibonacci

client = TestClient(app)

class TestFibonacciAPI(unittest.TestCase):

    def test_valid_input(self):
        response = client.get("/fib?n=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 5})

        response = client.get("/fib?n=10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 55})

if __name__ == "__main__":
    unittest.main()
