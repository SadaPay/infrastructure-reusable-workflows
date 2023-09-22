import unittest
from unittest.mock import patch
import requests_mock


class MyTestCase(unittest.TestCase):

    @requests_mock.Mocker()
    def test_mock_post_request(self, m):
        # Create a mock object for the POST request
        url = "https://wmj70051.live.dynatrace.com/api/config/v1/dashboards"
        expected_response = {"dashboards": []}

        # Define the headers
        headers = {"Authorization": "<key_here>", "accept": "application/json; charset=utf-8"}

        # Create a mock object for the POST request
        m.get(url, json=expected_response, status_code=200, headers=headers)

        # Import and use the function that makes the POST request
        from dynatrace_dashboard import get_dashboards
        response = get_dashboards()

        # Assert that the mock request was called with the expected URL
        self.assertEqual(m.call_count, 1)
        self.assertEqual(m.request_history[0].url, url)

        # Assert that the response from the function matches the expected response
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
