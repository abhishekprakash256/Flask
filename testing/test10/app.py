"""
make the main app for the website 
dummy code

"""

from flask import Flask, render_template


app = Flask(__name__)


app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/article')
def contact():
    return render_template('article-page.html')


@app.route('/showcase')
def card():
    return render_template('showcase.html')

if __name__ == '__main__':
    app.run(debug=True)