"""Module contains unittests for the recipelist class"""
import unittest
from app.classes.recipe import recipe
from app.classes.activity import Activity

class Testrecipelist(unittest.TestCase):
    """Class contains tests methods in recipelist class"""
    def setUp(self):
        self.myrecipelist = recipe('Coffee',
                                       'Procedure')
        self.myactivity = Activity("Use sundried coffee", "Grill the Coffe seeds")

    def test_add_activity_success(self):
        """Tests whether an activity was added to a recipelist """
        self.myrecipelist.add_activity(self.myactivity)
        self.assertIn(self.myactivity, self.myrecipelist.activities,
                      msg="activity should be in list activities of the recipelist object")

    def test_add_activity_string_input(self):
        """add_activity should raise type error with non activity objects"""
        self.assertRaises(TypeError, self.myrecipelist.add_activity,
                          'activity name',
                          msg="Input should activity object")

    def test_add_activity_integer_input(self):
        """add_activity should raise type error with non activity objects"""
        self.assertRaises(TypeError, self.myrecipelist.add_activity,
                          'activity name', msg="Input should activity object")

    def test_remove_activity_success(self):
        """Test whether activity is removed"""
        self.myrecipelist.add_activity(self.myactivity)
        self.myrecipelist.remove_activity('1')
        self.assertNotIn(self.myrecipelist, self.myrecipelist.activities)

    def test_remove_activity_non_existant(self):
        """Test with an activity that does not exist"""
        status = self.myrecipelist.remove_activity('2')
        self.assertEqual(status, 'Activity does not exist')

    def test_remove_activity_non_string(self):
        """remove_activity should Raise a typeerror if passed a non string"""
        self.assertRaises(TypeError, self.myrecipelist.remove_activity,
                          57, msg="Activity name should be a string")

if __name__ == '__main__':
    unittest.main()
