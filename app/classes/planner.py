"""The Planner class handles all methods partaining to the user object """
from .user import User
class Planner:
    """The planner class contains methods to interact with all the other classes"""

    loged_in = []

    def __init__(self):
        self.users = {}

    def create_user(self, firstname, lastname, username, userpass, email):
        """A method to create a new user"""
        if self.user_exists(username):
            return 'Fail'
        new_user = User(firstname, lastname, username, userpass, email)
        self.users.update({new_user.username:new_user})
        return 'Success'

    def delete_user(self, username):
        """A method to delete an existing user"""
        pass

    def login_user(self, username, userpass):
        """A method to login a user with username and password"""
        if self.user_exists(username) and self.users[username].password == userpass:
            Planner.loged_in.append(self.users[username].username)
            return True
        return False

    def logout_user(self, username):
        """A method to logout a user with given username"""
        Planner.loged_in.remove(username)
    def user_exists(self, username):
        """method checks if the user already exists basing on username"""
        return username in self.users

    def get_name_from_id(self, recipe_id):
        """Methods takes a recipe id and returns its name"""
        found = False
        for user in self.users:
            for recipe in self.users[user].recipes:
                if recipe.recipe_id == recipe_id:
                    found = True
                    return recipe.name
                else:
                    found = False
        if  not found:
            return False
