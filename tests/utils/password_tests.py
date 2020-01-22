import unittest
from util.password import hash_password
from util.password import check_password


class PasswordTests(unittest.TestCase):

    def test_hash_password(self):
        self.assertNotEqual("password", hash_password("password"))

    def test_check_password_correct(self):
        self.assertTrue(check_password("password", hash_password("password")))

    def test_check_password_incorrect(self):
        self.assertFalse(check_password("not_password", hash_password("password")))
