import unittest
from restunl.unetlab import *

UNETLAB_ADDRESS = '192.168.1.21'
USERNAME = 'admin'
PASSWORD = '---'
LAB_NAME = 'unittest_lab'

class UnlTests(unittest.TestCase):

    def setUp(self):
        self.unl = UnlServer(UNETLAB_ADDRESS)
        resp = self.unl.login(USERNAME, PASSWORD)
        self.assertEqual(200, resp.status_code)

    def tearDown(self):
        resp = self.unl.logout()
        self.assertEqual(200, resp.status_code)

class BasicUnlTests(UnlTests):

    def test_status(self):
        resp = self.unl.get_status()
        self.assertEqual(200, resp.status_code)

    def test_templates(self):
        resp = self.unl.get_templates()
        self.assertEqual(200, resp.status_code)

    def test_user_info(self):
        resp = self.unl.get_user_info()
        self.assertEqual(200, resp.status_code)
