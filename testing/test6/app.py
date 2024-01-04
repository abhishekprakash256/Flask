"""
make the main app for the website 
dummy code

"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/new')
def new():
    return render_template('new.html')


"""
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
"""


if __name__ == '__main__':
    app.run(debug=True)

