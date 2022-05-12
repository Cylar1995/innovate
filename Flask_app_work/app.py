from flask import Flask, render_template, redirect, Blueprint

# from views import home

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello World</h1>"





@app.route("/about")
def about():
    return render_template("about.html")





if __name__ == "__main__":
    app.run(debug=True, port=7890)

@app.errorhandler (404)
def page_not_found(e):
    render_template("404.html", e=e)
