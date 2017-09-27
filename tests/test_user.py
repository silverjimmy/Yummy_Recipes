"""Module contains unittest for the User class"""
import unittest
from app.classes.user import User

class TestUser(unittest.TestCase):
    """Tests for methods in the user"""

    def setUp(self):
        """Setting up a user to use for each test"""
        self.myuser = User('Bruno',
                           'Herbert',
                           'bruno',
                           '1234',
                           'silverjimmy2@gmail.com')

    def test_create_recipelist_success(self):
        """Testing whether a recipelist was successfully created,
        it should increase the length of self.recipelists"""
        count_before = len(self.myuser.recipelists)
        self.myuser.create_recipelist('African Coffee',
                                      'Try Coffee sundried and roasted coffee beans from kenya')
        count_after = len(self.myuser.recipelists)
        self.assertEqual(count_after, count_before + 1,
                         msg='count_after should equal count_before + 1')

    def test_create_recipelist_non_string_input(self):
        """Method should raise a type error for non string inputs"""
        self.assertRaises(TypeError,
                          self.myuser.create_recipelist,
                          'Boil at 20 degrees', 20,
                          msg="Method only accept string inputs")

    def test_view_recipelists_success(self):
        """View_recipelists should return a list"""
        recipelists = self.myuser.view_recipelists()
        self.assertIsInstance(recipelists, list)

if __name__ == '__main__':
    unittest.main()
