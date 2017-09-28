"""Module for the User Class"""
from .recipe import recipe
from .activity import Activity


class User:
    """Creates the user object and has methods for creating and
        viewingrecipes and activities"""

    def __init__(self, firstname, lastname, username, password, email):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.recipes = []

    def create_recipe(self, name, description):
        """method creates a new recipe for current user with the given name and description"""
        self.recipes.append(recipe(name, description))

    def create_activity(self, recipe_name, activity_name, description):
        """method creates a new activity with activity_name and
           description in recipe of provided name"""
        new_activity = Activity(activity_name, description)
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                found = True
                recipe.add_activity(new_activity)
        if not found:
            recipe = self.create_recipe(recipe_name, '')
            recipe.add_activity(new_activity)

    def view_recipes(self):
        """method returns all the recipes for the current user"""
        return self.recipes

    def view_recipe_activities(self, recipe_name):
        """method returns a list of activities in a given bucket_list for the current user"""
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                return recipe.activities

    def delete_recipe(self, recipe_name):
        """Method deletes a recipe"""
        if isinstance(recipe_name, str):
            recipe = self.get_object_from_name(recipe_name, self.recipes)
            self.recipes.remove(recipe)
        else:
            raise TypeError('Given Name not a string')

    def delete_activity(self, recipe_id, activity_id):
        """Method deletes activity from recipe """

        for recipe in self.recipes:
            if recipe.recipe_id == recipe_id:
                recipe.remove_activity(activity_id)

    def get_object_from_name(self, item_name, container):
        """searches a list of objects by name returns the object if name found """
        for item in container:
            if item.name == item_name:
                return item
