import os
from flask import (Flask, flash, render_template, redirect, request, session, url_for)
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


@app.route("/addrecipe")
def addrecipe():
    return render_template("addrecipe.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        user = mongo.db.users
        current_user = user.find_one(
            {"username": request.form.get("username").lower()})
        if current_user:
            if check_password_hash(
                current_user["password"],
                    request.form.get("password")):
                session["username"] = request.form.get("username").lower()
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


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.errorhandler(404)
def page_not_available(e):
    """
    If a 404 error occurs, the user is directed to a custom 404 page.
    """
    return render_template('404.html')


@app.errorhandler(500)
def server_error(e):
    """
    If a 500 error occurs, the user is directed to a custom 500 page.
    """
    return render_template('500.html')


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
