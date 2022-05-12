# # from flask import render_template, redirect

# # from app import app

# from flask import Blueprint


# my_view = Blueprint('my view __name__')



# @my_view.route('')


from flask import render_template


@my_view.route("/home")
def about():
    return render_template("home.html", bands = )
















# @app.route("/")
# def home():
#     return "<h1>Hello world</h1>"