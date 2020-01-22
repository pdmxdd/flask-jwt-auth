import unittest
from models.user import User
from util.password import check_password


class UserTests(unittest.TestCase):

    def test_create_user(self):
        test_user = User("testemail@email.com", "test_password")
        self.assertEqual(test_user.email, "testemail@email.com")
        self.assertTrue(check_password("test_password", test_user.password))
        self.assertFalse(check_password("not_password", test_user.password))
