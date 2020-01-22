import unittest
import requests


class BpUserTests(unittest.TestCase):

    # reset_database()
    host = "127.0.0.1"
    port = "8888"
    server_url = f"http://{host}:{port}"

    def test_register_user(self):
        path = "/user/register"
        resp = requests.post(f"{self.server_url}{path}", json={"email": "email@email.com", "password": "thepassword"})
        self.assertEqual(resp.status_code, 201)

    def test_register_duplicate_user(self):
        path = "/user/register"
        resp1 = requests.post(f"{self.server_url}{path}", json={"email": "email1@email.com", "password": "thepassword"})
        self.assertEqual(resp1.status_code, 201)
        resp2 = requests.post(f"{self.server_url}{path}", json={"email": "email1@email.com", "password": "thepassword"})
        self.assertNotEqual(resp2.status_code, 201)

    def test_user_login(self):
        path = "/user/login"
        requests.post(f"{self.server_url}/user/register", json={"email": "email2@email.com", "password": "thepassword"})
        resp1 = requests.post(f"{self.server_url}{path}", json={"email": "email2@email.com", "password": "thepassword"})
        self.assertEqual(resp1.status_code, 200)
        resp2 = requests.post(f"{self.server_url}{path}", json={"email": "email2@email.comm", "password": "nopassword"})
        self.assertEqual(resp2.status_code, 400)
