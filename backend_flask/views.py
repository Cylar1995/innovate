from flask import render_template, redirect

from app import app

@app.route("/")
def home():
    return "index.html"

if __name__ == "__main__":
    app.run(debug=True, port=7890)

@app.errorhandler (404)
def page_not_found(e):
    render_template("404error.html", e=e)