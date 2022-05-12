from flask import Flask, render_template
import views



app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port= 7890) #debugging mode is enabled to show errors on the webapp


