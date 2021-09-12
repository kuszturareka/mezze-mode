import os
from flask import (Flask, flash, render_template, redirect,
                   request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    recipes = mongo.db.recipes.find()
    return render_template("index.html", recipes=recipes)


@app.route("/addrecipe", methods=["GET", "POST"])
def addrecipe():
    if request.method == "POST":
        get_recipe = request.form.get
        recipe = {
           "recipe_name": get_recipe("recipe_name"),
           "image_url": get_recipe("image_url"),
           "description": get_recipe("description"),
           "ingredients_1": get_recipe("ingredients_1"),
           "ingredients_2": get_recipe("ingredients_2"),
           "ingredients_3": get_recipe("ingredients_3"),
           "ingredients_4": get_recipe("ingredients_4"),
           "ingredients_5": get_recipe("ingredients_5"),
           "ingredients_6": get_recipe("ingredients_6"),
           "ingredients_7": get_recipe("ingredients_7"),
           "ingredients_8": get_recipe("ingredients_8"),
           "step_1": get_recipe("step_1"),
           "step_2": get_recipe("step_2"),
           "step_3": get_recipe("step_3"),
           "step_4": get_recipe("step_4"),
           "step_5": get_recipe("step_5"),
           "step_6": get_recipe("step_6"),
           "step_7": get_recipe("step_7"),
           "step_8": get_recipe("step_8"),
           "prep_time": get_recipe("prep_time"),
           "cook_time": get_recipe("cook_time"),
           "servings": get_recipe("servings"),
           "recipe_by": session["username"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("You have succesfully added your recipe!")
        return redirect(url_for("index"))
    return render_template("addrecipe.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        user = mongo.db.users
        current_user = user.find_one(
            {"username": request.form.get("username")})
        if current_user:
            if check_password_hash(current_user["password"], request.form.get("password")):
                session["username"] = request.form.get("username")
                return redirect(url_for("profile",
                                username=session["username"]))
            else:
                flash("You have entered a wrong username/password")
                return redirect(url_for("login"))
        else:
            flash("You have entered the wrong username/password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username")
    flash("You have been successfully logged out")
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        user = mongo.db.users
        username = request.form.get("username")
        password = request.form.get("password")
        confirmed_password = request.form.get("confirm_password")
        active_user = user.find_one({"username": username.lower()})

        if active_user:
            flash("Sorry, the username you have selected already exists",
                  category="error")
            return redirect(url_for("register"))
        elif len(username) < 6:
            flash("Your username must be longer than 6 characters",
                  category="error")
            return redirect(url_for("register"))
        elif len(password) < 7:
            flash("Your password must be be longer than 7 characters",
                  category="error")
            return redirect(url_for("register"))
        elif password != confirmed_password:
            flash("The passwords you have entered do not match",
                  category="error")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(password, method="sha256")
        }
        user.insert_one(register)

        session["username"] = request.form.get("username").lower()
        flash("Hooray! You are now successfully registered",
              category="success")
        return redirect(url_for('profile'))

    return render_template("register.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():

    user = mongo.db.users
    recipes = list(mongo.db.recipes.find())
    username = user.find_one({"username": session["username"]})['username']
    print("username")
    if session["username"]:
        return render_template("profile.html", recipes=recipes)
    else:
        return redirect(url_for("login"))
    if session["username"]:
        return render_template("profile.html", recipes=recipes,
                               username=username)
    else:
        return redirect(url_for("login"))


@app.route("/update<recipe_id>", methods=["GET", "POST"])
def update_recipe(recipe_id):

    if request.method == "POST":
        get_recipe = request.form.get
        new_update = {
           "recipe_name": get_recipe("recipe_name"),
           "image_url": get_recipe("image_url"),
           "description": get_recipe("description"),
           "dietary_info": get_recipe("dietary_info"),
           "ingredients_1": get_recipe("ingredients_1"),
           "ingredients_2": get_recipe("ingredients_2"),
           "ingredients_3": get_recipe("ingredients_3"),
           "ingredients_4": get_recipe("ingredients_4"),
           "ingredients_5": get_recipe("ingredients_5"),
           "ingredients_6": get_recipe("ingredients_6"),
           "ingredients_7": get_recipe("ingredients_7"),
           "ingredients_8": get_recipe("ingredients_8"),
           "step_1": get_recipe("step_1"),
           "step_2": get_recipe("step_2"),
           "step_3": get_recipe("step_3"),
           "step_4": get_recipe("step_4"),
           "step_5": get_recipe("step_5"),
           "step_6": get_recipe("step_6"),
           "step_7": get_recipe("step_7"),
           "step_8": get_recipe("step_8"),
           "prep_time": get_recipe("prep_time"),
           "cook_time": get_recipe("cook_time"),
           "servings": get_recipe("servings"),
           "recipe_by": session["username"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, new_update)
        flash("Your recipe has been updated successfully")
        return redirect(url_for("index"))
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("profile.html", recipes=recipes)


@app.route("/delete/<recipe_id>")
def delete(recipe_id):
    """
    Allows user to delete recipes. The selected recipe is captured by it's id
    and the deleted. The user is then returned to the homepage and flashed a
    message to let them know the recipe has been successfully deleted"
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Your recipe has been succesfully deleted!")
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_available(e):
    """
    If a 404 error occurs, the user is directed to a custom 404 page.
    """
    return render_template("404.html")


@app.errorhandler(500)
def server_error(e):
    """
    If a 500 error occurs, the user is directed to a custom 500 page.
    """
    return render_template("500.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
