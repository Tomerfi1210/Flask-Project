from app import app
import unittest


class ApiTests(unittest.TestCase):

    def test_get_user(self):
        tester = app.test_client(self)
        response = tester.get('/users/kelsea_head')
        statuscode = response.status_code
        #TODO
        self.assertEqual(statuscode, 200)

    def test_all_users(self):
        tester = app.test_client(self)
        response = tester.get('/users')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


if __name__ == '__main__':
    unittest.main()