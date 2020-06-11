from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return render_template("prediction_form.html")

@home_routes.route("/hello")
def hello():
    print('Visiting the Home Page')
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    print('Visiting the About Page')
    return "About me"