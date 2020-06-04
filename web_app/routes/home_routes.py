from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print('Visiting the Home Page')
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    print('Visiting the About Page')
    return "About me"