import unittest
import requests
import subprocess
import time
import os

class TestFibonacciService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the CherryPy server in a separate process
        cls.server = subprocess.Popen(['python', '__main__.py'])
        # Wait for the server to start
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        # Terminate the CherryPy server
        cls.server.terminate()

    def test_fibonacci_2(self):
        response = requests.get("http://localhost:8080/?n=2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"fibonacci": 1})

    def test_fibonacci_10(self):
        response = requests.get("http://localhost:8080/?n=10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"fibonacci": 55})

    def test_invalid_input(self):
        response = requests.get("http://localhost:8080/?n=abc")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"error": "Invalid input. Please provide an integer value."})

    def test_negative_input(self):
        response = requests.get("http://localhost:8080/?n=-5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"error": "Input must be a non-negative integer."})

if __name__ == '__main__':
    unittest.main()
