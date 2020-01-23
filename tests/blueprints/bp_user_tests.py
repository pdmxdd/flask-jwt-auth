import os
import unittest
import requests
from flask import Flask


class BpUserTests(unittest.TestCase):

    # reset_database()
    host = "127.0.0.1"
    port = "8888"
    server_url = f"http://{host}:{port}"

    def setUp(self) -> None:
        requests.post(f"{self.server_url}/database/reset")

    def tearDown(self) -> None:
        requests.post(f"{self.server_url}/database/reset")

    def test_register_user(self):
        path = "/user/register"
        resp = requests.post(f"{self.server_url}{path}", json={"email": "email@email.com", "password": "thepassword"})
        self.assertEqual(201, resp.status_code)

    def test_register_duplicate_user(self):
        path = "/user/register"
        resp1 = requests.post(f"{self.server_url}{path}", json={"email": "email1@email.com", "password": "thepassword"})
        self.assertEqual(201, resp1.status_code)
        resp2 = requests.post(f"{self.server_url}{path}", json={"email": "email1@email.com", "password": "thepassword"})
        self.assertNotEqual(201, resp2.status_code)

    def test_user_login(self):
        path = "/user/login"
        requests.post(f"{self.server_url}/user/register", json={"email": "email2@email.com", "password": "thepassword"})
        resp1 = requests.post(f"{self.server_url}{path}", json={"email": "email2@email.com", "password": "thepassword"})
        self.assertEqual(200, resp1.status_code)
        resp2 = requests.post(f"{self.server_url}{path}", json={"email": "email2@email.comm", "password": "nopassword"})
        self.assertEqual(400, resp2.status_code)
