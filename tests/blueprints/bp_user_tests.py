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

    def test_register_user(self):
        path = "/user/register"
        resp = requests.post(f"{self.server_url}{path}", json={"email": "email@email.com", "password": "thepassword"})
        self.assertEqual(201, resp.status_code)
        self.assertTrue("token" in resp.json().keys())

    def test_register_duplicate_user(self):
        path = "/user/register"
        resp1 = requests.post(f"{self.server_url}{path}", json={"email": "email@email.com", "password": "thepassword"})
        self.assertEqual(201, resp1.status_code)
        resp2 = requests.post(f"{self.server_url}{path}", json={"email": "email@email.com", "password": "thepassword"})
        self.assertNotEqual(201, resp2.status_code)

    def test_user_login(self):
        path = "/user/login"
        requests.post(f"{self.server_url}/user/register", json={"email": "email@email.com", "password": "thepassword"})
        resp1 = requests.post(f"{self.server_url}{path}", json={"email": "email@email.com", "password": "thepassword"})
        self.assertEqual(200, resp1.status_code)
        self.assertTrue("token" in resp1.json().keys())
        resp2 = requests.post(f"{self.server_url}{path}", json={"email": "email@email.comm", "password": "nopassword"})
        self.assertEqual(400, resp2.status_code)
        self.assertFalse("token" in resp2.json().keys())

    def test_get_user_account(self):
        path = "/user/account"
        resp = requests.post(f"{self.server_url}/user/register",
                             json={"email": "email@email.com", "password": "thepassword"})
        resp2 = requests.get(f"{self.server_url}{path}", headers={"Authorization": resp.json().get("token")})
        self.assertEqual(resp2.status_code, 200)
        self.assertTrue("id" in resp2.json().keys())
        self.assertTrue("email" in resp2.json().keys())
        self.assertTrue("ip_address" in resp2.json().keys())
        self.assertTrue("iat" in resp2.json().keys())
        self.assertTrue("exp" in resp2.json().keys())

    def test_get_user_account_bad_token(self):
        path = "/user/account"
        resp = requests.post(f"{self.server_url}/user/register",
                             json={"email": "email@email.com", "password": "thepassword"})
        resp2 = requests.get(f"{self.server_url}{path}", headers={"Authorization": f"{resp.json().get('token')}a"})
        self.assertEqual(resp2.status_code, 401)

    def test_post_user_account_change_password(self):
        path = "/user/account"
        resp = requests.post(f"{self.server_url}/user/register",
                             json={"email": "email@email.com", "password": "thepassword"})
        resp2 = requests.post(f"{self.server_url}{path}",
                              headers={"Authorization": f"{resp.json().get('token')}"},
                              json={"email": "email@email.com",
                                    "new_password": "newpassword",
                                    "confirm_password": "newpassword"})
        self.assertEqual(200, resp2.status_code)
        resp3 = requests.post(f"{self.server_url}/user/login", json={"email": "email@email.com",
                                                                     "password": "newpassword"})
        self.assertEqual(200, resp3.status_code)
