import unittest
import requests


class BpUserTests(unittest.TestCase):

    host = "127.0.0.1"
    port = "9999"
    server_url = f"http://{host}:{port}"

    def setUp(self) -> None:
        requests.post(f"{self.server_url}/database/reset")

    def tearDown(self) -> None:
        requests.post(f"{self.server_url}/database/reset")

    def test_database_reset(self):
        path = "/database/reset"
        resp = requests.post(f"{self.server_url}{path}")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["status"], "success")
