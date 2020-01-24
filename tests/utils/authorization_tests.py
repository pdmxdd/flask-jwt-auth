import unittest
import time

from util.authorization import assign_token, verify_token


class AuthorizationTests(unittest.TestCase):

    def test_assign_token(self):
        token = assign_token({"status": "test", "body": "hello"}, "252.144.144.12")
        self.assertEqual(str, type(token))
        # token should have exactly 2 '.' splitting the string into 3 sections
        self.assertEqual(3, len(token.split('.')))

    def test_verify_default_token_success(self):
        token = assign_token({"status": "test", "body": "hello"}, "252.144.144.12")
        result = verify_token(token, "252.144.144.12")
        self.assertTrue(result["success"])
        self.assertEqual("test", result["payload"]["status"])
        self.assertEqual("hello", result["payload"]["body"])
        self.assertTrue("exp" in result["payload"].keys())
        self.assertTrue("iat" in result["payload"].keys())
        # token is issued by default for 6 hours (6 * 60 * 60 -> 21600)
        self.assertEqual(21600, result["payload"]["exp"] - result["payload"]["iat"])

    def test_verify_token_bad_ip(self):
        token = assign_token({"status": "test", "body": "hello"}, "252.144.144.12")
        result = verify_token(token, "111.111.111.111")
        self.assertFalse(result["success"])
        self.assertEqual("JWT error. IP Addresses don't match! User needs to re-authenticate.", result["status"])

    def test_verify_token_bad_token(self):
        token = assign_token({"status": "test", "body": "hello"}, "252.144.144.12")
        result = verify_token(f"{token}a", "252.144.144.12")
        self.assertFalse(result["success"])
        self.assertEqual("JWT error. User needs to re-authenticate.", result["status"])

    def test_expired_token(self):
        token = assign_token({"status": "test", "body": "hello"}, "252.144.144.12", lifetime_hours=(1/3600))
        time.sleep(2.0)
        result = verify_token(token, "252.144.144.12")
        self.assertFalse(result["success"])
        self.assertEqual("JWT expired. User must re-authenticate for a new token.", result["status"])
