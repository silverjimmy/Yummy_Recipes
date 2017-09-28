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

    def update_recipe(self, recipe_id, new_name, new_description):
        """Method updates the attributes of the recipe"""
        if self.get_recipe_from_id(recipe_id) in self.recipes:
            for recipe in self.recipes:
                if recipe.recipe_id == recipe_id:
                    recipe.name = new_name
                    recipe.description = new_description
        else:
            return 'invalid'

    def update_activity(self, recipe_id, activity_id, new_name, new_description):
        """Method updates the attributes of the activity"""
        found = False
        if self.get_recipe_from_id(recipe_id) in self.recipes:
            for recipe in self.recipes:
                if recipe.recipe_id == recipe_id:
                    for activity in recipe.activities:
                        if activity.activity_id == activity_id:
                            activity.name = new_name
                            activity.description = new_description
                            found = True
                    if not found:
                        return 'invalid'
        return 'invalid'

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
    def get_recipe_from_id(self, recipe_id):
        """searches a list of objects by id, returns the object if id is found"""
        for recipe in self.recipes:
            if recipe.recipe_id == recipe_id:
                return recipe
