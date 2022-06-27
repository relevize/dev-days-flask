from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<int:fav_number>")
def hello_cat(fav_number):
    return f"<h1>You're favorite number is: {fav_number}!</h1>"
