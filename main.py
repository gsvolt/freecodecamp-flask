from flask import Flask, render_template,request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

@app.route("/contact", methods=[ "GET", "POST" ])
def contact():
    if "names" not in session:
        session["names"] = []
    if request.method == "POST":
        name = request.form.get("name")
        session["names"].append(name)
    
    return render_template("contact.html", names=session["names"])

if __name__ == "__main__":
    app.run(debug=True)

