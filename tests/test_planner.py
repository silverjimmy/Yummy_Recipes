"""Module contains unit tests for the Planner class"""
import unittest
from app.classes.planner import Planner

class TestPlanner(unittest.TestCase):
    """Class to handle tests for the planner class"""

    def setUp(self):
        """Setting up a user and Planner object for every test"""
        self.plan = Planner()
        self.plan.create_user('Okello', 'jackson', 'okello', 'admin', 'okeloo_admin@google.com')
    def test_create_user_success(self):
        """Test a user is created successfully"""
        self.plan.create_user('Bruno', 'Herbert', 'bruno', '1234', 'silverjimmy2@gmail.com')
        self.assertEqual(len(self.plan.users), 2,
                         msg="Length of the the users dictionary should be 2")
    def test_create_user_fail(self):
        """Test failure due to duplicate username"""
        user1 = self.plan.create_user('Bruno',
                                      'Herbert',
                                      'bruno',
                                      '1234',
                                      'silverjimmy2@gmail.com')
        user2 = self.plan.create_user('Bruno',
                                      'Herbert',
                                      'bruno',
                                      '1234',
                                      'silverjimmy2@gmail.com')
        self.assertEqual([user1, user2], ['Success', 'Fail'])

    def test_login_user_success(self):
        """Method updates the loged_in variable of the Planner class"""
        online_before = len(Planner.loged_in)
        self.plan.login_user('okello', 'admin')
        online_after = len(Planner.loged_in)
        self.assertEqual(online_after, online_before + 1)

if __name__ == '__main__':
    unittest.main()
