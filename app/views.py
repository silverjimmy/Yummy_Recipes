"""Module contains all the views for the App"""
from app import app, render_template, request, session, url_for, redirect, flash
from app.classes.planner import Planner

PLAN = Planner()

@app.route('/')
def index():
    """View handles the index page of the app"""
    if 'name' in session:
        return render_template('home.html')
    return redirect(url_for('log_in'))

@app.route('/login', methods=['GET', 'POST'])
def log_in():
    """View handles loging in a user"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if PLAN.login_user(username, password):
            session['name'] = username
            flash("Login success ...")
            return redirect(url_for('index'))
        flash("Login failed ...")
        return render_template('login.html')
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def log_out():
    """View handles longing out a user"""
    if 'name' in session:
        PLAN.logout_user(session['name'])
        session.pop('name', None)
        return redirect(url_for('log_in'))
    return redirect(url_for('log_in'))

@app.route('/createuser', methods=['GET', 'POST'])
def create_user():
    """View handles creating a new User"""
    if request.method == 'POST':
        PLAN.create_user(request.form['fname'],
                         request.form['lname'],
                         request.form['username'],
                         request.form['password'],
                         request.form['email'])
        return redirect(url_for('index'))
    return render_template('newuser.html')

@app.route('/create_recipe', methods=['GET', 'POST'])
def create_recipe():
    """View handles creating a new recipe"""
    if 'name' in session:
        if request.method == 'POST':
            PLAN.users[session['name']].create_recipe(request.form['name'],
                                                      request.form['description'])
            return redirect(url_for('view_recipes'))
        return render_template('newrecipe.html')
    return redirect(url_for('log_in'))

@app.route('/recipes')
def view_recipes():
    """view lists all recipes current"""
    if 'name' in session:
        recipeitem = PLAN.users[session['name']].view_recipes()
        return render_template('recipes.html', recipeitem=recipeitem)
    return redirect(url_for('log_in'))

@app.route('/recipes/<recipe_id>/delete')
def delete_recipe(recipe_id):
    """View handles deleting a recipe"""
    if 'name' in session:
        name = PLAN.get_name_from_id(recipe_id)
        PLAN.users[session['name']].delete_recipe(name)
        return redirect(url_for('view_recipes'))
    return redirect(url_for('log_in'))

@app.route('/create_activity/<recipe_id>', methods=['GET', 'POST'])
def create_activity(recipe_id):
    """view handles creating a recipe"""
    if 'name' in session:
        recipe = PLAN.get_name_from_id(recipe_id)
        if request.method == 'POST':
            PLAN.users[session['name']].create_activity(recipe,
                                                        request.form['name'],
                                                        request.form['description'])
            return redirect(url_for('view_activities', recipe_id=recipe_id))
        return render_template('newactivity.html')
    return redirect(url_for('log_in'))

@app.route('/recipes/<recipe_id>', methods=['GET', 'POST'])
def view_activities(recipe_id):
    """View lists all activities in a recipe"""
    if 'name' in session:
        recipe = PLAN.get_name_from_id(recipe_id)
        activities = PLAN.users[session['name']].view_recipe_activities(recipe)
        return render_template('activities.html',
                               activities=activities,
                               recipe=recipe,
                               recipe_id=recipe_id)
    return redirect(url_for('log_in'))
@app.route('/recipes/<recipe_id>/<activity_id>/delete')
def delete_activity(recipe_id, activity_id):
    """View for deleting an activity"""
    if 'name' in session:
        PLAN.users[session['name']].delete_activity(recipe_id, activity_id)
        return redirect(url_for('view_activities', recipe_id=recipe_id))
    return redirect(url_for('log_in'))
@app.route('/recipes/<recipe_id>/update', methods=['GET', 'POST'])
def update_recipe(recipe_id):
    """View for updating recipe"""
    if 'name' in session:
        if request.method == 'POST':
            PLAN.users[session['name']].update_recipe(recipe_id,
                                                      request.form['name'],
                                                      request.form['description'])
            return redirect(url_for('view_recipes'))
        recipe = PLAN.users[session['name']].get_recipe_from_id(recipe_id)
        return render_template('updaterecipe.html',
                               recipe=recipe)
    return redirect(url_for('log_in'))
@app.route('/recipes/<recipe_id>/<activity_id>/update', methods=['GET', 'POST'])
def update_activity(recipe_id, activity_id):
    """View for updating activity"""
    if 'name' in session:
        if request.method == 'POST':
            PLAN.users[session['name']].update_activity(recipe_id,
                                                        activity_id,
                                                        request.form['name'],
                                                        request.form['description'])
            return redirect(url_for('view_activities', recipe_id=recipe_id))
        activity = PLAN.users[session['name']].get_recipe_from_id
        (recipe_id).object_from_id(activity_id)
        return render_template('updateactivity.html', activity=activity)

    return redirect(url_for('log_in'))
