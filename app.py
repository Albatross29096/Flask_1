from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello user this is my first flask app"

@app.route("/about")
def about():
    return "This is about us page"

@app.route("/contact")
def contact():
    return "This is us contact page"

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "You sent data!"
    else:
        return "You are only viewing the form"

if __name__ == "__main__":
    app.run(debug=True)
