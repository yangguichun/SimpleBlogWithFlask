import unittest
from werkzeug.security import generate_password_hash, check_password_hash

class TestPasswordHash(unittest.TestCase):
    def test_generate_password_hash(self):
        hash = generate_password_hash('mima')
        print('mima的hash是：', hash)

    def test_check_password_hash(self):
        password = 'mima'
        hash = generate_password_hash(password)
        self.assertTrue(check_password_hash(hash, password))
        self.assertFalse(check_password_hash(hash, password+'1'))
