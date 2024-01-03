
from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """view the about page"""
    return render_template("about.html")

@app.route("/contact")
def contact():
    """view the contact page"""
    return render_template("contact.html")


if __name__ == '__main__':  
   app.run()