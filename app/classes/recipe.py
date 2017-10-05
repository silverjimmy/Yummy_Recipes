"""Module for the recipe class """
class recipe:
    """A class for creating and managing recipe objects"""

    recipe_id = 0

    def __init__(self, name, description):
        """class constructor"""
        self.recipe_id = str(recipe.recipe_id + 1)
        self.name = name
        self.description = description
        self.activities = []
        recipe.recipe_id += 1

    def add_activity(self, activity):
        """method to add an activity to the recipe"""
        self.activities.append(activity)

    def remove_activity(self, activity_id):
        """method to remove an activity of a given name from the recipe"""
        activity = self.object_from_id(activity_id)
        if activity in self.activities:
            self.activities.remove(activity)
            return 'Success'
        return 'Activity does not exist'

    def object_from_id(self, activity_id):
        """Returns an activity object"""
        for activity in self.activities:
            if activity.activity_id == activity_id:
                return activity


    